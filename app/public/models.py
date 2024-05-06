from datetime import datetime

from app import db


class ChatMessage(db.Model):

    __tablename__ = 'chat_messages'
    
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('messages', lazy=True))
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f"ChatMessage('{self.message}', '{self.user.email}', '{self.date}')"

    @staticmethod
    def get_by_id(id):
        return ChatMessage.query.get(id)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()