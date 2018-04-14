# 
#   Created by Oleh Kurachenko
#          aka okurache
#   on 2018-04-14T05:36:10Z as a part of AxelrodModel4
#   
#   ask me      oleh.kurachenko@gmail.com , I'm ready to help
#   GitHub      https://github.com/OlehKurachenko
#   rate & CV   http://www.linkedin.com/in/oleh-kurachenko-6b025b111
# 

from collections import OrderedDict


class ConstAlgorithm:
    """
       Const decision in any situation, determined in data
    """

    @staticmethod
    def make_step(data: OrderedDict, prevCompetitor: int = -1):
        return data["const_value"]

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        result = OrderedDict()
        result["const_value"] = data["const_value"]
        return result


std_algorithms = {"const": ConstAlgorithm}
