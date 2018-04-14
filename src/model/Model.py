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

from collections import OrderedDict


class Model:
    # TODO write proper comments
    """
    A model
    """

    def __init__(self, stateJSONFilename: str, pointsTableJSONFilename: str, defaultNumberOfSteps: int = 100):
        self.__state = json.load(stateJSONFilename, object_pairs_hook=OrderedDict)
        self.__pointsTable = json.load(pointsTableJSONFilename, object_pairs_hook=OrderedDict)
        self.__numberOfSteps = defaultNumberOfSteps
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
            entity1_points = entity1["points"]
            entity1_data = entity1["data"]
            for entity2 in old_pool:
                entity2_algorithm = self.__algorithm[entity2["type"]]
                entity2_points = entity2["points"]
                entity2_data = entity2["data"]
                entity1_step = entity1_algorithm.makeStep(entity1_data)
                entity2_step = entity2_algorithm.makeStep(entity2_data)
                entity1_points += self.__pointsTable[points_table_size - entity1_step][points_table_size - entity2_step]
                entity2_points += self.__pointsTable[points_table_size - entity2_step][points_table_size - entity1_step]
                for i in range(1, number_of_steps):
                    entity1_previous_step = entity1_step
                    entity2_previous_step = entity2_step
                    entity1_step = entity1_algorithm.makeStep(entity1_data, entity2_previous_step)
                    entity2_step = entity2_algorithm.makeStep(entity2_data, entity1_previous_step)
                    entity1_points += self.__pointsTable[points_table_size - entity1_step][points_table_size - entity2_step]
                    entity2_points += self.__pointsTable[points_table_size - entity2_step][points_table_size - entity1_step]
                entity1_algorithm.analyzeRezult(entity1_data)
                entity2_algorithm.analyzeRezult(entity2_data)
        old_pool.sort(key=lambda x: x["points"])
        old_pool = old_pool[:(len(old_pool) * 4 / 5 + 1)]
        new_pool = []
        for i in range(min(self.__state["pool_size"] / 5, len(old_pool))):
            new_pool.append(self.__algorithm[old_pool[i]["type"]].reproduce(old_pool[i]["data"]))
        for entity in old_pool:
            del entity["points"]
        new_pool.append(old_pool)
        self.__state["pool"] = list(new_pool)

    def loadAlgorithms(self, algorithms: dict):
        self.__algorithm.update(algorithms)

