# Task Master

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-green?logo=flask)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3.40.1-lightgrey?logo=sqlite)](https://sqlite.org/index.html)

**Task Master** is a simple web-based To-Do List application built with Flask and SQLite.  
It allows users to easily add, edit, delete, and view tasks.
 
---

## Features

- Add a new task  
- Edit an existing task  
- Delete a task  
- Display tasks with creation date

---

## Technologies Used

- [Flask](https://flask.palletsprojects.com/) – Python web framework  
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) – ORM for SQLite  
- SQLite – Lightweight built-in database  
- HTML / Jinja2 – Template engine for dynamic web pages

---

## Installation and Usage

1. Clone the repository

```bash
git clone https://github.com/your-username/task-master.git
cd task-master
````

2. Create a virtual environment and activate it

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Install the dependencies

```bash
pip install -r requirements.txt
```

4. Create the database

```bash
python3 create_db.py
```

5. Run the application

```bash
python3 app.py
```

6. Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Project Structure

```
/task-master
│
├── app.py              # Main Flask app
├── create_db.py        # Script to create the database
├── requirements.txt    # List of Python dependencies
├── /templates          # HTML templates (base.html, index.html, update.html)
└── /static             # Static files (CSS, JS, images)
```

---

## Screenshots
<img width="1512" height="525" alt="Screenshot 2025-07-16 at 12 48 14" src="https://github.com/user-attachments/assets/971d8c17-97db-42e6-be04-0f1e185b0bd7" />


