from app import db
from sqlalchemy import func

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(64), unique=True)
    completed = db.Column(db.Boolean, default=False)

    def __init__(self,details):
        self.details = details

    def save_task_to_db(details):
        task = Todo(details)
        db.session.add(task)
        db.session.commit()

    def get_tasks():
        tasks = Todo.query.all()
        return tasks

    def set_task_as_complete(task_id):
        task = Todo.query.filter_by(id=task_id).first()
        task.completed = True
        db.session.commit()
        

        
        

