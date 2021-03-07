class Clock:
    def __init__(self, hour, minute):
        self.minute = abs(minute%60)
        self.hour = (hour+minute//60) % 24
       
    def __repr__(self):
        return str(self.hour).zfill(2) + ':' + str(self.minute).zfill(2)

    def __eq__(self, other):
        if self.hour == other.hour and self.minute == other.minute:
            return True
        return False

    def __add__(self, minutes):
        self = Clock(self.hour, self.minute + minutes)
        return self

    def __sub__(self, minutes):
        self = Clock(self.hour, self.minute - minutes)
        return self