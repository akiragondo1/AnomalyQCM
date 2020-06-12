from Detectors.HtmDetector import HTMDetector
import os

_EXAMPLE_DIR = os.path.dirname(os.path.abspath(__file__))
_PARAMS_PATH = os.path.join(_EXAMPLE_DIR, "params", "model.yaml")

a = HTMDetector(_PARAMS_PATH, )
print(a.detect)