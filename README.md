# Employee Management API

A RESTful API built with Flask for managing employees with JWT authentication. Each user only sees their own employee data.

---

## Features

- User registration and login
- JWT-protected endpoints
- Employee CRUD (create, read, update, delete)
- User-scoped data — employees belong to the authenticated user
- SQLite database

---

## Tech Stack

- Python / Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- SQLite

---

## Project Structure

```
employee2_api/
├── app.py
├── extensions.py
├── models.py
├── routes/
│   ├── auth.py
│   ├── employees.py
│   └── salaries.py
├── instance/
│   └── database.db
├── requirements.txt
└── README.md
```

---

## Setup

```bash
# Clone the repo
git clone https://github.com/saifan340/employee-management-api.git
cd employee-management-api

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

Server runs at `http://127.0.0.1:5000`

---

## Authentication

This API uses JWT. After login, include the token in all protected requests:

```
Authorization: Bearer <your_token>
```

---

## API Endpoints

### Auth

| Method | Endpoint    | Description              |
|--------|-------------|--------------------------|
| POST   | `/register` | Register a new user      |
| POST   | `/login`    | Login and receive a JWT  |

**Register**
```json
POST /register
{
  "username": "saifan",
  "password": "password123"
}
```

**Login**
```json
POST /login
{
  "username": "saifan",
  "password": "password123"
}
```
Response:
```json
{
  "message": "Login successful",
  "token": "eyJ..."
}
```

---

### Employees (Protected)

All endpoints require `Authorization: Bearer <token>`. Employees are scoped to the authenticated user.

| Method | Endpoint              | Description          |
|--------|-----------------------|----------------------|
| GET    | `/employees`          | Get all employees    |
| POST   | `/employees`          | Add a new employee   |
| PUT    | `/employees/<id>`     | Update an employee   |
| DELETE | `/employees/<id>`     | Delete an employee   |

**Add Employee**
```json
POST /employees
{
  "name": "Ali",
  "position": "Backend Developer"
}
```

**Update Employee**
```json
PUT /employees/1
{
  "name": "Ali Hassan",
  "position": "Senior Developer"
}
```

---

## Author

GitHub: [saifan340](https://github.com/saifan340)
