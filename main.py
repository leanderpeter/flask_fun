from flask import Flask, render_template
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from flask import request
import json
import os
print("Lets go...")

"""Flask wird hiermit instanziert"""
#app = Flask(__name__, static_folder='static/build', static_url_path='/', template_folder="template")
app = Flask(__name__, template_folder="template")


@app.route('/')
def helloWorld():
    # return '<h1>Hi Leander!</h1>'
    return 'Hello World!'
    # return app.send_static_file('index.html')
