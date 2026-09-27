# Django Masterclass

A collection of Django projects built while following the **Django Masterclass: Build 9 Real-World Django Projects** course.

The course focuses on building practical Django applications, working with databases and authentication, and developing REST APIs with Django REST Framework.

## 🛠️ Tech Stack

### Backend

- **Python**
- **Django 6**
- **Django REST Framework**
- **django-filter**
- **drf-spectacular**

### Database

- **PostgreSQL**
- **Django ORM**
- **psycopg**

### Authentication & Security

- **Django Authentication**
- **DRF Token Authentication**
- **JWT Authentication**
- **Django Permissions**

### Supporting Libraries & Tools

- **Pillow**
- **python-dotenv**
- **Ruff**
- **djLint**
- **Insomnia**

## 📁 Repository Structure

Each project from the course is kept in its own directory.

```text
django-projects/
│
├── project-1/
├── project-2/
├── project-3/
├── ...
│
├── requirements.txt
└── README.md
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd django-projects
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file when required by a project.

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=your-database
DB_USER=your-user
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

## 📚 About the Course

The course uses multiple hands-on projects to explore Django and its ecosystem, progressing from core Django development to building REST APIs with Django REST Framework.

This repository contains the implementations and code developed throughout the course.
