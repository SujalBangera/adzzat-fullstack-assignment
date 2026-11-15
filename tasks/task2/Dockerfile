FROM python:3.10-slim

WORKDIR /app

COPY sales.csv .
COPY task.yaml .
COPY test_task2.py .
COPY test.sh .

RUN chmod +x test.sh

CMD ["bash", "test.sh"]
