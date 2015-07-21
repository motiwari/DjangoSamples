To run:

virtualenv ENV

source ENV/bin/activate

cd mysite

pip install -r requirements.txt

python manage.py makemigrations statistics

python manage.py migrate

python manage.py runserver

Then visit 127.0.0.1:8000/statistics in web browser

Can test error handling commenting/uncommenting line 22: print distinct_users[4] in mysite/statistics/migrations/views.py and saving.