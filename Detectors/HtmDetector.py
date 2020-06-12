from meta import IAnomaly
from nupic.frameworks.opf.model_factory import ModelFactory
from nupic.algorithms.anomaly_likelihood import AnomalyLikelihood
import yaml
import copy
from tqdm import tqdm

class HTMDetector(IAnomaly):
    def __init__(self, params_file, stabilizationTime):
        """
        :param params_file: path  to params file [yaml]
        :param stabilizationTime: stabilizationTime[samples]
        """
        with open(params_file, 'r') as p_file:
            modelParams = yaml.safe_load(p_file)
            self.model = ModelFactory.create(modelParams)
            self.model.enableInference({"predictedField": "Resistance"})
            self.anomalyLikelihood = AnomalyLikelihood()
            self.samplesUntilStable = stabilizationTime
            self.samples = []

    def isStable(self):
        if self.samplesUntilStable >= 0:
            return False
        else:
            return True

    def detect(self, new_data):
        self.samplesUntilStable = self.samplesUntilStable - 1
        self.samples = self.samples + 1
        result = self.model.run(new_data)
        anomalyScore = result.inferences["anomalyScore"]
        currentAnomalyLikelihood = self.anomalyLikelihood.anomalyProbability(
            value=new_data["Resistance"],
            anomalyScore=anomalyScore,
            timestamp=new_data["Time"]
        )
        dictHeaders = ['detectionCode', 'anomalyLikelihood', 'anomalyScore']
        if self.isStable():
            if currentAnomalyLikelihood > 0.9999:
                print "Detected High anomaly at sample number {}".format(self.samples)
                return dict(zip(dictHeaders, [3, currentAnomalyLikelihood, anomalyScore]))
            elif currentAnomalyLikelihood > 0.95:
                return dict(zip(dictHeaders,[2, currentAnomalyLikelihood, anomalyScore]))
            elif currentAnomalyLikelihood > 0.90:
                return dict(zip(dictHeaders,[1, currentAnomalyLikelihood, anomalyScore]))
            else:
                return dict(zip(dictHeaders,[0, currentAnomalyLikelihood, anomalyScore]))
        else:
            return dict(zip(dictHeaders,[-1, currentAnomalyLikelihood, anomalyScore]))

    def detectFromList(self, data):
        results = []
        print "Detecting anomalies for {} samples of data".format(data.__len__())
        for data_point in tqdm(data):
            detection = self.detect(data_point)
            result = copy.copy(data_point)
            result.update(detection)
            results.append(result)
        return results
