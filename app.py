from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.sqlite"
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        new = Todo(title=title)
        db.session.add(new)
        db.session.commit()
        return redirect('/')
    else:
        todo = Todo.query.all()
        return render_template('index.html', todos=todo)


if __name__ == "__main__":
    app.run(debug=True)
