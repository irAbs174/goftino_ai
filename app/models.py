from . import db

class Setting(db.Model):
    __tablename__ = 'Application_Settings'

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Boolean ,nullable=True)

    def __repr__(self):
        return f'<Setting {self.state}>'


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


class Visit(db.Model):
    __tablename__ = 'Visited_Pages'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(250) ,nullable=True)
    date = db.Column(db.String(30) ,nullable=True)
    time_on_page = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<Visit {self.url}>'


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.String(35) ,nullable=True)
    user_id = db.Column(db.String(35) ,nullable=True)
    avatar = db.Column(db.String(250) ,nullable=True)
    name = db.Column(db.String(25) ,nullable=True)
    email = db.Column(db.String(35) ,nullable=True)
    phone = db.Column(db.String(15) ,nullable=True)
    description = db.Column(db.String(50) ,nullable=True)
    tags = db.Column(db.String(35) ,nullable=True)
    ip = db.Column(db.String(35) ,nullable=True)
    location = db.Column(db.String(35) ,nullable=True)
    browser = db.Column(db.String(35) ,nullable=True)
    os = db.Column(db.String(35) ,nullable=True)
    is_banned = db.Column(db.String(35) ,nullable=True)
    last_url = db.Column(db.String(35) ,nullable=True)
    last_visit = db.Column(db.String(35) ,nullable=True)
    first_visit = db.Column(db.String(35) ,nullable=True)
    page_view = db.Column(db.String(35) ,nullable=True)

    def __repr__(self):
        return f'<User {self.name} {self.phone}>'


class Chat(db.Model):
    __tablename__ = 'Chats'

    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.String(35) ,nullable=True)
    user_id = db.Column(db.String(35) ,nullable=True)
    message_count = db.Column(db.Integer, nullable=True)
    chat_status = db.Column(db.String(35) ,nullable=True)
    current_owner = db.Column(db.String(250) ,nullable=True)
    all_operators = db.Column(db.String(250) ,nullable=True)

    def __repr__(self):
        return f'<Chat {self.name} {self.phone}>'

    
class Message(db.Model):
    __tablename__ = 'Messages'

    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.String(35) ,nullable=True)
    sender = db.Column(db.String(35) ,nullable=True)
    date = db.Column(db.String(35) ,nullable=True)
    content = db.Column(db.String(35) ,nullable=True)
    message_type = db.Column(db.String(35) ,nullable=True)
    is_seen = db.Column(db.Boolean, default=False)
    reply_to = db.Column(db.String(35) ,nullable=True)

    def __repr__(self):
        return f'<Message {self.message_id}>'