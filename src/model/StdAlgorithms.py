# 
#   Created by Oleh Kurachenko
#          aka okurache
#   on 2018-04-14T05:36:10Z as a part of AxelrodModel4
#   
#   ask me      oleh.kurachenko@gmail.com , I'm ready to help
#   GitHub      https://github.com/OlehKurachenko
#   rate & CV   http://www.linkedin.com/in/oleh-kurachenko-6b025b111
# 

import random

from collections import OrderedDict

from src.model.AlgorithmsSuperclass import Algorithm

class ConstAlgorithm(Algorithm):
    """
       Const decision in any situation, determined in data
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        return data["const_value"]

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        result = OrderedDict()
        result["const_value"] = data["const_value"]
        return result


class EyeForEyeAlgorithm(Algorithm):
    """
        - step: _first step 5, next step the same as competitors previous_
        - analysis: _none_
        - reproduction rule: _none_
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            return 5
        return prev_competitor

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict()


class RandomAlgorithm(Algorithm):
    """
         - step: _random_
        - analysis: _none_
        - reproduction rule: _none_
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        return random.randint(1, 5)

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict()


class EnvyAlgorithm(Algorithm):
    """
        - step: _1 every time_
        - analysis: _none_
        - reproduction rule: _none_
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        return 1

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict()


class AnalysisAlgorithm(Algorithm):
    """
        - step: _first 5 turns are {3, 5, 1, 4, 2} to test behaviour of oponent. It
        it is eye-for-eye then all turns will be 5, if all are the same - 1,
        else - random._
        - analysis: _none_
        - reproduction rule: _none_
    """

    __teststeps = [3, 5, 1, 4, 2]

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        if prev_competitor == -1:
            data["game_mode"] = "analysis"
            data["step_number"] = 0
            data["competitor_steps"] = []
        if data["game_mode"] == "analysis":
            if data["step_number"] > 0:
                data["competitor_steps"].append(prev_competitor)
            if data["step_number"] < 5:
                data["step_number"] += 1
                return AnalysisAlgorithm.__teststeps[data["step_number"] - 1]
            if data["competitor_steps"] == AnalysisAlgorithm.__teststeps:
                data["game_mode"] = "good"
                return 5
            elif all(x==data["competitor_steps"][0] for x in data["competitor_steps"]):
                data["game_mode"] = "bad"
                return 1
            else:
                data["game_mode"] = "mad"
            return 1
        elif data["game_mode"] == "good":
            return 5
        elif data["game_mode"] == "bad":
            return 1
        return random.randint(1, 5)

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        return OrderedDict()


class MutableConstantAlogrithm(Algorithm):
    """
        - step: contant depending on data content
        - analysis: none
        - reproduction rule: 3/5 of population will have the same constant step
        value as parent, 1/5 - +1 (if possible), 1/5 - -1, randomly
    """

    @staticmethod
    def make_step(data: OrderedDict, prev_competitor: int = -1):
        return data["value"]

    @staticmethod
    def analyze_result(data: OrderedDict):
        pass

    @staticmethod
    def reproduce(data: OrderedDict):
        result = OrderedDict()
        rnd = random.randint(1, 5)
        result["value"] = data["value"]
        if (result["value"] != 5) and (rnd == 5):
            result["value"] += 1
        if (result["value"] != 1) and (rnd == 1):
            result["value"] -= 1
        return result


std_algorithms = {
    "eye_for_eye": EyeForEyeAlgorithm,
    "random": RandomAlgorithm,
    "envy": EnvyAlgorithm,
    "analysis": AnalysisAlgorithm,
    "mutable_constant": MutableConstantAlogrithm,
    "const": ConstAlgorithm
}
