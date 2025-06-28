from flask import Flask, render_template, request

app = Flask(__name__)

grade_points = {'S': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'F': 0}

@app.route('/', methods=['GET', 'POST'])
def index():
    gpa = None
    if request.method == 'POST':
        credits = list(map(int, request.form.getlist('credit')))
        grades = request.form.getlist('grade')

        total_credits = sum(credits)
        total_points = sum(grade_points.get(grades[i].upper(), 0) * credits[i] for i in range(len(credits)))
        gpa = round(total_points / total_credits, 2) if total_credits else 0

    return render_template('index.html', gpa=gpa)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
