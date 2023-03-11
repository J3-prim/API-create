from flask import Flask, jsonify, request
import pandas as pd
import numpy as np

app = Flask(__name__)

users = [
    {"id": 1, "name": "Thailand", "city": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "city": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "city": "Cairo", "area": 1010408},
]

@app.route('/users/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
      user = request.args

      new_data = jsonify({
            'id': user['id'],
            'name': user['name'],
            'city': user['city'],
            'area': [25406]
        })

      return (new_data) , 201
    else:
      return jsonify(users), 200

@app.route('/person/')
def hello():
    return jsonify({'name':'Jimit',
                    'address':'India'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)