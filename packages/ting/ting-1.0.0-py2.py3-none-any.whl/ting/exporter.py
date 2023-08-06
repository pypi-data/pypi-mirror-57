# -*- coding: utf-8 -*-
import pickle

from six import string_types


class TingsExporter(object):
    def __init__(self):

        pass

    def export_tings(self, tingset, ting_names=None):

        if ting_names is None:
            ting_names = list(tingset.keys())
        elif isinstance(ting_names, string_types):
            ting_names = [ting_names]

        export_set = {}
        for tn in ting_names:

            ting = tingset.get(tn)
            pickle.dump(ting, open("save.p", "wb"))

            # frozen = jsonpickle.encode(ting)
            # export_set[tn] = frozen

        return export_set

        # if exclude_attributes is None:
        #     exclude_attributes = []
        # elif isinstance(exclude_attributes, string_types):
        #     exclude_attributes = [exclude_attributes]
        #
        # export_set = {}
        # for tn in ting_names:
        #     ting = tingset.get(tn)
        #     temp = {}
        #     for an in ting._ting_attribute_names:
        #         print(an)
        #         if an in exclude_attributes:
        #             temp.setdefault("__excluded__", []).append(an)
        #             continue
        #
        #         attr = getattr(ting, an)
        #         from frutils.frutils_cli import output
        #         try:
        #             output(attr, output_type="pformat")
        #         except Exception as e:
        #             print(e)
        #         json_string = simplejson.dumps(attr, for_json=True)
        #
        #         temp[an] = json_string
        #
        #     export_set[tn] = temp
