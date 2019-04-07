# FB Poster Setup

git clone https://github.com/pabin/fbposter

virtualenv -p python3 env

source env/bin/activate

pip install -r requirements.txt

cd fbposter

python manage.py migrate

python manage.py runserver

### Tokens and Page ID Setup
Add Token from --> More --> Add Access Token

Add Facebook Pages from --> More --> Add Facebook Page (Enter Name and Page Id)

### Go to FB POST:
Enter Message or Image URL

Select All Pages to Post on all listed Pages or Select Specific Page to Post



### GET EXTENDED TOKEN FOR TWO MONTH USING FOLLOWING URL
"https://graph.facebook.com/v2.10/oauth/access_token?grant_type=fb_exchange_token&client_id={app_id}&client_secret={app_secret}&fb_exchange_token={short_lived_token}"
