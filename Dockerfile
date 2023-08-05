FROM python:latest

WORKDIR /app

COPY . .

RUN mkdir models

RUN pip3 install -r requirements.txt && \
    pip3 install torch --index-url https://download.pytorch.org/whl/cpu

RUN gdown 1rYxQ_4dp7kjiIQLCTBs2lG48iAvNsQMQ

RUN mv adpt_finetuned_distilbert_cnn.bin models

EXPOSE 5000

CMD ["python3", "app.py"]