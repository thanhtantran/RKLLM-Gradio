FROM python:3.12-bookworm
WORKDIR /app
COPY ./requirements.txt ./setup.sh /app/
RUN pip install --upgrade pip && apt update && apt -y install cmake && bash setup.sh && rm -rf /var/cache/apt/archives /var/lib/apt/lists/*
COPY . /app
ENTRYPOINT ["bash", "-c", "source ~/.venv/rkllm-gradio/bin/activate && exec python rkllm_server_gradio.py"]
