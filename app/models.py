from app import db

from werkzeug.security import generate_password_hash,check_password_hash

class Quote(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String,nullable=False,index=True,default='Unknown')
    text = db.Column(db.String,nullable=False)

    def __repr__(self):
        return '<{} {}>'.format(self.id,self.text)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,nullable=False)
    password_hash = db.Column(db.String,nullable=False)
    quota = db.Column(db.Integer,default=0,nullable=False)
    
    def set_password(self,p):
        self.password_hash = generate_password_hash(p)
    
    def check_password(self,p):
        return check_password_hash(self.password_hash,p)

    def __repr__(self):
        return '<{} {}>'.format(self.id,self.username)