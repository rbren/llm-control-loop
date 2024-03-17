import os
import json
import requests
import subprocess

class Event:
    def __init__(self, action, args):
        self.action = action
        self.args = args

    def __str__(self):
        return self.action + " " + str(self.args)

    def to_dict(self):
        return {
            'action': self.action,
            'args': self.args
        }

    def is_runnable(self):
        return self.action in ['run', 'browse', 'read', 'write', 'recall']

    def run(self, memory):
        if self.action == 'run':
            cmd = self.args['command']
            result = subprocess.run(["/bin/bash", "-c", cmd], capture_output=True, text=True)
            output = result.stdout + result.stderr
            exit_code = result.returncode
            if exit_code != 0:
                raise ValueError('Command failed with exit code ' + str(exit_code) + ': ' + output)
            return output
        elif self.action == 'browse':
            url = self.args['url']
            response = requests.get(url)
            return response.text
        elif self.action == 'read':
            file_path = self.args['path']
            with open(file_path, 'r') as file:
                return file.read()
        elif self.action == 'write':
            with open(self.args['path'], 'w') as file:
                file.write(self.args['contents'])
            return ""
        elif self.action == 'recall':
            return memory.search(self.args['query'])
        else:
            raise ValueError('Invalid action type')
