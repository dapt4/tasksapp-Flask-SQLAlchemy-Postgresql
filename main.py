from flask import Flask, request
from sqlalchemy.orm import Session
from database.db import engine
from models.models import Task
from sqlalchemy import select

app = Flask(__name__)

@app.route('/', methods=['GET',])
def getAll():
    try:
        with Session(engine) as session:
            tasks = session.query(Task).all()
            return tasks
    except Exception as err:
        print(err)

@app.route('/task/<int:id>')
def getOne(id):
    try:
        with Session(engine) as session:
            stmt = select(Task).where(Task.id == id)
            task = session.scalars(stmt).one()
            return task.to_dict()
    except Exception as err:
        print(err)
        return {"error": err}

@app.post('/task')
def createOne():
    try:
        with Session(engine) as session:
            task = Task(title=request.json["title"],
                        description=request.json['description'])
            session.add(task)
            session.commit()
            return task.to_dict()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    app.run(debug=True)

