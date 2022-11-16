# Django--GoogleMapsApi
In this app I show how you can use the Google Maps API to: 

- Geocode adress strings 
- Calculate distance and duration between two points 
- Create a map in your Django App 
- Place markers on a Google Map in your Django App

Beware, before using this project you will need to create an API key on Google Cloud Platform and enable the APIs used in the tutorial. 
More info on how to do that can be found on my website: https://cbi-analytics.nl/python-django-google-maps-api-set-up-api-in-google-cloud-platform/

How do you use this code: 

1. Download the ZIP file. 
2. Create your own virtual environment in the project: 
    python -m pip install virtualenv
    python -m virtualenv venv
3. Activate virtual environment 
    venv/scripts/activate 
4. Install requirements 
   pip install -r requirements.txt
5. Run the server
    python manage.py runserver
