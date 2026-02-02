# 🎓 Student Management System - Web Application

A modern, professional web-based Student Management System built with Flask and Python.

**Created by: Yogeeta Mishra**

## ✨ Features

- 🔐 **Secure Login System** - Username and password authentication
- 👥 **Student Management** - Add, view, update, and delete student records
- 📊 **Dashboard** - Clean and intuitive interface with quick stats
- 🎨 **Modern UI** - Beautiful, responsive design that works on all devices
- ✅ **Form Validation** - Ensures data integrity with client and server-side validation
- 🗄️ **SQLite Database** - Lightweight and efficient data storage

## 📋 Requirements

- Python 3.7 or higher
- Flask
- SQLite3 (comes with Python)

## 🚀 Installation & Setup

### Step 1: Install Flask

Open your terminal/command prompt in PyCharm and run:
```bash
pip install Flask
```

Or install all requirements at once:
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application

Navigate to the project directory and run:
```bash
python app.py
```

You should see output like:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 3: Access the Application

Open your web browser and go to:
```
http://localhost:5000
```

## 🔑 Default Login Credentials

- **Username:** `admin`
- **Password:** `123`

## 📁 Project Structure
```
student_management_web/
│
├── app.py                  # Main Flask application
├── backend.py              # Database operations and business logic
├── requirements.txt        # Python dependencies
├── README.md              # This file
│
├── templates/             # HTML templates
│   ├── base.html         # Base template with navbar and footer
│   ├── login.html        # Login page
│   ├── dashboard.html    # Main dashboard
│   ├── students.html     # View all students
│   └── add_student.html  # Add new student form
│
├── static/               # Static files (CSS, JS)
│   ├── css/
│   │   └── style.css    # Main stylesheet
│   └── js/
│       └── script.js    # JavaScript for interactivity
│
└── studentsx.db          # SQLite database (created automatically)
```

## 🎯 How to Use

### 1. Login
- Enter username: `admin`
- Enter password: `123`
- Click "Login"

### 2. Dashboard
After login, you'll see the dashboard with four main options:
- **View Students** - See all registered students
- **Add Student** - Register a new student
- **Manage Records** - Update or delete student data
- **Logout** - Exit the system

### 3. Add a Student
- Click "Add Student"
- Fill in the form:
  - Name (only letters and spaces)
  - Age (number between 1-150)
  - Course (only letters and spaces)
- Click "Add Student"

### 4. View Students
- Click "View Students" to see a table of all students
- Each row shows: ID, Name, Age, Course
- Action buttons: Edit and Delete

### 5. Update a Student
- Go to "View Students"
- Click "Edit" button on any student row
- Modify the details in the popup modal
- Click "Update Student"

### 6. Delete a Student
- Go to "View Students"
- Click "Delete" button on any student row
- Confirm the deletion

## 🛠️ Technical Details

### Backend (backend.py)
- SQLite database management
- CRUD operations (Create, Read, Update, Delete)
- Input validation with regex
- Authentication system

### Frontend (Flask + HTML/CSS/JS)
- Flask routes for handling requests
- Jinja2 templates for dynamic content
- Responsive CSS with modern design
- JavaScript for interactive features
- Session management for authentication

### Database Schema
```sql
CREATE TABLE studentsx (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL
)
```

## 🎨 Customization

### Change Colors
Edit `static/css/style.css` and modify the CSS variables:
```css
:root {
    --primary-color: #4a90e2;
    --secondary-color: #6c757d;
    --success-color: #28a745;
    --danger-color: #dc3545;
}
```

### Change Login Credentials
Edit `backend.py`:
```python
VALID_USERNAME = "your_username"
VALID_PASSWORD = "your_password"
```

### Change Port
Edit `app.py`:
```python
app.run(debug=True, port=5000)  # Change 5000 to your desired port
```

## 🔒 Security Notes

⚠️ **For Learning Purposes Only**

This application uses hardcoded credentials and is meant for learning. For production use:
- Implement proper user registration
- Hash passwords using bcrypt or similar
- Use environment variables for secrets
- Add CSRF protection
- Implement proper session security
- Add input sanitization
- Use HTTPS

## 📝 Validation Rules

- **Name**: Only letters and spaces, required
- **Age**: Number between 1-150, required
- **Course**: Only letters and spaces, required

## 🐛 Troubleshooting

### Port Already in Use
If you get an error about port 5000 being in use:
```bash
# Change port in app.py to 5001 or another available port
app.run(debug=True, port=3000)
```

### Module Not Found
Make sure Flask is installed:
```bash
pip install Flask
```

### Database Errors
Delete `studentsx.db` and restart the application to create a fresh database.

## 📚 Learn More

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python SQLite Tutorial](https://docs.python.org/3/library/sqlite3.html)
- [HTML/CSS Basics](https://www.w3schools.com/)

## 🤝 Contributing

Feel free to fork this project and make improvements!

## 📄 License

This project is open source and available for educational purposes.

---

**Developed by Yogeeta Mishra**

Happy Coding! 🚀
