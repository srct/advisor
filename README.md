create virtualenv

pip install -r requirements.txt

python manage.py migrate --all

python manage.py syncdb

python manage.py runserver
