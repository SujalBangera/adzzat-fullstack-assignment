FROM python:3.10-slim

WORKDIR /app

# Copy the original starter program
COPY tag_utils.py .

# Copy task instructions
COPY task.yaml .

# Copy automated grader tests
COPY test_normalize.py .

# Copy test runner
COPY test.sh .

RUN chmod +x test.sh

CMD ["bash", "test.sh"]