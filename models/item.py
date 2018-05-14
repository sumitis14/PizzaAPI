from db import db
class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    timeOpen = db.Column(db.String(80))
    timeClose = db.Column(db.String(80))

    def __init__(self,name, timeOpen, timeClose):
        self.name = name
        self.timeOpen = timeOpen
        self.timeClose = timeClose


    def json(self):
        return {'name' : self.name, 'time opens at' : self.timeOpen, 'time closes at' : self.timeClose}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first() #SELECT * FROM WHERE name=name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


