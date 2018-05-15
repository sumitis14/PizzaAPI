import datetime
import time
from db import db
class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    timeOpen = db.Column(db.Integer)
    timeClose = db.Column(db.Integer)


    def __init__(self, name, timeOpen, timeClose,eid=0):
        self.name = name
        self.timeOpen = timeOpen
        self.timeClose = timeClose
        if eid ==0:
            self.id = id
        else:
            self.id = eid

    def json(self):
        self.timeOpen *=3600
        self.timeClose *=3600
        return {'id': self.id, 'name' : self.name,
                'time opens at' : time.strftime("%H:%M:%S", time.gmtime(self.timeOpen)),
                'time closes at' : time.strftime("%H:%M:%S", time.gmtime(self.timeClose))}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first() #SELECT * FROM WHERE name=name

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()  # SELECT * FROM WHERE name=name

    # @classmethod
    # def find_id_by_name(cls, name):
    #     print(cls.query.filter_by(name=name).first())
    #     return cls.query.filter_by(name=name).first()  # SELECT * FROM WHERE name=name


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


