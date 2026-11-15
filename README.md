# Adzzat Labs - Full-Stack Software Engineer Assignment

## Project Overview
Two custom Terminal-Bench-style coding tasks with automated graders, Docker environments, and a Flask web interface.

## Technologies
- Python 3.10
- Flask
- HTML, CSS, JavaScript
- Docker
- Ubuntu (WSL)

## Tasks

### Task 1: Fix Text Normalization in Python
- Type: Language-driven
- Difficulty: Easy
- Grader: 7 automated tests
- Normalize text by converting it to lowercase, removing punctuation, handling whitespace, and replacing spaces with hyphens.

### Task 2: Generate a Sales Summary
- Type: Outcome-driven
- Difficulty: Medium
- Grader: 5 automated tests
- Generate a JSON file containing regional sales totals and the overall total from a CSV file.

## Run the Web Application

Install dependencies:

    pip install -r requirements.txt

Start Flask:

    python app.py

Open http://127.0.0.1:5000/

## API Endpoints
- GET /api/tasks
- GET /api/tasks/1
- GET /api/tasks/2

## Run Task 1

    cd /mnt/f/adzzat-assignment/tasks/task1
    docker build -t adzzat-task1 .
    docker run --rm adzzat-task1

The starter implementation is expected to fail the tests. Apply the reference solution with:

    bash solution.sh

## Run Task 2

    cd /mnt/f/adzzat-assignment/tasks/task2
    docker build -t adzzat-task2 .
    python3 solution.py
    docker run --rm -v "$PWD/summary.json:/app/summary.json:ro" adzzat-task2

The correct reference output passes all five grader tests.

## Testing and Validation
- Task 1: Tested starter code, reference solution, and an incomplete shortcut implementation.
- Task 2: Tested missing output, incorrect totals, and correct output.
- Both tasks packaged and tested using Docker.
- Flask homepage, task detail pages, and API endpoints checked.

## AI Tool Disclosure
ChatGPT assisted with task design, code, tests, Docker configuration, Flask development, debugging, and documentation. The project was manually run and tested, and encountered errors were inspected and corrected.

## Limitations
These are custom Terminal-Bench-style tasks packaged with Docker and YAML instructions. Official Harbor or Terminal-Bench compatibility has not been validated.

No external autonomous agent evaluation is claimed. Validation was performed using reference solutions, automated graders, and manual testing.
