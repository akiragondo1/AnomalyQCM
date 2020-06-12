import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from datetime import datetime, timedelta
import csv

def generateTransition(
        duration,
        sigmoidRatio,
        transitionStart,
        threeSigmaNoiseLevel,
        startAmplitude,
        endAmplitude,
        useDatetime = True,
        stepDuration = 1
       ):
    # Input: curve parameters
    # Output: datetime or scalar dataset with noise
    assert(duration > transitionStart)

    x, stepSize = np.linspace(0, duration, num = int(duration/stepDuration), retstep=True)
    y = [startAmplitude +(endAmplitude-startAmplitude)*(1/(1+np.exp(-sigmoidRatio*(xElement - transitionStart)))) for xElement in x]



    # Todo add noise
    normalRandom = np.random.normal(0, threeSigmaNoiseLevel/3, x.shape)

    signalWithNoise = y + normalRandom

    # Todo add datetime

    referenceDate = datetime(2020,1,1,0,0)
    timeStep = timedelta(0, stepSize)
    timeScale = [(referenceDate+index*timeStep).strftime("%H:%M:%S") for index,_ in enumerate(x)]
    if useDatetime:
        results = np.stack([timeScale, signalWithNoise], axis=-1)
    else:
        results = np.stack([x, signalWithNoise], axis=-1)

    return(results)

def generateDataset(
        size,
        transitionStartTime,
        noiseLevel,
        outputCsvFile
        ):
    print "Generating {} samples of data".format(size)
    resistanceResults = generateTransition(size, 0.1, int(transitionStartTime), noiseLevel, 450, 400)
    frequencyResults = generateTransition(size, 0.005, int(transitionStartTime), noiseLevel*3, 5009491, 5009237)
    samples = np.stack([resistanceResults[:,0],frequencyResults[:,1], resistanceResults[:,1]], axis=-1)
    with open(outputCsvFile, 'w') as outputFile:
        writer = csv.writer(outputFile)
        writer.writerow(['Time', 'Frequency', 'Resistance'])
        for row in samples:
            writer.writerow(row)

