# 
#   Created by Oleh Kurachenko
#          aka okurache
#   on 2018-04-14T06:13:22Z as a part of AxelrodModel4
#   
#   ask me      oleh.kurachenko@gmail.com , I'm ready to help
#   GitHub      https://github.com/OlehKurachenko
#   rate & CV   http://www.linkedin.com/in/oleh-kurachenko-6b025b111
# 

from collections import OrderedDict


class Algorithm:
    """
       SuperClass for all algorithm classes
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        pass

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        pass