# -*- coding: utf-8 -*-
import copy
import logging
import os
import sys

from jinja2 import Environment, FileSystemLoader
from six import string_types

from frutils import dict_merge
from frutils.jinja2_filters import ALL_FILTERS
from ting.ting_attributes import TingAttribute


log = logging.getLogger("freckles")

GLOBAL_RENDER_JINJA_ENV_CACHE = {}


class JinjaTemplateMixin(object):
    def __init__(self, *args, **kwargs):

        pass

    def render_template(self, ting_repl_name, template, extra_repl_dict=None):

        if extra_repl_dict is None:
            repl_dict = {}
        else:
            repl_dict = copy.copy(extra_repl_dict)

        repl_dict[ting_repl_name] = self

        try:
            rendered = template.render(**repl_dict)
        except (Exception) as e:
            log.debug("Error rendering ting '{}': {}".format(self.id, e), exc_info=1)
            raise e

        return rendered


class JinjaTemplateAttribute(TingAttribute):
    def __init__(
        self,
        template,
        target_attr_name=None,
        template_dir=None,
        required_attrs=None,
        constants=None,
    ):

        if template_dir is None:
            if not hasattr(sys, "frozen"):
                template_dir = os.path.join(os.path.dirname(__file__), "templates")
            else:
                template_dir = os.path.join(
                    sys._MEIPASS, "ting", "attributes", "templates"
                )

        if required_attrs is None:
            required_attrs = []
        if isinstance(required_attrs, string_types):
            required_attrs = [required_attrs]
        self.required_attrs = required_attrs
        self.template = template

        if target_attr_name is None:
            target_attr_name = os.path.splitext(template)[0]
        self.target_attr_name = target_attr_name

        self.template_dir = template_dir
        self.template_filters = ALL_FILTERS

        if constants is None:
            constants = {}
        self.constants = constants

        self.use_cache = False

        global GLOBAL_RENDER_JINJA_ENV_CACHE

        if (
            not self.use_cache
            or GLOBAL_RENDER_JINJA_ENV_CACHE.get(self.template, None) is None
        ):
            self.jinja_env = Environment(loader=FileSystemLoader(self.template_dir))

            if self.template_filters:
                for tn, tf in self.template_filters.items():
                    self.jinja_env.filters[tn] = tf["func"]

            GLOBAL_RENDER_JINJA_ENV_CACHE[template] = self.jinja_env
        else:
            self.jinja_env = GLOBAL_RENDER_JINJA_ENV_CACHE[template]

    def provides(self):

        return [self.target_attr_name]

    def requires(self):

        return self.required_attrs

    def get_attribute(self, ting, attribute_name=None):

        try:
            rendered = self.render(ting)
            return rendered
        except (Exception) as e:

            return "<p>Can't render ting {}: {}".format(ting.id, e)

    def render(self, frecklet):

        repl_dict = {}
        for req in self.required_attrs:
            repl_dict[req] = getattr(frecklet, req)

        repl_dict = dict_merge(self.constants, repl_dict, copy_dct=True)

        template = self.jinja_env.get_template(self.template)

        try:
            rendered = template.render(**repl_dict)
        except (Exception) as e:
            import traceback

            traceback.print_exc()
            raise e

        return rendered
