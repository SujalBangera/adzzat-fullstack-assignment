
from flask import Flask, jsonify, render_template

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Fix Text Normalization in Python",
        "type": "Language-driven",
        "difficulty": "Easy",
        "difficulty_note": "Requires basic Python string manipulation.",
        "environment": "Python 3.10",
        "statement": """Fix the normalize_tag() function in tag_utils.py.

Requirements:
1. Convert all characters to lowercase.
2. Remove leading and trailing whitespace.
3. Remove punctuation characters.
4. Replace one or more spaces between words with a single hyphen.
5. Return the normalized string.

Examples:
Python Programming -> python-programming
Hello World -> hello-world
Web Development! -> web-development"""
    },
    {
        "id": 2,
        "title": "Generate a Sales Summary",
        "type": "Outcome-driven",
        "difficulty": "Medium",
        "difficulty_note": "Requires interpreting tabular data and producing an accurate summary.",
        "environment": "Python 3.10",
        "statement": """You are given a file named sales.csv containing sales records.

Produce a file named summary.json that reports:
- The total sales amount for each region.
- The overall total sales amount.

Regional entries must be ordered alphabetically by region.
The output must contain valid JSON and the calculated totals must be accurate."""
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/tasks")
def get_tasks():
    return jsonify(tasks)


@app.route("/api/tasks/<int:task_id>")
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task)


@app.route("/tasks/<int:task_id>")
def task_detail(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)

    if task is None:
        return "Task not found", 404

    return render_template("task.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)
