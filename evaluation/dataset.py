import json
from datasets import Dataset

def load_dataset(path="evaluation/questions.json"):
    with open(path, "r") as f:
        data = json.load(f)

    return Dataset.from_dict({
        "question": [d["question"] for d in data],
        "ground_truth": [d["ground_truth"] for d in data],
    })
