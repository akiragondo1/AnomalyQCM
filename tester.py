from Detectors.HtmDetector import HTMDetector
import os
from utils.loader import loadCsv
from utils.plotter import plotResults,plotFromCSV
from utils.output import outputResults
from utils.generator import generateDataset
from Detectors.OCSVM import OCSVMDetector
from Detectors.iForest import IForestDetector
import csv

_EXAMPLE_DIR = os.path.dirname(os.path.abspath(__file__))
_PARAMS_PATH = os.path.join(_EXAMPLE_DIR, "params", "model.yaml")
_DATA_PATH = os.path.join(_EXAMPLE_DIR, "data", "OLIVIA2.csv")
stabilizationTime = 1000


#htmDetector = HTMDetector(_PARAMS_PATH, 1000)
svmDetector = IForestDetector(1000)
# results = htmDetector.detectFromList(loadCsv(_DATA_PATH))
results = svmDetector.detectFromList(loadCsv(_DATA_PATH))

# with open('../data/AnomalyTest-LowerResolution.csv', 'r') as f:
#     reader = csv.reader(f)
#     headers = reader.next()
#     results = [dict(zip(headers, record)) for record in reader]
#     plotFromCSV(results, 'Anomaly Detection test')
plotResults(results, 'OCSVM Anomaly Detection test Olivia')
outputResults('OCSVM AnomalyOlivia-HigherThreshold', results)

#generateDataset(40000, 32000, 10, '../data/testDataset.csv')