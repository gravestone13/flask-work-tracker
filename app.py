from flask import Flask, render_template, request, redirect, url_for
from logic import calculate_salary, filter_shifts_by_month, summarize_shifts
from storage import save_shift, load_shifts
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    shifts = load_shifts()

    if request.method == 'POST':
        date = request.form['date']
        hours = float(request.form['hours'])
        boxes = int(request.form['boxes'])

        result = calculate_salary(boxes, hours)

        shift = {
            "date": date,
            "hours": hours,
            "boxes": boxes,
            "salary": result["salary"],
            "percent": result["percent"]
        }

        save_shift(shift)
        return redirect(url_for('index'))

    return render_template('index.html', shifts=shifts[::-1])  # последние сверху


@app.route('/report', methods=['GET', 'POST'])
def report():
    summary = None
    filtered = []

    if request.method == 'POST':
        month_str = request.form['month']
        all_shifts = load_shifts()
        filtered = filter_shifts_by_month(all_shifts, month_str)

        if filtered:
            summary = summarize_shifts(filtered)

    return render_template('report.html', summary=summary, shifts=filtered)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
