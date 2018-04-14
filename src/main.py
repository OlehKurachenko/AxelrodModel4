# 
#   Created by Oleh Kurachenko
#          aka okurache
#   on 2018-04-14T05:08:26Z as a part of AxelrodModel4
#   
#   ask me      oleh.kurachenko@gmail.com , I'm ready to help
#   GitHub      https://github.com/OlehKurachenko
#   rate & CV   http://www.linkedin.com/in/oleh-kurachenko-6b025b111
# 

import model.StdAlgorithms as StdAlgo
import model.Gen2018 as Gen2018Algo
import model.Model as Model


def run_model_1():
    model1 = Model.Model("../data/model2_s_0.json", "../data/table.json")
    model1.loadAlgorithms(StdAlgo.std_algorithms)
    for i in range(10):
        model1.perform_step()
        print(str(i) + str(model1.statistics()))


def run_model_2():
    model2 = Model.Model("../data/model_pure_gen2018_s_0.json", "../data/table.json")
    model2.loadAlgorithms(Gen2018Algo.gen2018_algorithms)
    for i in range(10):
        model2.perform_step()
        print(str(i) + str(model2.statistics()))

def run_model_3():
    model3 = Model.Model("../data/model_gen2018_s_0.json", "../data/table.json")
    model3.loadAlgorithms(Gen2018Algo.gen2018_algorithms)
    model3.loadAlgorithms(StdAlgo.std_algorithms)
    for i in range(30):
        model3.perform_step()
        print(str(i) + str(model3.statistics()))

def run_model_4():
    model3 = Model.Model("../data/model3_s_0.json", "../data/table.json")
    model3.loadAlgorithms(StdAlgo.std_algorithms)
    for i in range(10):
        model3.perform_step()
        print(str(i) + str(model3.statistics()))

def interestingPart1():
    print("@@@ Simulation 1:")
    model1 = Model.Model("../data/model_pure_gen2018_interesting1_s_0.json", "../data/table.json")
    model1.loadAlgorithms(Gen2018Algo.gen2018_algorithms)
    for i in range(15):
        model1.perform_step()
        print(str(i) + str(model1.statistics()))
    print("@@@ Simulation 2:")
    model2 = Model.Model("../data/model_pure_gen2018_interesting2_s_0.json", "../data/table.json")
    model2.loadAlgorithms(Gen2018Algo.gen2018_algorithms)
    for i in range(25):
        model2.perform_step()
        print(str(i) + str(model2.statistics()))

if __name__ == "__main__":
    run_model_4()
    # interestingPart1()