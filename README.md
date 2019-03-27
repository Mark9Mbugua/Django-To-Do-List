# A To Do List
This is a simple application which enables users to keep track of their schedules both in
the long and short term. 

## Getting Started
Clone the repo from GitHub:
    
    git clone: https://github.com/Mark9Mbugua/Django-To-Do-List.git   

Navigate to root folder
    `cd To_do_list`

Create a virtual environment
    `virtualenv venv`

Activate the virtual environment from the root folder
    `source ./venv/Scripts/activate`

Install application dependencies
    `pip install -r requirements.txt`

Install PostgreSQL
  `sudo apt-get install postgresql`

Create a user account postgres and switch over to it
  `sudo -u postgres psql`

Create a database
  `create database to_do_list`

Set up PostgreSQL in `To_do_list/todo/todo/settings.py` as follows:
    `DATABASES = {`
    `'default': {`
        `'ENGINE': 'django.db.backends.postgresql_psycopg2',`
        `'NAME': 'to_do_list',`
        `'USER': 'postgres',`
        `'PASSWORD': 'your_preferred_password',`
        `'HOST': '',`
        `'PORT': '',`
    `}`
`}`

## Starting the server
Navigate to the project folder
    `cd todo`

On the terminal, run `python manage.py runserver`


## Application Features

1. A user can create a list of to-do items
2. A user can mark a to-do item as complete
3. A user can delete all complete to-do items on the list
4. A user can delete all to-do items even the ones that are not complete.

## Built with...

* Python
* Django
* HTML
* CSS
* Bootstrap

### Credits
Copyright (c) [Mark Mbugua](https://github.com/Mark9Mbugua)