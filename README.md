### Django used MVT (model - View - Template):

Whenever user send a request to server, it will handle this request by Model, View, Template. Django will check user's URL has correct via mapping this URL with router(urls.py), if this URl is valid then View start to interact with Model and send Template back to user as a respone.

### Basic sections of Django:

    ├── page1/
    ├── page2/
    ├── page3/
    ├── manage.py
    ├── home
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── tests.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── views.py
    │   ├── forms.py
    │   ├── wsgi.py
    │   ├── static/
    │   └── templates/

- page1, page2, page3: are packages, they can contain 1 or many modules and an additional __init__.py, 1 module is a single Python file
- manage.py: allow interact with Django by many diff ways
- __init__.py: as a constructor, be created to Django know the folder is a package
- settings.py: setting file
- urls.py: router of project
- wsgi.py: have no idea =)), just know this file to serve for deloy progress
- tests.py: allow us to write test code for the application. It'll used to test the working of the app
- models.py: are classes that represent data base table
- views.py: takes a web request from urls.py, and returns a web response
- forms.py: define structure of data, able to receive data from from client side to validate... and keep on progress
- static/: contain static files, like: css/js/image/front
- templates/: contain html file

### The project will perform list of client. And from list page, we can click to redirect to detail page to see detailed profile of them.
- Page 1 is list of clients (ClientIndexPage) 
  - Live link: http://127.0.0.1:8000/client/
- Page 2 is detailed of each client in list (ClientPage):
  - Live link: http://127.0.0.1:8000/client/ammad/
  - Properties: first_name - last_name - birth_day - address - intro - avatar


### Setup development environment
- cd python-profile-template/ (main folder)
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver