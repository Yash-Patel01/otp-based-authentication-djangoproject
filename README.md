# djangoproject

Follow the given instructions to run project.

 - Create virtual environment
    `python -m venv env`
    
 - Activate virtual environment
	 `env\Scripts\activate`
	 
 - Go to project directory and install requirements.txt
	 `pip install -r requirements.txt`
	 
 - Create MySQL 'djangodatabase' database and change configuration of
   database in settings.py file add USER, PASSWORD, HOST and PORT
`DATABASES = { 'default': { 'ENGINE': 'django.db.backends.mysql', 'NAME': 'djangodatabase', 'USER': '', 'PASSWORD': '', 'HOST': '', 'PORT': '',} }`

 - Run migration commands
    `python manage.py makemigrations`
    `python manage.py migrate`

 - Run project on development server.
	`python manage.py runserver` 