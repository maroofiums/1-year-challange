
# Day292
# Student API



A simple **Django Rest Framework (DRF)** project to manage students with full CRUD functionality. This project demonstrates the use of **ViewSets**, **Serializers**, and **Routers** for creating a RESTful API.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

---

## Project Overview

This project provides a RESTful API for managing student data. Each student has:

- Name
- Age
- Email

It allows you to **create, read, update, and delete** students via API requests.

---

## Features

- Create a new student
- Retrieve all students
- Retrieve a single student by ID
- Update student details
- Delete a student
- Fully validated input using Django REST Framework serializers
- Scalable structure with **ViewSets** and **Routers**

---

## Technologies Used

- Python 3.x  
- Django 4.x  
- Django REST Framework  
- SQLite (default DB for Django)  

---

## Project Structure

```

students/
├── manage.py
├── student_api/
│   ├── **init**.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── venv/
└── requirements.txt

````

- **models.py** → Database models (StudentModel)  
- **serializers.py** → DRF serializers for validation and conversion  
- **views.py** → ViewSet for handling CRUD API requests  
- **urls.py** → Router configuration for automatic URL generation  
- **migrations/** → Database migration files  

---

## Installation

1. **Clone the repository**:

```bash
git clone <your-repo-url>
cd students
````

2. **Create virtual environment**:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run migrations**:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Start the server**:

```bash
python manage.py runserver
```

---

## Usage

Once the server is running, you can access the API endpoints at:

```
http://127.0.0.1:8000/students/
```

---

## API Endpoints

| Method | Endpoint        | Description                 |
| ------ | --------------- | --------------------------- |
| GET    | /students/      | List all students           |
| POST   | /students/      | Create a new student        |
| GET    | /students/<id>/ | Retrieve a single student   |
| PUT    | /students/<id>/ | Update a student completely |
| PATCH  | /students/<id>/ | Update a student partially  |
| DELETE | /students/<id>/ | Delete a student            |

**Example POST request:**

```json
{
  "name": "Maroof",
  "age": 17,
  "email": "maroof@example.com"
}
```

---

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add feature'`)
5. Push to the branch (`git push origin feature-name`)
6. Open a Pull Request

---