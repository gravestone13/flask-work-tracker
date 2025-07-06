def calculate_salary(boxes, hours, process="P01"):
    norms = {
        "P01": 190,
        "P03": 287,
        "P21": 175,
        "P16": 250
    }

    if hours <= 0 or process not in norms:
        return {"salary": 0, "percent": 0}

    norm = norms[process]
    boxes_per_hour = boxes / hours
    percent = round((boxes_per_hour / norm) * 100, 2)

    if percent < 100:
        salary = 28 * hours
    else:
        rate_per_box = 38 / norm
        salary = rate_per_box * boxes

    return {"salary": round(salary, 2), "percent": percent}



def filter_shifts_by_month(shifts, month_str):
    return [s for s in shifts if s["date"].startswith(month_str)]

def summarize_shifts(shifts):
    total_hours = sum(s["hours"] for s in shifts)
    total_boxes = sum(s["boxes"] for s in shifts)
    total_salary = sum(s["salary"] for s in shifts)
    average_percent = round(sum(s["percent"] for s in shifts) / len(shifts), 2) if shifts else 0
    return {
        "total_hours": total_hours,
        "total_boxes": total_boxes,
        "total_salary": round(total_salary, 2),
        "average_percent": average_percent
    }
