from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Example(db.Model):
    __tablename__ = 'exampless'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(16), unique=True)

    def __repr__(self):
        return "<Example: {0}>".format(self.name)
