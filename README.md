- Django used MVT (model - View - Template):
Whenever user send a request to server, it will handle this request by Model, View, Template. Django will check user's URL has correct via mapping this URL with router(urls.py), if this URl is valid then View start to interact with Model and send Template back to user as a respone.

Basic sections of Django:

├── page1/
├── page2/
├── page3/
├── manage.py
├── dir2
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py

- page1, page2, page3: are packages, they can contain 1 or many modules and an additional __init__.py, 1 module is a single Python file
- manage.py: allow interact with Django by many diff ways
- __init__.py: as a constructor, be created to Django know the folder is a package
- settings.py: setting file
- urls.py: router of project
- wsgi.py: have no idea =)), just know this file to serve for deloy progress