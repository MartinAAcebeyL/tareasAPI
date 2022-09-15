from unittest import TestCase
import unittest
from app import create_app
from config import configs
from app import db

class TestAPI(TestCase):
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

    def test_get_all(self):
        path = self.path + 'task'
        response = self.client.get(path = path)
        self.assertEqual(response.status_code, 200)

    def test_get_first(self):
        path = self.path +'task/1'
        print(path)
        response = self.client.get(path = path, content_type = self.content_type)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()