import time
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('timeOpen',
                        type=int,
                        required=True,
                        help="This item needs time open"
                        )
    #
    parser.add_argument('timeClose',
                        type=int,
                        required=True,
                        help="This item needs time close"
                        )


    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message' :
                    f"An items with name {name} already exists"
                   }, 400

        #put data after filtering out
        data = Item.parser.parse_args()
        id = ItemModel.find_by_name(name)
        item = ItemModel(name, data['timeOpen'],data['timeClose'],id)
        try:
            item.save_to_db()
        except:
            return {"message" : "An error occurred while inserting item"}, 500
        return item.json(), 201

    @jwt_required()
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        else:
            return {'message': 'delete failed'}, 400

        return {'message' : 'item deleted'}

    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        id = ItemModel.find_by_name(name)
        # data['timeOpen'] *=3600
        if item is None:
            item = ItemModel(name, data['timeOpen'],data['timeClose'],id)
        else:
            item.timeOpen = data['timeOpen']
            item.timeClose = data['timeClose']

        item.save_to_db()
        return item.json()


class ItemId(Resource):
        def get(self,  id):
            item = ItemModel.find_by_id(id)
            if item:
                return item.json()
            return {'message': 'item not found'}, 404


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
        # return  {'items': list(map(lambda  x: x.json(), ItemModel.query.all()))}