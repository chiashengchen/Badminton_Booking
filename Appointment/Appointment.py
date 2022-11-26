from Center.CenterFactory import CenterFactory
from Content.Content import Content
import threading

class Appointment :
    def __init__(self, time, infos, type):
        lock = threading.Lock()
        center, state = CenterFactory.createCenter(time, type)
        self._contents = []
        for info in infos:
            content = Content(center, info, state, time, lock)
            self._contents.append(content)
        
    def start(self):
        for content in self._contents:
            content.start()