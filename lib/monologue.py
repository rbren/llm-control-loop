import lib.json as json

import lib.llm as llm

class Monologue:
    def __init__(self):
        self.thoughts = []

    def add_event(self, t):
        self.thoughts.append(t)

    def get_thoughts(self):
        return self.thoughts

    def get_total_length(self):
        return sum([len(json.dumps(t)) for t in self.thoughts])

    def condense(self):
        self.thoughts = llm.summarize_monologue(self.thoughts)

