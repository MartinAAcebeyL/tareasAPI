from flask import jsonify

def response(data:dict):
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

def bad_request():
    return jsonify(
        {
            'succses':False,
            'data':{},
            'message':'mal requerimiento',
            'code':400
        }
    ),400