from . import db
from datetime import datetime
from sqlalchemy.event import listen
class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadLine = db.Column(db.DateTime(), nullable=False)
    date = db.Column(db.DateTime(), nullable=False, default= datetime.now())

    def __str__(self) -> str:
        print(self.title)

    def serialize(self):
        return {
            'id':self.id,
            'title':self.title,
            'description':self.description,
            'deadLine':self.deadLine,
            'date':self.date
        }

def insertar_registros(*args, **kwargs):
    db.session.add(
        Task(title='titulo 1', description="descripcion 1", deadLine ='2022-09-24 12:00:00')
    )
    db.session.add(
        Task(title='titulo 2', description="descripcion 2", deadLine ='2022-06-28 18:00:00')
    )

    db.session.commit()

listen(Task.__table__, "after_create", insertar_registros)