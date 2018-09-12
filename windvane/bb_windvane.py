from windvane.windvane import Windvane
from Adafruit_BBIO import ADC as ADC

FRVALUE = 10000

class BBWindvane(Windvane):
    def __init__(self, pinNumber = 'P9_36'):
        self.wvPin = pinNumber
        self.fixedResistorValue = FRVALUE
        self.adc = ADC

    def wind_direction(self, rawReading):
        return self.direction_text(rawReading * 3.3)

    def read(self):
        return self.adc.read(self.wvPin)

    def setup(self):
        self.adc.setup()

    def set_fixed_resistor_value(self, resistor):
        self.fixedResistorValue = resistor
        return self.fixedResistorValue
