from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def get_user(user_id):
    return User.query.get(user_id)
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    breakfast_insulin = db.Column(db.String(5), nullable=False)
    breakfast_carb = db.Column(db.String(5), nullable=False)
    lunch_insulin = db.Column(db.String(5), nullable=False)
    lunch_carb = db.Column(db.String(5), nullable=False)
    dinner_insulin = db.Column(db.String(5), nullable=False)
    dinner_carb = db.Column(db.String(5), nullable=False)
    correction_150_199 = db.Column(db.String(5), nullable=False)
    correction_200_249 = db.Column(db.String(5), nullable=False)
    correction_250_299 = db.Column(db.String(5), nullable=False)
    correction_300_349 = db.Column(db.String(5), nullable=False)
    correction_350_399 = db.Column(db.String(5), nullable=False)
    correction_400 = db.Column(db.String(5), nullable=False)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()
        

    def __repr__(self):
        return f"<User|{self.username}>"

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def save(self):
        db.session.commit()
