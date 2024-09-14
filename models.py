from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Faq(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer
        }
