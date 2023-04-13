# tasksapp-Flask-SQLAlchemy-Postgresql

first create your virtualenv

`$ python3 -m venv venv`

activate venv

`$ source venv/bin/activate`

then install requirements

`$ pip install -r requirements.txt`

install postgresql, login and create the database

`CREATE DATABASE <yourDBname>;`

create a .env file in the root folder

`$ touch .env`

and add your postgresql url to .env file

>ENV_URL='postgresql+psycopg2://{yourDbUsername}:{yourDbPass}@{yourHost or localhost}/{yourDBname}'

finally the project run with: 

`$ flask --app main run`

open your browser or your http Client in: 

### get all task
`GET http://localhost:5000/task`
### get a task
`GET http://localhost:5000/task/5`
### create a new task
`POST http://localhost:5000/task`
### edit a task
`PUT http://localhost:5000/task/5`
### delete a task
`DELETE http://localhost:5000/task/5`


