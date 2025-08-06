# Backend-Todo using DRF (pushed in master branch)
This is the backend for the To-Do app built using Django and Django REST Framework (DRF). It provides REST APIs to create, update, delete, and list tasks. This guide will walk you through how to set up and run the backend locally using Visual Studio Code.

Make sure you have the following installed:

- Python 3.10 or higher
- Git
- pip (comes with Python)
- Visual Studio Code

api endpoints urls:-
- GET `/api/tasks/` - list all tasks
- POST `/api/tasks/` - create a new task
- PUT `/api/tasks/<id>/` - update a task
- DELETE `/api/tasks/<id>/` - delete a task

steps:-

1. Clone the Project
git clone https://github.com/shefiinnn/React-Todo

cd todo-backend

2. Set Up a Virtual Environment
   python -m venv venv
   venv\Scripts\activate

3. Install the Requirements
    pip install -r requirements.txt
   If u dont have requirements.txt (pip freeze > requirements.txt)

4.Start the server
python manage.py runserver

5.Allowing Frontend Access (CORS)

To connect this backend with your frontend, install and set up `django-cors-headers`:

Install the package:
pip install django-cors-headers


In your `settings.py`, add it like this:

python
INSTALLED_APPS = [

    'corsheaders',
    'rest_framework,
]
#add this with the existing installed apps

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
  
] #add this with the existing middleware

CORS_ALLOW_ALL_ORIGINS = True

6.Set up the database 
python manage.py makemigrations
python manage.py migrate

7.Start the server 
python manage.py runserver

Bonus tips:-

Activate your virtual environment every time you reopen the terminal.

If migrations fail, delete the db.sqlite3 file and __pycache__ folders, then try again.

If using a custom database (like PostgreSQL), update DATABASES in settings.py.





