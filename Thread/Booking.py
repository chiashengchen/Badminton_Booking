from SportsCenterState.State import State
import threading

class Booking(threading.Thread) :
    state : State

    def __init__(self, state) :
        threading.Thread.__init__(self)
        self.state = state

    def handle(self):
        self.state.handle(self)

    def setState(self, state):
        self.state = state

    def run(self):
        self.handle()