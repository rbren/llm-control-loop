import json

import lib.llm as llm

class Monologue:
    def __init__(self):
        self.thoughts = []

    def add_thought(self, t):
        self.thoughts.append(t)

    def get_thoughts(self):
        return self.thoughts

    def condense(self):
        prompt = """
Below is the internal monologue of an automated LLM agent. Each
thought is an item in a JSON array.

Please return a new, smaller JSON array, which summarizes the
internal monologue. You can summarize individual thoughts, and
you can condense related thoughts together with a description
of their content.

```json
"""
        prompt += json.dumps(self.thoughts, indent=2)
        prompt += "\n```"
        answer = llm.sendJSONPrompt(prompt)
        self.thoughts = [t for t in answer]

