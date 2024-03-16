from lib.monologue import Monologue
from lib.memory import LongTermMemory
from lib.event import Event
import lib.llm as llm

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

    def get_next_action(self):
        action_dict = llm.request_action(self.monologue.get_thoughts())
        event = Event(action_dict['action'], action_dict['args'])
        self.latest_action = event
        self.add_event(event)
        return event

    def maybe_perform_latest_action(self):
        if not (self.latest_action and self.latest_action.is_runnable()):
            return
        output = self.latest_action.run(self)
        out_event = Event('output', {'output': output})
        self.add_event(out_event)
        return out_event

