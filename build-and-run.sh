docker build -t control-loop .
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -v /workspace:./workspace control-loop python main.py
