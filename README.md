# 📋 Todo List API

A straightforward and lightweight REST API for managing a task to-do list, built with asynchronous Python.

---

## 🛠 Tech Stack

* **Framework:** FastAPI
* **ORM:** SQLAlchemy 2.0 (Async)
* **Database:** SQLite
* **Data Validation:** Pydantic

---

## 📌 Features

* ✅ **Create Task:** Add new entries to your to-do list.
* ✅ **Get All Tasks:** Retrieve a full list of existing tasks.
* ✅ **Get Task by ID:** Fetch detailed information for a specific task.
* ✅ **Mark as Completed:** Update task status dynamically.
* ✅ **Delete Task:** Remove tasks permanently from the database.

---

## 🚀 Installation & Setup

1. **Clone the repository and navigate to the project directory:**
   ```bash
   git clone [https://github.com/Ashkelon1337/todo_list_API.git](https://github.com/Ashkelon1337/todo_list_API.git)
   cd todo_list_API
   ```
2. **Create and activate a virtual environment:**
	```bash
   # On Windows
	python -m venv venv
	venv\Scripts\activate
	
	# On Linux/macOS
	python3 -m venv venv
	source venv/bin/activate
 	```
 3. **Install the required packages:**
	```bash pip install -r requirements.txt```
4. **Start the FastAPI development server:**
	```bash python main.py```
Explore the API Interactively:
Once the server is running, open your browser and navigate to the Swagger UI documentation to test the endpoints:
👉 http://127.0.0.1:8000/docs
