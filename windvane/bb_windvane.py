from windvane.windvane import Windvane
from Adafruit_BBIO import ADC as ADC

class BBWindvane(Windvane):
    def __init__(self, **kwargs):
        pass

    def read(self):
        return 1.2