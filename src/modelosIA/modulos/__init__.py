import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger

basedir = os.path.abspath(os.path.dirname(__file__))


def registrar_handlers():
    import modelosIA.modulos.aplicacion


def comenzar_consumidor():
    import threading
    import modelosIA.modulos.infraestructura.consumidores as modelosIA

    threading.Thread(target=modelosIA.suscribirse_a_eventos).start()

    threading.Thread(target=modelosIA.suscribirse_a_comandos).start()

def create_app(configuracion={}):
    app = Flask(__name__, instance_relative_config=True)


    app.secret_key = "9d58f98f-3ae8-4149-a09f-3a8c2012e32c"
    app.config["SESSION_TYPE"] = "filesystem"
    app.config["TESTING"] = configuracion.get("TESTING")


    registrar_handlers()

    with app.app_context():
        if not app.config.get("TESTING"):
            comenzar_consumidor()

    return app
