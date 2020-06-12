import csv
import numpy as np
from datetime import datetime

def loadCsv(pathToCsv):
    """
    :param pathToCsv: path to the csv
    :return: [Time(datetime), Frequency(float), Resistance(float)] list
    """
    with open(pathToCsv, 'r') as fin:
        reader = csv.reader(fin)
        headers = reader.next()
        results = []
        for record in reader:
            sample = dict(zip(headers, record))
            time = datetime.strptime(
                sample["Time"],
                "%H:%M:%S"
            )
            frequency = float(sample["Frequency"])
            resistance = float(sample["Resistance"])
            result = {
                'Time': time,
                'Frequency': frequency,
                'Resistance': resistance}
            results.append(result)
        return results
