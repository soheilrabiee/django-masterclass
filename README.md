# Django Masterclass Projects

A collection of practical Django projects developed while completing the **Django Masterclass: Build 9 Real World Django Projects**.

The repository focuses on practical **Python/Django backend development**, covering Django fundamentals, database-driven applications, authentication, and REST API development with Django REST Framework.

## 🛠️ Tech Stack

- **Python**
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **SQLite**
- **Git**
- **Insomnia**

## 📚 Topics Covered

### Django

- Django project and application structure
- MVT architecture
- URL routing and namespacing
- Function-based views
- Class-based views
- Templates and template inheritance
- Static and media files
- Forms and ModelForms
- CRUD operations
- Django Admin

### Database & ORM

- Django models and relationships
- Database migrations
- Django ORM and QuerySets
- CRUD database operations
- ForeignKey and OneToOne relationships
- Model validation
- PostgreSQL integration
- Query optimization and efficient database access
- Soft-delete patterns

### Authentication & Authorization

- User registration and authentication
- Login and logout
- User-specific data
- Authentication and authorization
- Permissions and access control
- Token-based authentication
- JWT authentication

### Backend Development

- Class-based views
- Custom middleware
- Request/response lifecycle
- Pagination
- Search and filtering
- Logging
- Validation and error handling
- Caching
- Reusable backend patterns

### REST API Development

Hands-on development with Django REST Framework, including:

- Serializers
- Function-based API views
- `APIView`
- Generic API views
- `ListCreateAPIView`
- `RetrieveUpdateDestroyAPIView`
- `ModelViewSet`
- Routers
- RESTful CRUD endpoints
- API authentication
- API permissions
- JWT authentication

## 📂 Projects

### `mysite`

The first project in the Masterclass repository, covering the core Django development workflow and progressing into backend API development.

The project includes practical implementations of:

- Django project and app architecture
- Models, migrations, and Django ORM
- Database relationships
- Forms and validation
- User authentication
- Permissions and authorization
- Function-based and class-based views
- Custom middleware
- Pagination
- Search and filtering
- Application logging
- Soft deletion
- PostgreSQL
- Django REST Framework
- RESTful CRUD APIs
- Token and JWT authentication
- API permissions

Additional projects from the Masterclass will be added to this repository as they are completed.

## 📁 Repository Structure

```text
django-projects/
│
├── mysite/
│   ├── manage.py
│   ├── <django-project>/
│   └── <django-apps>/
│
├── requirements.txt
├── README.md
└── .gitignore
```

Each Masterclass project will be maintained within its own directory while sharing the repository's overall development environment.

## 🚀 Getting Started

### Clone the Repository

```bash
git clone <repository-url>
cd django-projects
```

### Create a Virtual Environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python mysite/manage.py migrate
```

### Run the Development Server

```bash
python mysite/manage.py runserver
```

The development server will be available at:

```text
http://127.0.0.1:8000/
```

> Some projects may require additional configuration, such as PostgreSQL credentials or environment variables.

## 📦 Dependencies

Python dependencies are listed in [`requirements.txt`](requirements.txt).

Install them with:

```bash
pip install -r requirements.txt
```

## 🎯 Focus

The repository emphasizes practical backend development with Python and Django, including:

- Designing Django applications and data models
- Working with the Django ORM
- PostgreSQL and database migrations
- Building RESTful APIs
- Authentication and authorization
- API permissions and access control
- Validation and error handling
- Pagination and filtering
- Database query optimization
- Application logging
- Writing maintainable backend code

## 🎓 Course

**Django Masterclass: Build 9 Real World Django Projects**  
by **Ashutosh Pawar**

[View the course on Udemy](https://www.udemy.com/course/django-course/)
