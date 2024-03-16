from lib.monologue import Monologue
from lib.memory import LongTermMemory

class Agent:
    def __init__(self):
        self.monologue = Monologue()
        self.memory = LongTermMemory()

    def add_thought(self, thought):
        self.monologue.add_thought(thought)
        self.memory.add_thought('thought', thought)
        if self.monologue.get_total_length() > 2000:
            self.monologue.condense()
