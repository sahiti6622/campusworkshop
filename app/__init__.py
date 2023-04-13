"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq4j9mbg5e4khql0a0-a.oregon-postgres.render.com",
        database="todo_u2dy",
        user="root",
        password="8cH5TYivzp8zevPhD2fTXv0CLuBMTaFk")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
