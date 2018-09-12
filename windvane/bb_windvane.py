from windvane.windvane import Windvane
from Adafruit_BBIO import ADC as ADC

FRVALUE = 10000

class BBWindvane(Windvane):
    def __init__(self, pinNumber = 'P9_20'):
        self.anemometerPin = pinNumber
        self.fixedResistorValue = FRVALUE
        self.adc = ADC

    def read(self):
        return self.adc.read(self.anemometerPin)

    def setup(self):
        self.adc.setup()

    def set_fixed_resistor_value(self, resistor):
        self.fixedResistorValue = resistor
        return self.fixedResistorValue