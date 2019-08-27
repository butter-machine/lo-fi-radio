heroku apps:destroy lo-fi-radio --confirm lo-fi-radio
heroku create lo-fi-radio
heroku git:remote -a lo-fi-radio
git push heroku master && heroku logs --tail