from app import db
from sqlalchemy import func

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(64), unique=True)
    completed = db.Column(db.Boolean, default=False)
    image = db.relationship('Image', uselist=False, backref='image_ref')

    def __init__(self,details):
        self.details = details

    def save_task_to_db(details, image_url):
        image = Image(url=image_url)
        task = Todo(details)
        db.session.add(task)
        db.session.commit()
        print("@@@2")
        print(task.id)
        image.todo_id=task.id
        db.session.add(image)
        db.session.commit()

    def get_tasks():
        tasks = Todo.query.select_from(Todo).join(Image, Todo.id==Image.todo_id).all()
        # print(tasks[0].image.url)
        return tasks

    def set_task_as_complete(task_id):
        task = Todo.query.filter_by(id=task_id).first()
        task.completed = True
        db.session.commit()
        

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256), unique=True)
    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'))
        
        

