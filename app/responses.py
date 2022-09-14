from flask import jsonify


def response(data):
    return jsonify(
        {
            'succses':True,
            'data':data
        }
    ),200

def not_found():
    return jsonify(
        {
            'succses':False,
            'data':{},
            'message':'recurso no encontrado',
            'code':404
        }
    ),404

def hidden(data):
    return jsonify(
        {
            'succses':True,
            'data':data
        }
    ),200