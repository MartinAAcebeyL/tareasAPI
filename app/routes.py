from flask import Blueprint
from flask import request

from .responses import *
from .models.tasks import Task
from .shemas import *

api = Blueprint('api', __name__, url_prefix='/api')


def exist_task(function):
    def wrap(*args, **kwargs):
        id = kwargs.get('id', 0)
        task = Task.query.get(id)
        if task is None:
            return not_found()
        return function(task)
    wrap.__name__ = function.__name__
    return wrap

@api.route('/task', methods=['GET'])
def get_tasks():
    page = int(request.args.get('page', 1))
    order = request.args.get('order', 'asc')
    
    tasks = Task.get_by_page(order, page, 5)
    # tasks = Task.query.all()
    # return response([ task.serialize() for task in tasks])
    return response(task_shemas.dump(tasks))

@api.route('/task/<id>', methods=['GET'])
@exist_task
def get_task(task):
    return response(task_shema.dump(task))

@api.route('/task', methods=['POST'])
def create_task():
    response = request.get_json()
    
    error = params_task_shema.validate(response)
    if error:
        print(error)
        return bad_request()

    task = Task.create(response['title'], response['description'], response['deadLine'])
    if task.save():
        return response(task_shema.dump(task))

    return bad_request()

@api.route('/task/<id>', methods=['PUT'])
@exist_task
def update_tasks(task):
    response = request.get_json()
    
    task.title = response.get('title', task.title)
    task.description = response.get('description', task.description)
    task.deadLine = response.get('deadLine', task.deadLine)

    if task.save():
        return response(task_shema.dump(task))
    return bad_request()

@api.route('/task/<id>', methods=['DELETE'])
@exist_task
def delete_tasks(task):
    if task.unsave():
        return response(task_shema.dump(task))
    return bad_request()