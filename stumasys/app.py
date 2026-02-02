from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import backend

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_in_production'  # Change this in production

# Initialize database
backend.create_table()


@app.route('/')
def index():
    if 'logged_in' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if backend.authenticate(username, password):
            session['logged_in'] = True
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session.get('username'))

#python app.py
@app.route('/students')
def students():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    students_list = backend.view_students()
    return render_template('students.html', students=students_list)


@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        course = request.form.get('course', '').strip()

        if not name or not age.isdigit() or not course:
            flash('Please enter valid data', 'error')
            return render_template('add_student.html')

        result = backend.add_student(name, int(age), course)

        if isinstance(result, str) and result.startswith("Error:"):
            flash(result, 'error')
            return render_template('add_student.html')

        flash(f'Student {name} added successfully!', 'success')
        return redirect(url_for('students'))

    return render_template('add_student.html')


@app.route('/update_student/<int:student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        course = request.form.get('course', '').strip()

        if not name or not age.isdigit() or not course:
            flash('Please enter valid data', 'error')
            return redirect(url_for('students'))

        result = backend.update_student(student_id, name, int(age), course)

        if isinstance(result, str) and result.startswith("Error:"):
            flash(result, 'error')
        else:
            flash('Student updated successfully!', 'success')

        return redirect(url_for('students'))

    return redirect(url_for('students'))


@app.route('/delete_student/<int:student_id>')
def delete_student(student_id):
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    backend.delete_student(student_id)
    flash('Student deleted successfully!', 'success')
    return redirect(url_for('students'))


@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, port=3000)