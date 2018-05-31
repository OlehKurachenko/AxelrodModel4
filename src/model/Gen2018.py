# 
#   Created by Oleh Kurachenko
#          aka okurache
#   on 2018-04-14T07:17:42Z as a part of AxelrodModel4
#   
#   ask me      oleh.kurachenko@gmail.com , I'm ready to help
#   GitHub      https://github.com/OlehKurachenko
#   rate & CV   http://www.linkedin.com/in/oleh-kurachenko-6b025b111
# 

import random

from collections import OrderedDict

from src.model.AlgorithmsSuperclass import Algorithm


class VitaliaAlgo(Algorithm):
    """
        - step: _first step: 3, all next: competitor-1_
        - analysis: _none_
        - reproduction rule: _none_
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            return 3
        if prev_competitor == 1:
            return 1
        return prev_competitor - 1

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict()

class KT1Algo(Algorithm):
    """
        - step: _first step: random, then, the next loop for each 6 steps:_
            - 1, 3: competitor+2
            - 2, 4: competitor-2
            - 5: 6 - (competitor on loop step 2)
            - 6: 6 - (competitor on loop step 3)
        - analysis: _none_
        - reproduction rule: _none_
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            data["step"] = 0
            return random.randint(1, 5)
        data["step"] += 1
        if data["step"] == 1:
            return min(prev_competitor + 2, 5)
        if data["step"] == 2:
            data["on1"] = prev_competitor
            return max(prev_competitor - 2, 1)
        if data["step"] == 3:
            data["on2"] = prev_competitor
            return min(prev_competitor + 2, 5)
        if data["step"] == 4:
            return max(prev_competitor - 2, 1)
        if data["step"] == 5:
            return 6 - data["on1"]
        if data["step"] == 6:
            data["step"] = 0
            return 6 - data["on2"]

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        result = OrderedDict()
        result["step"] = 0
        result["on1"] = 0
        result["on2"] = 0
        return result


class KT2Algo(Algorithm):
    """
        - step: _first step: 3, all next: 6 - competitor_
        - analysis: _none_
        - reproduction rule: _none_
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            return 3
        assert ((6 - prev_competitor) >= 1), str(6 - prev_competitor) + "->" + str(prev_competitor)
        return 6 - prev_competitor

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict()


class BB1601Algo(Algorithm):
    """
        - step: _in loop for each 8 steps:_
            - 1: random
            - 2: 3
            - 3: competitor-1
            - 4: competitor-1
            - 5: 4
            - 6: 2
            - 7: competitor+1
            - 8: competitor+1
        - analysis: _none_
        - reproduction rule: _none_
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            data["step"] = 1
        data["step"] += 1
        if data["step"] == 1:
            return random.randint(1, 5)
        elif data["step"] == 2:
            return 3
        elif data["step"] == 3 or data["step"] == 4:
            return max(prev_competitor - 1, 1)
        elif data["step"] == 5:
            return 4
        elif data["step"] == 6:
            return 2
        elif data["step"] == 7:
            return min(prev_competitor + 1, 5)
        data["step"] = 0
        return min(prev_competitor + 1, 5)


    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict({"step": 0})


class May048beAlgo(Algorithm):
    """
        - step: _in loop for each 6 steps:_
            - 1: 3
            - 2: competitor-1
            - 3: competitor+1
            - 4: 4
            - 5: 3
            - 6: competitor-1
        - analysis: _none_
        - reproduction rule: _none_
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            data["step"] = 0
        data["step"] += 1
        if data["step"] == 1:
            return 3
        elif data["step"] == 2:
            return max(prev_competitor - 1, 1)
        elif data["step"] == 3:
            return min(prev_competitor + 1, 5)
        elif data["step"] == 4:
            return 4
        elif data["step"] == 5:
            return 3
        data["step"] = 0
        return max(prev_competitor - 1, 1)

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict({"step": 0})


class AndrewAlgo(Algorithm):
    """
        - step: _in loop for each 5 steps:_
            - 1: 3
            - 2: competitor-1
            - 3: competitor+1
            - 4: 3
            - 5: competitor-1
        - analysis: _none_
        - reproduction rule: _none_
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            data["step"] = 0
        data["step"] += 1
        if data["step"] == 1:
            return 3
        elif data["step"] == 2:
            return max(prev_competitor - 1, 1)
        elif data["step"] == 3:
            return min(prev_competitor + 1, 5)
        elif data["step"] == 4:
            return 3
        data["step"] = 0
        return max(prev_competitor - 1, 1)

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict({"step": 0})


