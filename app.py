from flask import Flask
from controller.user_controller import api
from config import load_config_to_app

app = Flask(__name__)
app.register_blueprint(api)
load_config_to_app(app)

if __name__ == '__main__':
    app.run(port=app.config['server']['port'], host='127.0.0.1', debug=True)
