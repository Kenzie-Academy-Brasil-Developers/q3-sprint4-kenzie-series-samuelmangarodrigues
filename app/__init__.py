from flask import Flask
from app.routes import series_route
from psycopg2.errors import FdwTableNotFound

def create_app():

    app=Flask(__name__)
    app.register_blueprint(series_route.bp)


    return app