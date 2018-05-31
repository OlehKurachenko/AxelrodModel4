# 
#   Created by Oleh Kurachenko
#          aka okurache
#   on 2018-04-12T23:59:46Z as a part of AxelrodModel4
#   
#   ask me      oleh.kurachenko@gmail.com , I'm ready to help
#   GitHub      https://github.com/OlehKurachenko
#   rate & CV   http://www.linkedin.com/in/oleh-kurachenko-6b025b111
# 

import json
import sys

from collections import OrderedDict


class Model:
    # TODO write proper comments
    """
    A model
    """

    def __init__(self, state_json_filename: str, points_table_json_filename: str, default_number_of_steps: int = 100):
        with open(state_json_filename, "r") as stateJSONFile:
            self.__state = json.load(stateJSONFile, object_pairs_hook=OrderedDict)
        with open(points_table_json_filename, "r") as pointsTableJSONFile:
            self.__pointsTable = json.load(pointsTableJSONFile, object_pairs_hook=OrderedDict)["table"]
        self.__numberOfSteps = default_number_of_steps
        self.__algorithm = dict()
        # TODO tell about not loaded algorithms

    def perform_step(self, number_of_steps: int = 0):
        if number_of_steps == 0:
            number_of_steps = self.__numberOfSteps
        points_table_size = len(self.__pointsTable)
        old_pool = list(self.__state["pool"])
        for entity in old_pool:
            entity["points"] = 0
        for entity1 in old_pool:
            entity1_algorithm = self.__algorithm[entity1["type"]]
            entity1_data = entity1["data"]
            for entity2 in old_pool:
                entity2_algorithm = self.__algorithm[entity2["type"]]
                entity1_points = 0
                entity2_points = 0
                entity2_data = entity2["data"]
                entity1_step = entity1_algorithm.make_step(entity1_data)
                entity2_step = entity2_algorithm.make_step(entity2_data)
                entity1_points += self.__pointsTable[points_table_size - entity1_step][points_table_size - entity2_step]
                entity2_points += self.__pointsTable[points_table_size - entity2_step][points_table_size - entity1_step]
                for i in range(1, number_of_steps):
                    entity1_previous_step = entity1_step
                    entity2_previous_step = entity2_step
                    entity1_step = entity1_algorithm.make_step(entity1_data, entity2_previous_step)
                    entity2_step = entity2_algorithm.make_step(entity2_data, entity1_previous_step)
                    entity1_points += self.__pointsTable[points_table_size - entity1_step][points_table_size - entity2_step]
                    entity2_points += self.__pointsTable[points_table_size - entity2_step][points_table_size - entity1_step]
                entity1_algorithm.analyze_result(entity1_data)
                entity2_algorithm.analyze_result(entity2_data)
                entity1["points"] += entity1_points
                entity2["points"] += entity2_points
        old_pool.sort(key=lambda x: x["points"], reverse=True)
        # TODO remove or refactor
        # sys.stdout.write("\033[1;31m")
        # print("Here, on run:")
        # sys.stdout.write("\033[0;0m")
        # print(old_pool)
        # end
        old_pool = old_pool[:int(len(old_pool) * 4 / 5 + 1)]
        new_pool = []
        for i in range(min(int(self.__state["pool_size"] / 5), len(old_pool))):
            new_entity = OrderedDict()
            new_entity["type"] = old_pool[i]["type"]
            new_entity["id"] = self.__state["pool_free_id"]
            self.__state["pool_free_id"] += 1
            new_entity["data"] = self.__algorithm[old_pool[i]["type"]].reproduce(old_pool[i]["data"])
            new_pool.append(OrderedDict(new_entity))
        for entity in old_pool:
            del entity["points"]
            new_pool.append(entity)
        self.__state["pool"] = list(new_pool)

    def loadAlgorithms(self, algorithms: dict):
        self.__algorithm.update(algorithms)

    def exportState(self, state_json_filename: str):
        with open(state_json_filename, "w+") as stateJSONFile:
            stateJSONFile.write(json.dumps(self.__state, indent=4))

    def statistics(self):
        resultMap = {}
        for entity in self.__state["pool"]:
            if entity["type"] in resultMap:
                resultMap[entity["type"]] += 1
            else:
                resultMap[entity["type"]] = 1
        return list(resultMap.items())
