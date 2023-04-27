# Project Eco2Work

Web application made to register distance done on eco-friendly
way when traveling from home to office and back to home.

General purpose is to implement it in Creadis company.

Goal at some page is to have activities visible in calendar-look table.

# DB models

### `Activity`

Have implemented `__str__` function, which return `{distance} {vehicle} {date}`.

| Variable | Type | Description                      |
| --- |------|----------------------------------|
| id | int  | id                               |
| distance | int  | Distance of the activity in [km] |
| vehicle | char | Name / type of the transport vehicle. Going to make it selectable and have only pre-defined options. |
| date | date | Date of the activity |
| time_create | datetime | Time of creation particular activity. Generated automatically. |
| time_update | datetime | Time of the last update the activity. Generated automatically. |

---

# Useful stuff

Some useful links and hints used during development of this
application.


### Data structures for 'views.py' / 'def show_view(request, year, month):'

    users = {
        'username': <int> sum_of_distances_in_the_month,
        'username': <int> sum_of_distances_in_the_month,
    }

    activities = {
        'username': [
            # [day, distance_km],
            [1, 0],
            [2, 3],
            [3, 2],
            [4, 0],
            ...
        ]
    }

### edit_view

Struggeling with geting activity data from bd based on passed 'username' and 'date'. I think that I might need to change it to passing activity ID.


## Links

| Description | Link                                                        |
| ----------- |-------------------------------------------------------------| 
| Django | https://docs.djangoproject.com/en/4.1/intro/tutorial02/     |
| About MD files | https://www.markdownguide.org/basic-syntax/#paragraphs-1    |
| More about MD files | https://www.markdownguide.org/extended-syntax/#availability |

## Terminal commands

Some commands used to create 'eco2work' and 'e2w_app'

### Commands during first setup / steps of development

Installing Django

    python -m pip install Django    
    python -m django --version
    
Creating project in specific directory /folder/ and checking if it's working.
Don't forget to change directory to folder `eco2work`. Do it by using command
`cd eco2work`.

    django-admin startproject eco2work
    python manage.py runserver

Now we can create app inside project (same directory as before `eco2work`).

    python manage.py startapp e2w_app

    python manage.py makemigrations e2w_app
    python manage.py sqlmigrate e2w_app 0001
    python manage.py migrate

When making changes in `models.py` have to do some commands:

- Change your models (in `models.py`).
- Run `python manage.py makemigrations` to create migrations for those changes
- Run `python manage.py migrate` to apply those changes to the database.

### Creating superuser

    python manage.py createsuperuser

login: `h4sski`
mail:   `h4sski.programming@gmail.com`
password: `H$sskih4sski`

### Other, not used in this project

Virtual environment

    python -m venv .venv

