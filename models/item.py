import uuid
from db import db
class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    timeOpen = db.Column(db.String(80))
    timeClose = db.Column(db.String(80))


    def __init__(self, name, timeOpen, timeClose,eid=0):

        self.name = name
        self.timeOpen = timeOpen
        self.timeClose = timeClose
        if eid ==0:
            self.id = id
        else:
            self.id = eid
        # self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return {'id': self.id, 'name' : self.name, 'time opens at' : self.timeOpen, 'time closes at' : self.timeClose}

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


