from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT

from resources.user import UserRegister
from resources.item import Item, ItemId, ItemList
from security import authenticate, identity


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.secret_key = '1ab2'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) #creates /auth

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemId,'/item/<int:id>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister, '/register') #User registration

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)