import json
from datetime import datetime

# Путь к файлу с данными
filename = "data/shifts.json"

# Загружаем данные
with open(filename, "r", encoding="utf-8") as file:
    shifts = json.load(file)

# Обрабатываем каждую смену
for shift in shifts:
    date_str = shift.get("date", "")

    # Пробуем преобразовать дату из формата ДД.ММ.ГГГГ → ГГГГ-ММ-ДД
    try:
        parsed_date = datetime.strptime(date_str, "%d.%m.%Y")
        shift["date"] = parsed_date.strftime("%Y-%m-%d")
    except ValueError:
        print(f"❗ Пропускаем: {date_str} — не дата (или уже в правильном формате)")

# Сохраняем обратно
with open(filename, "w", encoding="utf-8") as file:
    json.dump(shifts, file, indent=4, ensure_ascii=False)

print("✅ Даты успешно обновлены!")