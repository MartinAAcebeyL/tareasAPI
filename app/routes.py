import re
from flask import Blueprint
from flask import request

from .responses import *
from .models.tasks import Task

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/task', methods=['GET'])
def get_tasks():
    page = int(request.args.get('page', 1))
    order = request.args.get('order', 'asc')
    
    tasks = Task.get_by_page(order, page, 5)
    # tasks = Task.query.all()
    return response([ task.serialize() for task in tasks])


    

@api.route('/task/<id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    if task is None:
        return not_found()
    return response(task.serialize())

@api.route('/task', methods=['POST'])
def create_task():
    response = request.get_json()
    if response is None:
        return bad_request()
    
    if 'title' not in response or len(response['title']) > 50:
        return bad_request()

    if 'description' not in response or 'deadLine' not in response:
        return bad_request()

    task = Task.create(response['title'], response['description'], response['deadLine'])
    if task.save():
        return task.serialize()

    return bad_request()

@api.route('/task/<id>', methods=['PUT'])
def update_tasks(id):
    task = Task.query.get(id)
    if task is None:
        return not_found()
    response = request.get_json()
    
    task.title = response.get('title', task.title)
    task.description = response.get('description', task.description)
    task.deadLine = response.get('deadLine', task.deadLine)

    if task.save():
        return task.serialize()
    return bad_request()

@api.route('/task/<id>', methods=['DELETE'])
def delete_tasks(id):
    task = Task.query.get(id)
    if task is None:
        return not_found()

    if task.unsave():
        return task.serialize()
    return bad_request()