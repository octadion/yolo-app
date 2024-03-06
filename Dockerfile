FROM python:3.9-slim as python-base

WORKDIR /app

COPY . /app

RUN apt-get update -y && apt-get install -y \
    gcc \
    g++ \
    python3-dev \
    curl \
    libgl1-mesa-glx \
    libglib2.0-dev \
    libpq-dev \
    && pip install --upgrade pip && pip install -r requirements.txt

RUN mkdir -p weights
RUN curl -L https://github.com/octadion/visionllm/raw/main/models/yolo-nas/ckpt_best2.pth -o weights/ckpt_best2.pth

CMD ["python", "app.py"]