import csv
import json
from collections import defaultdict

totals = defaultdict(int)

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        region = row["region"]
        amount = int(row["amount"])
        totals[region] += amount

summary = {
    "regions": dict(sorted(totals.items())),
    "overall_total": sum(totals.values())
}

with open("summary.json", "w") as file:
    json.dump(summary, file, indent=4)

print("Sales summary generated successfully.")
