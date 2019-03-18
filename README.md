# FB Poster Setup

git clone https://github.com/pabin/fbposter

virtualenv -p python3 env

source env/bin/activate

pip install -r requirements.txt

cd fbposter

python3 migrate

### Tokens and Page ID Setup
Create tokens.py file inside home app

create token dictionary as below:

token = {
  "access_token" : "<Access Token Created from Facebook App at
   https://developers.facebook.com/"
}

Create page_id dictionary as below:

page_id = {
  "pid_page1": "<Facebook Page1 ID>",
  "pid_page2": "<Facebook Page2 ID>",
}

python manage.py runserver
