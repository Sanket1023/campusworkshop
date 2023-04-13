"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq3ppmbg5e4khqfjtg-a.oregon-postgres.render.com/todo_og6o",
        database="todo_og6o",
        user="root",
        password="QG7YCg23MzwDqRnKIr96UkLNNzyKIxoy")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
