from python:3.12-bookworm

ENV OPENAI_API_KEY=""
ENV OPENAI_MODEL="gpt-4-0125-preview"

COPY requirements.txt ./requirements.txt
RUN python -m pip install -r requirements.txt

COPY lib ./lib
COPY main.py ./main.py

