from flask import Blueprint

from .responses import response, not_found
from .models.tasks import Task

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/task', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return response([ task.serialize() for task in tasks])

@api.route('/task/<id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    if task is None:
        return not_found()
    return response(task.serialize())

@api.route('/task', methods=['POST'])
def create_task():
    pass

@api.route('/task/<id>', methods=['PUT'])
def update_tasks(id):
    pass

@api.route('/task/<id>', methods=['DELETE'])
def delete_tasks():
    pass