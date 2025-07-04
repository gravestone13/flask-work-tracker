import json
import os

def load_shifts(filename="data/shifts.json"):
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        return json.load(file)

def save_shift(shift, filename="data/shifts.json"):
    shifts = load_shifts(filename)
    shifts.append(shift)

    with open(filename, "w") as file:
        json.dump(shifts, file, indent=4)