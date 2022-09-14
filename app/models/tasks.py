from . import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadLine = db.Column(db.DateTime(), nullable=False)
    # date = db.Column(db.DateTime(), nullable=False, default= datetime.now())

    def __str__(self) -> str:
        print(self.title)