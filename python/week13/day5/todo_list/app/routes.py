from app import app, db
from app.models import Todo
from flask import redirect, render_template
from app.forms import AddTodo

@app.route('/', methods=['GET', 'POST'])
def home():
    formi = AddTodo()
    if formi.validate_on_submit():
        details = formi.details.data
        image = formi.image.data
        print(details)
        Todo.save_task_to_db(details, image)
        return redirect('http://127.0.0.1:5000/')

    tasks = Todo.get_tasks()
    return render_template('index.html', form=formi, tasks=tasks)


@app.route('/complete/<task_id>',)
def complete(task_id):
    Todo.set_task_as_complete(task_id)
    return redirect('http://127.0.0.1:5000/')