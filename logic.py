from datetime import datetime
def calculate_salary(boxes, hours):
    norm_per_hour = 190
    full_rate = 38.0
    box_price = 0.2

    total_boxes_norm = norm_per_hour * hours
    percent = boxes / total_boxes_norm
    salary = boxes * box_price

    return {
        "percent": round(percent * 100, 2),
        "salary": round(salary, 2)
    }
def filter_shifts_by_month(shifts, month_str):
    # Оставляем только смены с указанным месяцем: "2025-06"
    return [s for s in shifts if s["date"].startswith(month_str)]

def summarize_shifts(shifts):
    # Суммируем часы, коробки, зарплату
    total_hours = sum(s["hours"] for s in shifts)
    total_boxes = sum(s["boxes"] for s in shifts)
    total_salary = sum(s["salary"] for s in shifts)

    # Считаем процент выполнения нормы (по формуле из calculate_salary)
    norm_per_hour = 190
    norm_total_boxes = norm_per_hour * total_hours
    percent = (total_boxes / norm_total_boxes * 100) if norm_total_boxes > 0 else 0

    return {
        "total_hours": total_hours,
        "total_boxes": total_boxes,
        "total_salary": round(total_salary, 2),
        "average_percent": round(percent, 2)
    }