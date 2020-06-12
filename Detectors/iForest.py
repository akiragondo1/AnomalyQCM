from sklearn.ensemble import IsolationForest
import numpy as np
import copy
from tqdm import tqdm
from meta import IAnomaly
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class IForestDetector(IAnomaly):
    def __init__(self, slidingWindowSize = None):
        self.slidingWindowSize = slidingWindowSize
        self.receivedSamplesNumber = 0
        self.currentSamples = []
        self.clf = IsolationForest()
        self.dictHeaders = ['detectionCode', 'anomalyLikelihood', 'anomalyScore']

    def appendNewData(self, sample):
        self.currentSamples.append(float(sample["Resistance"]))
        self.receivedSamplesNumber = self.receivedSamplesNumber +1
    def detect(self, new_data):
        if self.receivedSamplesNumber < self.slidingWindowSize - 1:
            #Append all of the stabilization samples
            self.appendNewData(new_data)
            return dict(zip(self.dictHeaders, [-1, -1, -1]))
        else:
            #Remove one from current samples and add new data
            self.currentSamples.pop(0)
            self.appendNewData(new_data)
            result = self.clf.fit_predict(np.array(self.currentSamples).reshape(-1,1))[-1]
            likelihood = self.clf.score_samples(np.array(self.currentSamples).reshape(-1,1))[-1]
            return dict(zip(self.dictHeaders, [result, likelihood, -1]))
    def detectFromList(self, data):
        results = []
        print "Detecting anomalies for {} samples of data".format(data.__len__())
        for data_point in tqdm(data):
            detection = self.detect(data_point)
            result = copy.copy(data_point)
            result.update(detection)
            results.append(result)
        return results
