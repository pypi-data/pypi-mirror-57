from flask import Flask
from flask_cors import CORS
from flask_script import Manager

from bolinette import env, Namespace
from bolinette.database import init_db
from bolinette.jwt import init_jwt
from bolinette.routes import init_routes
from bolinette.scripts import init_commands


class Bolinette:
    def __init__(self, name):
        self.app = Flask(name, static_url_path='')
        CORS(self.app, supports_credentials=True)
        self.manager = Manager(self.app)
        env.init(self.app)
        init_jwt(self.app)
        init_db(self.app)
        init_routes(self.app)
        init_commands(self.manager)
        Namespace.init_namespaces(self.app)
