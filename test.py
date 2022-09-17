import json
import unittest
from app import create_app
from app import db
from config import configs

class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        config = configs['test']
        self.app = create_app(config)
        #clinte, por el cual haremos las peticiones
        self.client = self.app.test_client()
        #tipo de datos a enviar y recibir
        self.content_type = 'application/json'
        #direccon base
        self.path = 'http://localhost:5000/api/'

    def tearDown(self) -> None:
        with self.app.app_context():
            db.drop_all()
        # self.app_context.pop()

    def test_get_all(self):
        path = self.path + 'task'
        response = self.client.get(path = path)
        self.assertEqual(response.status_code, 200)

    def test_get_first(self):
        path = self.path +'task/1'
        response = self.client.get(path = path, content_type = self.content_type)
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data.decode('utf-8'))
        task_id = data['data']['id']
        self.assertEqual(task_id, 1)

    def test_get_not_found(self):
        path = self.path + 'task/100'
        response = self.client.get(path=path, content_type=self.content_type)
        self.assertEqual(response.status_code, 404)


    def test_create_task(self):
        path = self.path + 'task'
        data = {
            "deadLine": "2020-11-30 10:00:00",
            "description": "descripcion 123",
            "title": "title 123"
        }
        response = self.client.post(path=path, 
                                    content_type=self.content_type,
                                    data=json.dumps(data))

        self.assertEqual(response.status_code, 200)
        task = json.loads(response.data.decode('utf-8'))
        self.assertEqual(task['id'],3,"no son iguales")

    def test_put_task(self):
        path = self.path + 'task/1'
        data = {
            "description": "descripcion  actualizada 1",
            "title": "titulo actualizado 1"
        }

        response = self.client.put(path=path, 
                                    content_type=self.content_type,
                                    data=json.dumps(data))

        self.assertEqual(response.status_code, 200)
        task = json.loads(response.data.decode('utf-8'))
        self.assertEqual(task['id'],1,"no son iguales")
        self.assertEqual(task['title'], "titulo actualizado 1", "no son iguales")

    def test_delete_task(self):
        path = self.path + 'task/1'
        response = self.client.delete(path=path,
                                   content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(path=path,
                                      content_type=self.content_type)
        self.assertEqual(response.status_code, 404)
