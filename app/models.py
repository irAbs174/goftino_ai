from . import db

class Operator(db.Model):
    __tablename__ = 'Operators'
    
    id = db.Column(db.Integer, primary_key=True)
    operator_id = db.Column(db.String(30) ,nullable=True)
    avatar = db.Column(db.String(80) ,nullable=True)
    name = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(20), nullable=True)
    is_online = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Operator {self.name}>'
