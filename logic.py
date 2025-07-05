def calculate_salary(boxes, hours):
    boxes_per_hour = boxes / hours if hours > 0 else 0
    percent = round((boxes_per_hour / 190) * 100, 2)

    if percent < 100:
        salary = 28 * hours
    else:
        base_salary = 38 * hours
        piecework_salary = 0.2 * boxes
        salary = max(base_salary, piecework_salary)

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
