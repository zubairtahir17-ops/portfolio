# Task 5: Django Project vs App

## Objective

To understand the difference between a Django Project and a Django App, create a Django project, create an application inside it, register the application, and run the development server.

## 1. Creating a Virtual Environment

Command:

`python -m venv venv`

Purpose:

Creates an isolated Python virtual environment for the Django project.

## 2. Activating Virtual Environment

Command:

`.\venv\Scripts\Activate.ps1`

Purpose:

Activates the virtual environment in Windows PowerShell.

## 3. Installing Django

Command:

`python -m pip install django`

Purpose:

Installs Django and its required dependencies into the active virtual environment.

## 4. Checking Django Version

Command:

`python -m django --version`

Purpose:

Displays the installed Django version.

## 5. Creating Django Project

Command:

`django-admin startproject portfolio .`

Purpose:

Creates a Django project named portfolio in the current directory.

The dot (.) ensures that the project files are created directly in the current directory rather than inside another nested folder.

## 6. Understanding Project Structure

The Django project contains:

- manage.py: Command-line utility for managing the project.
- settings.py: Contains project configuration.
- urls.py: Defines the main URL routing configuration.
- asgi.py: ASGI application entry point.
- wsgi.py: WSGI application entry point.
- **init**.py: Identifies the directory as a Python package.

## 7. Creating Django App

Command:

`python manage.py startapp pages`

Purpose:

Creates a Django application named pages inside the project.

## 8. Understanding App Structure

The Django app contains:

- admin.py: Used to register models with Django Admin.
- apps.py: Contains application configuration.
- models.py: Defines database models.
- tests.py: Contains automated tests.
- views.py: Handles requests and returns responses.
- migrations/: Stores database migration files.

## 9. Registering the App

File:

`portfolio/settings.py`

Added the following entry to INSTALLED_APPS:

`'pages',`

Purpose:

Registers the pages application so Django recognizes it as part of the project.

## 10. Running Django Development Server

Command:

`python manage.py runserver`

Purpose:

Starts Django's local development server.

Default address:

`http://127.0.0.1:8000/`

## 11. Stopping the Development Server

Shortcut:

`CTRL + C`

Purpose:

Stops the running development server.

## 12. Generating requirements.txt

Command:

`python -m pip freeze > requirements.txt`

Purpose:

Records installed Python packages and their versions for dependency management.

## 13. Git Ignore Configuration

File:

`.gitignore`

Purpose:

Prevents virtual environments, Python cache files, local database files, and other unnecessary files from being uploaded to GitHub.

## Outcome

Successfully created a Django project named portfolio, created an application named pages, registered the application in settings.py, and ran the Django development server.
