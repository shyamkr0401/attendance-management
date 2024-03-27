from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Dummy data for students
students = ['Shyam', 'Ankit', 'Aastha', 'Shreya']

# Dummy data for attendance
attendance_data = pd.DataFrame(columns=['Date'] + students)

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/save_attendance', methods=['POST'])
def save_attendance():
    date = request.form['date']
    present_students = request.form.getlist('present')

    attendance_data.loc[len(attendance_data)] = [date] + ['Present' if s in present_students else 'Absent' for s in students]

    # Save attendance to Excel
    attendance_data.to_excel('attendance.xlsx', index=False)

    return redirect(url_for('index'))

@app.route('/view_attendance')
def view_attendance():
    return render_template('attendance.html', table=attendance_data.to_html())

if __name__ == '__main__':
    app.run(debug=True)
