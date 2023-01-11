<p align="center">
<img src="https://github.com/pabin/facebook-poster/blob/master/static/image/logo.png?raw=true" />
</p>

## Project Setup Steps

### Clone Project Repository
```
git clone https://github.com/pabin/facebook-poster.git
cd facebook-poster
```

### Create and Activate Virtual Environment
```
virtualenv -p python3 ../env
source ../env/bin/activate
```

### Install Packages
```
pip install -r requirements.txt
```

### Database Migration with default sqlite3
```
python manage.py migrate
```

### Create Super User
```
python manage.py createsuperuser
```


### Run Project
```
python manage.py runserver
```


> Get Extended token for 2 months with following API
```
https://graph.facebook.com/v2.10/oauth/access_token?grant_type=fb_exchange_token&client_id={app_id}&client_secret={app_secret}&fb_exchange_token={short_lived_token}
```


### `Available Features`

* User Login  <br />
* Facebook page addition <br />
* Facebook Token addtion <br />
* Extend token <br />
* Post status to single facebook page <br />
* Post status to all/multiple facebook pages <br />

## Screenshots
### Login Screen
![ScreenShot](https://github.com/pabin/facebook-poster/blob/master/assets/screenshots/facebook_poster_img1.png?raw=true)

### Home screen
![ScreenShot](https://github.com/pabin/facebook-poster/blob/master/assets/screenshots/facebook_poster_img2.png?raw=true)

### Facebook pages list
![ScreenShot](https://github.com/pabin/facebook-poster/blob/master/assets/screenshots/facebook_poster_img3.png?raw=true)

### Add facebook page Screen
![ScreenShot](https://github.com/pabin/facebook-poster/blob/master/assets/screenshots/facebook_poster_img4.png?raw=true)

### Create extended Token Screen
![ScreenShot](https://github.com/pabin/facebook-poster/blob/master/assets/screenshots/facebook_poster_img5.png?raw=true)

### Status post Screen
![ScreenShot](https://github.com/pabin/facebook-poster/blob/master/assets/screenshots/facebook_poster_img6.png?raw=true)