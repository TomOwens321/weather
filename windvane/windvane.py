class Windvane:
    def __init__(self):
        pass
    
    def direction_text( self, dir ):
        dir = int(dir * 100)
        if dir in range(239, 260):
            return "N  "
        if dir in range(111, 140):
            return "NNE"
        if dir in range(140, 171):
            return "NE "
        if dir in range(24, 28):
            return "ENE"
        if dir in range(28, 35):
            return "E  "
        if dir in range(1, 24):
            return "ESE"
        if dir in range(50, 69):
            return "SE "
        if dir in range(35, 50):
            return "SSE"
        if dir in range(85, 111):
            return "S  "
        if dir in range(69, 85):
            return "SSW"
        if dir in range(198, 214):
            return "SW "
        if dir in range(171, 198):
            return "WSW"
        if dir in range(295, 400):
            return "W  "
        if dir in range(260, 276):
            return "WNW"
        if dir in range(276, 295):
            return "NW "
        if dir in range(214, 239):
            return "NNW"
        return str(dir)