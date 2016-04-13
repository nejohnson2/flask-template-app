# Flask Template App

Make sure you have ```virtualenv``` and ```autoenv``` installed.

## Install locally

```
git clone https://github.com/nejohnson2/flask-template-app.git new-app-name
cd new-app-name

echo "source venv/bin/activate" > .env
echo "export APP_SETTINGS="config.DevelopmentConfig" >> .env

# create virtual environment
virtualenv venv 

# move out of directory and back in to activate the autoenv environment
cd ..
cd new-app-name

# install dependencies
pip install -r requirements.txt

# launch server
python app.py
```

>Note: If the app does not run immediately, it may be because the mongodb has not been configured on heroku.  Continue with the steps below which should solve the problem.

## Deploy to Heroku

```
# create the app
heroku create

# rename app
heroku apps:rename newname

# define environmental variables
heroku config:set APP_SETTINGS="config.StagingConfig"

# add db
heroku addons:create mongolab

echo "export $(heroku config --shell | grep MONGODB_URI)" >> .env
```