from lib.monologue import Monologue
from lib.memory import LongTermMemory

MAX_MONOLOGUE_LENGTH = 20000

class Agent:
    def __init__(self):
        self.monologue = Monologue()
        self.memory = LongTermMemory()

    def add_event(self, event):
        self.monologue.add_event(event)
        self.memory.add_event(event)
        if self.monologue.get_total_length() > MAX_MONOLOGUE_LENGTH:
            self.monologue.condense()
