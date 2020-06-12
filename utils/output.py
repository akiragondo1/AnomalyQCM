import numpy as np
import csv
import os
def outputResults(outputName, results):
    curDir = os.path.dirname(os.path.abspath(__file__))
    outputPath = os.path.join(curDir, "../data", outputName + ".csv")
    outputFile = open(outputPath, 'w')
    writer = csv.writer(outputFile, delimiter=',')
    writer.writerow(['Time', 'Frequency', 'Resistance', 'detectionCode', 'anomalyLikelihood'])
    for result in results:
        resultContent = [
            result['Time'],
            result['Frequency'],
            result['Resistance'],
            result['detectionCode'],
            result['anomalyLikelihood']
        ]
        writer.writerow(resultContent)