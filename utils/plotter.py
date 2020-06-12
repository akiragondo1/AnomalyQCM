import numpy as np
import matplotlib
matplotlib.use('tkagg')
from matplotlib import pyplot as plt
from datetime import datetime

def plotResults(results, title):
    x = [result['Time'] for result in results]
    yRes = [result['Resistance'] for result in results]
    yLikelihood = [result['anomalyLikelihood'] for result in results]
    detectionCode = [result['detectionCode'] for result in results]
    plt.plot(x,yRes)
    plt.plot(x,yLikelihood)
    plt.plot(x,detectionCode)
    plt.title(title)
    plt.show()
    plt.savefig("../results/{}.png".format(title))



def plotFromCSV(results, title):
    x = [datetime.strptime(result['Time'], "%Y-%m-%d %H:%M:%S") for result in results]
    yRes = [float(result['Resistance'])/4 for result in results]
    yLikelihood = [float(result['anomalyLikelihood'])*100 for result in results]
    detectionCode = [float(result['detectionCode']) for result in results]
    for xSample, likelSample in zip(x, yLikelihood):
        if likelSample > 99.999:
            plt.axvline(x=xSample)
    plt.plot(x,yRes)
    plt.plot(x,yLikelihood)
    plt.plot(x,detectionCode)
    plt.axhline(y=99)
    plt.title(title)
    plt.show()
    plt.savefig("../results/{}.png".format(title))