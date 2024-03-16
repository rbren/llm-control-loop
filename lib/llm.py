import os

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import OpenAI

def sendJSONPrompt(template, input={}):
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
    prompt = PromptTemplate.from_template(template)
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    parser = JsonOutputParser()
    resp = llm_chain.invoke(input)
    parsed = parser.parse(resp['text'])
    return parsed

