# FB Poster Setup

git clone https://github.com/pabin/fbposter

virtualenv -p python3 env

source env/bin/activate

pip install -r requirements.txt

cd fbposter

python3 migrate

python manage.py runserver
