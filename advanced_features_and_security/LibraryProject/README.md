# LibraryProject

A Django-based library management system created as part of the ALX Django Learning Lab.

## Description

This is the initial Django project setup for building a library management application. The project demonstrates understanding of Django's core concepts including project structure, settings configuration, URL routing, and the development workflow.

## Technologies Used

- Python 3.x
- Django 4.2.27

## Setup Instructions

### Prerequisites
- Python 3.x installed
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
   git clone https://github.com/nancymwende/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/Introduction_to_Django/LibraryProject
```

2. Install Django:
```bash
   pip install django
```

3. Run database migrations:
```bash
   python3 manage.py migrate
```

4. Start the development server:
```bash
   python3 manage.py runserver
```

5. Open your browser and navigate to:
```
   http://127.0.0.1:8000/
```

### Running the Server
```bash
python3 manage.py runserver
```

The development server will start at `http://127.0.0.1:8000/`

### Creating a New App
```bash
python3 manage.py startapp app_name
```

### Applying Migrations
```bash
python3 manage.py migrate
```

## Learning Objectives

This project covers:
- Installing and configuring Django
- Understanding Django project structure
- Running the Django development server
- Exploring configuration files (settings.py, urls.py)
- Understanding the role of manage.py

## Author

Nancy Mwende

## Repository

GitHub: [Alx_DjangoLearnLab](https://github.com/nancymwende/Alx_DjangoLearnLab)

## License

This project is part of the ALX Django Learning Lab curriculum.