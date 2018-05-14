import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('timeOpen',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    #
    parser.add_argument('timeClose',
                        type=str,
                        required=True,
                        help="This item needs time close"
                        )

    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'mesaage' : 'item not found'}, 404


    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message' :
                    f"An items with name {name} already exists"
                   }, 400

        #put data after filtering out
        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {"message" : "An error occurred while inserting item"}, 500
        return item.json(), 201


    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message' : 'item deleted'}

    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.timeOpen = data['timeOpen']
            item.timeClose = data['timeClose']

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items' : [item.json() for item in ItemModel.query.all()]}