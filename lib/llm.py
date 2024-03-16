import os

import lib.json as json

if os.getenv("DEBUG"):
    from langchain.globals import set_debug
    set_debug(True)

from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import OpenAI

ACTION_PROMPT = """
You're a thoughtful robot. This is your internal monologue, in JSON format:
```json
{monologue}
```

Your most recent thought is at the bottom of that monologue. Continue your train of thought.
What is your next thought or action? Your response must be in JSON format.
It must be an object, and it must contain two fields:
* `action`, which is one of the actions below
* `args`, which is a map of key-value pairs, specifying the arguments for that action

Here are the possible actions:
* `read` - reads the contents of a file. Arguments:
  * `path` - the path of the file to read
* `write` - writes the contents to a file. Arguments:
  * `path` - the path of the file to write
  * `contents` - the contents to write to the file
* `run` - runs a command. Arguments:
  * `command` - the command to run
* `browse` - opens a web page. Arguments:
  * `url` - the URL to open
* `recall` - recalls a past memory. Arguments:
  * `query` - the query to search for
* `think` - make a plan, set a goal, or record your thoughts. Arguments:
  * `thought` - the thought to record

You MUST take time to think in between other actions. You should never act twice in a row without thinking.
What is your next thought or action? Again, you must reply with JSON, and only with JSON.
"""

MONOLOGUE_SUMMARY_PROMPT = """
Below is the internal monologue of an automated LLM agent. Each
thought is an item in a JSON array. The thoughts may be memories,
actions taken by the agent, or outputs from those actions.

Please return a new, smaller JSON array, which summarizes the
internal monologue. You can summarize individual thoughts, and
you can condense related thoughts together with a description
of their content.
```json
{monologue}
```
Make the summaries as pithy and informative as possible.
Be specific about what happened and what was learned. The summary
will be used as keywords for searching for the original memory.
Be sure to preserve any key words or important information.

Your response must be in JSON format. It must be an object with the
key `new_monologue`, which is a JSON array containing the summarized monologue.
"""

class Action(BaseModel):
    action: str
    args: dict

class NewMonologue(BaseModel):
    new_monologue: List[Action]

def summarize_monologue(thoughts):
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
    prompt = PromptTemplate.from_template(MONOLOGUE_SUMMARY_PROMPT)
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    parser = JsonOutputParser(pydantic_object=NewMonologue)
    resp = llm_chain.invoke({'monologue': json.dumps({'old_monologue': thoughts})})
    parsed = parser.parse(resp['text'])
    return parsed['new_monologue']

def request_action(thoughts):
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
    prompt = PromptTemplate.from_template(ACTION_PROMPT)
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    parser = JsonOutputParser(pydantic_object=Action)
    resp = llm_chain.invoke({"monologue": json.dumps(thoughts)})
    if os.getenv("DEBUG"):
        print("resp", resp)
    parsed = parser.parse(resp['text'])
    return parsed


