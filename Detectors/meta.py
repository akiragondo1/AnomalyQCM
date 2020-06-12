from abc import ABCMeta, abstractmethod

class IAnomaly(object):
    __metaclass__ = ABCMeta


    @abstractmethod
    def detect(self, new_data):
        """
        :param new_data: New Data point as dict with {
            Time: time[datetime],
            Frequency: Frequency[float],
            Resistance: Resistance[float]
        :return {
            detectionCode: detectionCode,
            anomalyLikelihood: anomalyLikelihood(optional)
            }
            detectionCode: 0 for not detected, 1 for low detected (>90), 2 for medium (>95),
            3 for high (>99) -1 for unstable
        """
        raise NotImplementedError

    @abstractmethod
    def detectFromList(self, data):
        """
        :param data: list of data with [Time[datetime], Frequency[float], Resistance[float]]
        :return: list if [Time[datetime], Frequency[float], Resistance[float], detectedCode, anomalyLikelihood(optional)]
        """
        raise NotImplementedError
