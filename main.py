from flask import Flask, request
from sqlalchemy.orm import Session
from database.db import engine
from models.models import Task
from sqlalchemy import select

app = Flask(__name__)

@app.route('/task', methods=['GET',])
def get_all():
    try:
        with Session(engine) as session:
            tasks = session.query(Task).all()
            tasks = [task.to_dict() for task in tasks]
            return tasks
    except Exception as err:
        print(err)
        return {"error": err}

@app.route('/task/<int:task_id>')
def get_one(task_id):
    try:
        with Session(engine) as session:
            stmt = select(Task).where(Task.id == task_id)
            task = session.scalars(stmt).one()
            return task.to_dict()
    except Exception as err:
        print(err)
        return {"error": err}

@app.post('/task')
def create_one():
    try:
        with Session(engine) as session:
            task = Task(title=request.json["title"],
                        description=request.json['description'])
            session.add(task)
            session.commit()
            return task.to_dict()
    except Exception as err:
        print(err)
        return {"error": err}


@app.route('/task/<int:task_id>', methods=['PUT',])
def edit_one(task_id):
    try:
        with Session(engine) as session:
            stmt = select(Task).where(Task.id == task_id)
            task = session.scalars(stmt).one()
            task.title = request.json['title']
            task.description = request.json['description']
            session.commit()
            return task.to_dict()
    except Exception as err:
        print(err)
        return {"error": err}


@app.route('/task/<int:task_id>', methods=['DELETE',])
def delete_one(task_id):
    try:
        with Session(engine) as session:
            task = session.get(Task, task_id)
            session.delete(task)
            session.commit()
            return task.to_dict()
    except Exception as err:
        print(err)
        return {"error": err}


if __name__ == '__main__':
    app.run(debug=True)

