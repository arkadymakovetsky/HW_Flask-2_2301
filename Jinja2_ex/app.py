from flask import Flask, abort, render_template, request, jsonify
from pathlib import Path
from werkzeug.exceptions import HTTPException
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

BASE_DIR = Path(__file__).parent

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{BASE_DIR / 'human.db'}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class NameModel(db.Model):
    __tablename__ = "names"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class HumanModel(db.Model):
    __tablename__ = "humans"
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(32), nullable=False)
    surname = db.Column(db.String(32), nullable=False)

    def __init__(self, last_name, name, surname):
        self.last_name = last_name
        self.name = name
        self.surname = surname

    def to_dict(self):
        return {
            "id": self.id,
            "last_name": self.last_name,
            "name": self.name,
            "surname": self.surname
        } 


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(32), nullable=False)
    surname = db.Column(db.String(32), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=True)
    phone = db.Column(db.String(32), nullable=True)

    def __init__(self, login, last_name, name, surname, birth_date, phone):
        self.login = login
        self.last_name = last_name
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.phone = phone

    def to_dict(self):
        return {
            "id": self.id,
            "login": self.login,
            "last_name": self.last_name,
            "name": self.name,
            "surname": self.surname,
            "birth_date": self.birth_date,
            "phone": self.phone
        } 


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/names")
def names():
    names = NameModel.query.all()
    entities = [name.to_dict() for name in names]
    return render_template("names.html", entities=entities)


@app.route("/table")
def table():
    humans = HumanModel.query.all()
    entities = [human.to_dict() for human in humans]
    return render_template("table.html", entities=entities)


@app.route("/users")
def users_list():
    users = UserModel.query.all()
    entities = [user.to_dict() for user in users]    
    return render_template("users_list.html", entities=entities)


@app.route("/users/<login>")
def user_info(login):
    item = UserModel.query.filter_by(login=login).all()
    if item is None:
        abort(404, f"Пользователь с логин={login} не найден")
    return render_template('user_info.html', item=item[0].to_dict())


@app.route("/about")
def about():
    return "О нас"


if __name__ == "__main__":
    app.run(debug=True)

