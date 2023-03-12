from flask import Flask, jsonify, request, make_response

import requests
import sqlite3
import pandas as pd
import numpy as np

#creating an instance of flask
app = Flask(__name__)

users = [
    {"species": "Human", "name": "Justin", "status": "Alive", "rating": 10},
    {"species": "Human", "name": "Jayden", "status": "Alive", "rating": 10},

]

@app.route('/users/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
      user = request.args
      conn = sqlite3.connect("people.db")
      response =   requests.get("https://rickandmortyapi.com/api/character/"+user['id'])

      cname = response.json()["name"]
      cspecies =response.json()["species"]
      cstatus = response.json()["status"]

      new_data = jsonify({
            'id': user['id'],
            'species': cspecies,
            'name': cname,
            'status': cstatus,
            'rating': user['rating']
        })
      
      cursor = conn.cursor()
      cursor.execute("insert into person (id, name, species, status, rating) values (?, ?, ? ,? ,? )",
            (user['id'],cname,cspecies,cstatus,user['rating']))

      conn.commit()
      return (new_data) , 201
    
    else:
      conn = sqlite3.connect("people.db")
      cur = conn.cursor()
      cur.execute("SELECT * FROM person")
      people = cur.fetchall()

      return jsonify(people), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)