from flask import Flask, render_template, request, redirect, url_for
from storage import load_shifts, save_shift, save_shift_list
from logic import calculate_salary, filter_shifts_by_month, summarize_shifts

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    shifts = load_shifts()

    if request.method == 'POST':
        date = request.form['date']
        hours = float(request.form['hours'])
        boxes = int(request.form['boxes'])
        process = request.form['process']

        result = calculate_salary(boxes, hours, process)

        shift = {
            "date": date,
            "hours": hours,
            "boxes": boxes,
            "process": process,
            "salary": result["salary"],
            "percent": result["percent"]
        }

        save_shift(shift)
        return redirect(url_for('index'))

    return render_template('index.html', shifts=shifts[::-1])



@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_shift(index):
    shifts = load_shifts()
    if request.method == "POST":
        shifts[index]["date"] = request.form["date"]
        shifts[index]["hours"] = float(request.form["hours"])
        shifts[index]["boxes"] = int(request.form["boxes"])
        shifts[index]["process"] = request.form["process"]

        result = calculate_salary(shifts[index]["boxes"], shifts[index]["hours"], shifts[index]["process"])
        shifts[index]["salary"] = result["salary"]
        shifts[index]["percent"] = result["percent"]

        save_shift_list(shifts)
        return redirect(url_for('index'))

    return render_template("edit_shift.html", shift=shifts[index], index=index)



@app.route("/delete/<int:index>")
def delete_shift(index):
    shifts = load_shifts()
    if 0 <= index < len(shifts):
        del shifts[index]
        save_shift_list(shifts)
    return redirect(url_for("index"))


@app.route("/report", methods=["GET", "POST"])
def report():
    summary = None
    filtered = []

    if request.method == "POST":
        month_str = request.form["month"]
        all_shifts = load_shifts()
        filtered = filter_shifts_by_month(all_shifts, month_str)

        if filtered:
            summary = summarize_shifts(filtered)

    return render_template("report.html", summary=summary, shifts=filtered)


if __name__ == "__main__":
    app.run(debug=True)
