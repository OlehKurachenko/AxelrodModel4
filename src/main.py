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
import model.Model as Model


if __name__ == "__main__":
    model1 = Model.Model("../data/model2_s_0.json", "../data/table.json")
    model1.loadAlgorithms(StdAlgo.std_algorithms)
    model1.perform_step()
    model1.exportState("../data/model2_s_1g.json")
    model1.perform_step()
    model1.exportState("../data/model2_s_2g.json")
    model1.perform_step()
    model1.exportState("../data/model2_s_3g.json")
    model1.perform_step()
    model1.exportState("../data/model2_s_4g.json")
