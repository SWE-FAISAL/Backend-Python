# Build a crud project in Django

A brief description of what this project does and who it's for

Step-1: Creating & activating venv
  Windows:
  ```powershell
    python3 -m venv .venv

    for windows
    python -m venv .venv

    to activate the virtual environment
    source .venv/bin/activate

    for windows
    .venv\Scripts\activate
  ```

Step-2: Installing Dependencies
  ```bash
run package file
    pip install -r requirements.txt  

Make and save all package    
    pip freeze > requirements.txt
  ```

Step-3: Start project
  ```bash
    django-admin startproject projectName
    cd chaiaurdjango
  ```

Step-4: Running application
Windows:
```bash
   python manage.py runserver
```
Step-5: create Migration
Windows:
```bash
   python manage.py makemigrations
   python manage.py migrate
```
Step-6: create superuser
Windows:
```bash
   python manage.py createsuperuser
   example-
   Username: srishti
   Email address: example@gmail.com
   Password:
   Password(again):
```
Step-7: Start app
Windows:
```bash
   python manage.py startapp MiniprojectName
```

