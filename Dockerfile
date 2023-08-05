FROM python:3.11-slim-bookworm

WORKDIR /app

COPY . .

RUN mkdir -p models || true

RUN pip3 install -r requirements.txt && \
    pip3 install torch --index-url https://download.pytorch.org/whl/cpu

RUN gdown 1rYxQ_4dp7kjiIQLCTBs2lG48iAvNsQMQ

RUN mv adpt_finetuned_distilbert_cnn.bin models

EXPOSE 5000

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]