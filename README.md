# Library Management System:
This project is a software application developed for a library management system. This system provides library administrators and users with the ability to manage and track library operations.

#Features:
```
Book Management: Add new books, edit and remove existing books.
User Management: Add, edit, and delete users.
```

# USAGE

```
$ git clone https://github.com/hamidbeyli005/library-management-system
$ cd library-management-system
$ docker-compose build
# create admin user, fill in the admin user's password
$ docker-compose run web bash -c "python library_manager/manage.py makemigrations && python library_manager/manage.py migrate && python library_manager/manage.py createsuperuser --email admin@example.com --username admin"
$ docker-compose up

Go to http://localhost:8000/admin or http://localhost:8000/api/books
Log in with admin user:
+ Username: admin
+ Password: <the password you filled in at the step creating admin user>
```

## Migrate DB and create super user (once time set up)
```
$ docker-compose run web bash -c "python library_manager/manage.py makemigrations && python library_manager/manage.py migrate && python library_manager/manage.py createsuperuser --email admin@example.com --username admin"
Password: password123
Password (again): password123
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

## Migrate DB for rest_example module
```
$ docker-compose run web bash -c "python library_manager/manage.py makemigrations  && python library_manager/manage.py migrate"
```

## Start server

```
$ docker-compose up
```

Start server in detached mode:

```
$ docker-compose up -d
```

## API location

* Go to `http://localhost:8000` to browse public RESTful APIs
* Django Admin: `http://localhost:8000/admin`
* Django Api: `http://localhost:8000/api`
