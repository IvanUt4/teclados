from flask import jsonify, request
from flask_pymongo import pymongo
from app import create_app
from bson.json_util import dumps
import db_config as db

app = create_app()

key = "3179JGb215"

@app.route('/test/')
def test():
    return jsonify({
        "message": "API working ok",

    })


@app.route('/api/all_keyboards/', methods=['GET'])
def show_keyboards():
    all_keyboards = dumps(list(db.db.api_teclados.find()))
    return all_keyboards


@app.route(f'/api/api_teclados/<int:n_key>/', methods=['GET'])
def show_a_key_board(n_key):
    keyboard = dumps(db.db.api_teclados.find_one({'n_key':n_key}))
    return keyboard


@app.route(f'/api/{key}/new_keyboard/', methods=['POST'])
def add_new_keyboard():
    db.db.api_teclados.insert_one({
        "n_key": request.json["n_key"],
        "modelo":request.json["modelo"],
        "marca":request.json["marca"],
        "img":request.json["img"],
    })
    return jsonify({
        "message":"A new keyboard was added with success",
        "status": 200,
    })


@app.route(f'/api/{key}/api_teclados/update/<int:n_key>',methods=['PUT'])
def update_keyboard(n_key):

    if db.db.api_teclados.find_one({'n_key':n_key}):
        db.db.api_teclados.update_one({'n_key':n_key},
        {'$set':{
            "n_key": request.json["n_key"],
            "modelo":request.json["modelo"],
            "marca":request.json["marca"],
            "img":request.json["img"],
        }})
    else:
        return jsonify({"status":400, "message": f"Keyboard #{n_key} not found"})

    return jsonify({"status":200, "message": f"The keyboard #{n_key} of the top was updated"})


@app.route(f'/api/{key}/api_teclados/del/<int:n_key>',methods=['DELETE'])
def delete_keyboard(n_key):
    if db.db.api_teclados.find_one({'n_key':n_key}):
        db.db.api_teclados.delete_one({'n_key':n_key})
    else:
        return jsonify({"status":400, "message": f"Keyboard #{n_key} not found"})
    return jsonify({"status":200, "message": f"The Keyboard #{n_key} was deleted"})


if __name__ == '__main__':
    app.run(load_dotenv=True, port=8080)
