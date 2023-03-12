from flask import Flask, jsonify, request, make_response

import requests
import sqlite3
import pandas as pd
import numpy as np

#creating an instance of flask
app = Flask(__name__)



@app.route('/users/', methods=['GET', 'POST'])
def userInt():
    if request.method == 'POST':
      user = request.args
      conn = sqlite3.connect("people.db")
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM person WHERE id IN (?)",(user['id']))
      

      if cursor.fetchall() ==[]:
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
        conn.close()
        return (new_data) , 201
      else:   return "Character id already exists in database",409
      
    else:
      conn = sqlite3.connect("people.db")
      cur = conn.cursor()
      cur.execute("SELECT * FROM person")
      people = cur.fetchall()
      conn.commit()
      conn.close() 
      return jsonify(people), 200

@app.route('/delete',methods=['DELETE'])
def userDel():

    user = request.args
    conn = sqlite3.connect("people.db")
    cursor = conn.cursor()
    localid = (user['id'])
    cursor.execute("SELECT * FROM person WHERE id IN (?)",localid)

    if cursor.fetchall() ==[]:
        
      return "There is no entry for that character to delete" , 404
    else:  
      cursor.execute("DELETE FROM person WHERE id = ?",(localid))
      conn.commit()
      conn.close()
      return "Character deleted", 200  

@app.route('/edit',methods=['PUT'])
def entryEdit():
    user = request.args
    conn = sqlite3.connect("people.db")
    cursor = conn.cursor()
    localid = (user['id'])
    cursor.execute("SELECT * FROM person WHERE id IN (?)",localid)

    if cursor.fetchall() ==[]:
        
      return "There is no entry for that character to update" , 404
    else:  
      cursor.execute("UPDATE person SET rating=? WHERE id=?",(user['rating'],localid))

      conn.commit()
      conn.close()
    return "Character updated", 200  
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)