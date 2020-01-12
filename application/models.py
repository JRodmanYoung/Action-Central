from application import app, db

class User(db.Model):
    user_ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    user_email = db.Column(db.String(256), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80))
    assignment_ID = db.Column(db.Integer, db.ForeignKey('user.user_ID'))
    
    secret_santa = db.relationship(
        'User',
        primaryjoin="User.assignment_ID == User.user_ID")
    