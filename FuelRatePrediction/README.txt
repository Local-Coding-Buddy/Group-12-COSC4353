Thomas Carroll
Emmanuel Hernandez
Jaffar, Abdulkadir

If you are trying to run the code then you will need to install Django and crispy then run the server and connect to 
the IP on a browser. Here is how to do that
1: install:
pip install django
pip install crispy-forms-gds
pip install django-readonly-field

For code coverage:
pip install pytest
pip install pytest-django
pip install pytest-cov

2: run the server: 
From the FuelRatePrediciton: 
python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 26, 2021 - 11:09:48
Django version 3.1.5, using settings 'FuelRatePrediction.settings'
Starting development server at http://127.0.0.1:8000/

3: Paste the http://127.0.0.1:8000/ ip into a browser Url to look at our website

4. to run the code coverage go to the directory Group-12-COSC4353\FuelRatePrediction and run the command pytest --cov=.