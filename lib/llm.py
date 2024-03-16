import os

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import OpenAI

def sendJSONPrompt(template, input={}):
    print("make llm")
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
    print("make prompt")
    prompt = PromptTemplate.from_template(template)
    print("make chain")
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    print("make parser")
    parser = JsonOutputParser()
    print("get resp")
    resp = llm_chain.invoke(input)
    print("resp", resp)
    parsed = parser.parse(resp['text'])
    print("parsed", parsed)
    return parsed

