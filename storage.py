import json
import os

FILE = "shifts.json"

def load_shifts():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_shift(shift):
    shifts = load_shifts()
    shifts.append(shift)
    save_shift_list(shifts)

def save_shift_list(shifts):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(shifts, f, ensure_ascii=False, indent=4)