from SportsCenterState.State import State

class EndState(State):
    def handle(self, booking):
        print("finish")