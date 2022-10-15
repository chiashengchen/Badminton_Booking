 
# from Thread.Booking import Booking # circular import ??

class State :
    url : str
    appointmentInterval : int
    court : int
    # booking : Booking
        
    def handle(self, booking):
        raise NotImplementedError("Not implement method yet !")