class IllyaAAlgo(Algorithm):
    """
        - step: first step: 3, then [1, 2, 3, 4, 5] -> [2, 3, 4, 5, 1]
        - analysis: _none_
        - reproduction rule: _none_
    """

    __reaction = [2, 3, 4, 5, 1]

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            return 3
        return IllyaAAlgo.__reaction[prev_competitor - 1]

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict()


class IllyaBAlgo(Algorithm):
    """
        - step: first step: 4, then [1, 2, 3, 4, 5] -> [3, 4, 5, 4, 2]
        - analysis: _none_
        - reproduction rule: _none_
    """

    __reaction = [3, 4, 5, 4, 2]

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            return 4
        return IllyaBAlgo.__reaction[prev_competitor - 1]

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict()


class IllyaCAlgo(Algorithm):
    """
        - step: first step: 5, then [1, 2, 3, 4, 5] -> [5, 3, 1, 5, 3]
        - analysis: _none_
        - reproduction rule: _none_
    """

    __reaction = [5, 3, 1, 5, 3]

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            return 5
        return IllyaCAlgo.__reaction[prev_competitor - 1]

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict()


class SergeyAAlgo(Algorithm):
    """
        - step: _in loop for each 5 steps:_
            - 1: 3
            - 2: 3
            - 3: 4
            - 4: 3
            - 5: 4
        - analysis: _none_
        - reproduction rule: _none_
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            data["step"] = 0
        data["step"] += 1
        if data["step"] == 1:
            return 3
        elif data["step"] == 2:
            return 3
        elif data["step"] == 3:
            return 4
        elif data["step"] == 4:
            return 3
        data["step"] = 0
        return 4

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict({"step": 0})


class NovyMishaAlgo(Algorithm):
    """
        - step: _in loop for each 3 steps:_
            - 1: 3
            - 2-3: competitor-1
        - analysis: _none_
        - reproduction rule: _none_
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            data["step"] = 0
        data["step"] += 1
        if data["step"] == 1:
            return 3
        elif data["step"] == 2:
            return max(prev_competitor - 1, 1)
        data["step"] = 0
        return max(prev_competitor - 1, 1)

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict({"step": 0})


class AnyaAlgo(Algorithm):
    """
        - step: _in loop for each 4 steps:_
            - 1: 4
            - 2: competitor-1
            - 3: 3
            - 4: competitor-1
        - analysis: _none_
        - reproduction rule: _none_
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            data["step"] = 0
        data["step"] += 1
        if data["step"] == 1:
            return 4
        elif data["step"] == 2:
            return max(prev_competitor - 1, 1)
        elif data["step"] == 3:
            return 3
        data["step"] = 0
        return max(prev_competitor - 1, 1)

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict({"step": 0})


class KIAlgo(Algorithm):
    """
        - step: _steps 1-7: 2. Then, if there were 3 the same in row, 2 on 3-5,
        1 on 1-2. Else 1 in any case._
        - analysis: _none_
        - reproduction rule: _none_
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            data["step"] = 0
            data["competitor"] = []
        data["step"] += 1
        if data["step"] < 9:
            if data["step"] != 1:
                data["competitor"].append(prev_competitor)
            return 2
        elif data["step"] == 10:  # mode 1
            if prev_competitor >= 3:
                return 2
            return 1
        elif data["step"] == 11:  # mode 2
            return 1
        if (data["competitor"][0] == data["competitor"][1] == data["competitor"][2]) or \
                (data["competitor"][1] == data["competitor"][2] == data["competitor"][3]) or \
                (data["competitor"][2] == data["competitor"][3] == data["competitor"][4]) or \
                (data["competitor"][3] == data["competitor"][4] == data["competitor"][5]) or \
                (data["competitor"][4] == data["competitor"][5] == data["competitor"][6]):
            data["step"] = 10
        else:
            data["step"] = 11
        return 2

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict({"step": 0, "competitor": []})


gen2018_algorithms = {
    "vitalia": VitaliaAlgo,
    "kt-1": KT1Algo,
    "kt-2": KT2Algo,
    "bb1601": BB1601Algo,
    "may048be": May048beAlgo,
    "andrew": AndrewAlgo,
    "illya-a": IllyaAAlgo,
    "illya-b": IllyaBAlgo,
    "illya-c": IllyaCAlgo,
    "sergey-a": SergeyAAlgo,
    "novy_misha": NovyMishaAlgo,
    "anya": AnyaAlgo,
    "ki": KIAlgo
}
