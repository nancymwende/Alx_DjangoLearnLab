# Social Media API

This project is a Django REST API for a social media platform.

## Project Structure

Alx_DjangoLearnLab/
│
└── social_media_api/
    ├── manage.py
    ├── social_media_api/
    └── accounts/

## Setup Instructions

1. Clone the repository

git clone https://github.com/yourusername/Alx_DjangoLearnLab.git

2. Navigate to the project

cd social_media_api

3. Install dependencies

pip install django djangorestframework

4. Run migrations

python manage.py makemigrations
python manage.py migrate

5. Run the development server

python manage.py runserver

## API Endpoints

Register  
POST /api/accounts/register/

Login  
POST /api/accounts/login/

Profile  
GET /api/accounts/profile/

## Authentication

Token-based authentication using Django REST Framework.