import os
import json
import requests

class Event:
    def __init__(self, event_type, args):
        self.event_type = event_type
        self.args = args

    def to_dict(self):
        return {
            'event_type': self.event_type,
            'args': self.args
        }

    def run(self, agent):
        if self.event_type == 'run':
            cmd = self.args['command']
            return os.popen(cmd).read()
        elif self.event_type == 'browse':
            url = self.args['url']
            response = requests.get(url)
            return response.text
        elif self.event_type == 'read':
            file_path = self.args['path']
            with open(file_path, 'r') as file:
                return file.read()
        elif self.event_type == 'write':
            with open(self.args['path'], 'w') as file:
                file.write(self.args['contents'])
            return ""
        elif self.event_type == 'recall':
            return agent.memory.search(self.args['query'])
        elif self.event_type == 'think':
            agent.add_thought(self.args['thought'])
            return self.content
        elif self.event_type == 'output':
            return self.args['output']
        else:
            raise ValueError('Invalid action type')




