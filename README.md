# Hvordan sette opp

Steg 1: Installer dependencies
Installer python 3.6 og heroku cli.
https://www.python.org/
https://devcenter.heroku.com/articles/heroku-cli

Steg 2: Pull fra git
```
git clone "https://github.com/hallisboe/tihlde"
```

Steg 3:
```
pip install pipenv 
pipenv install 
pipenv shell
```
Da skal alt være satt opp 

Steg 4: Kjør testserver
For mac og linux:
```
heroku local web
```
For windows:
```
python manage.py runserver
```
Steg 5: Push til rep (krever tilgang)
```
git push
git push heroku master 
```