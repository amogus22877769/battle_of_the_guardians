from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Column, Integer, String, desc

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqldb://amogus22877769_admin:Lion007legend@localhost:3306/amogus22877769_battle_of_the_guardians_leaderboard'
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db.init_app(app)

class User(db.Model):
    username = Column(String(30), primary_key=True)
    password = Column(String(30))
    score = Column(Integer, default=0)

    def __repr__(self):
        return f'username: {self.username}, password: {self.password}, score: {self.score}'

with app.app_context():
    db.create_all()

@app.post("/authorization")
def authorization_handler():
    if db.session.execute(db.select(User).where(
            (User.username == request.form['username']) & (User.password == request.form['password']))).first():
        return {'result': 'success'}
    if not db.session.execute(db.select(User).where(User.username == request.form['username'])).first():
        user = User(
            username=request.form['username'],
            password=request.form['password'],
        )
        db.session.add(user)
        db.session.commit()
        return {'result': 'success'}
    return {'result': 'fail'}



@app.get('/leaderboard')
def leaderboard_handler():
    return [[username, score]
            for username, score in db.session.execute(db.select(User.username, User.score).order_by(desc(User.score)))]

@app.post('/score')
def handle_score():
    print(f'new_score: {request.form['score']}')
    if not db.session.execute(db.select(User).where((User.username == request.form['username']) & (User.password == request.form['password']))).first():
        return {'result': 'fail'}
    user = db.session.execute(db.select(User).where(User.username == request.form['username'])).first()[0]
    user.score = request.form['score']
    db.session.commit()
    return {'result': 'success'}


@app.route('/')
def hello():
	return """<p>Hello</p>"""

if __name__ == "__main__":
  app.run()