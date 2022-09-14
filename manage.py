from sys import api_version
from app import create_app
from config import configs

config = configs['default']
app = create_app(config)

if __name__ == '__main__':
    app.run()