import requests
import sqlite3


conn = sqlite3.connect("people.db")
columns = [
     "id INTEGER PRIMARY KEY",
     "name VARCHAR ",
     "species VARCHAR",
     "status VARCHAR",
     "rating INTEGER"
 ]
create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
conn.execute(create_table_cmd)

people = [
    "1, 'Justin', 'Human', 'Alive',10",
    "2, 'Jayden', 'Human', 'Alive',6",
    "3, 'Love', 'Human', 'Alive',12",
 ]
for person_data in people:
     insert_cmd = f"INSERT INTO person VALUES ({person_data})"
     conn.execute(insert_cmd)

conn.commit()


cur = conn.cursor()
cur.execute("SELECT * FROM person")


people = cur.fetchall()
for person in people:
     print(person)

response =   requests.get("https://rickandmortyapi.com/api/character/135")

cname = response.json()["name"]
cspecies =response.json()["species"]
cstatus = response.json()["status"]
print(response.status_code)

cursor = conn.cursor()

cursor.execute("insert into person (id, name, species, status, rating) values (?, ?, ? ,? ,? )",
            (4,cname,cspecies,cstatus,5))

conn.commit()

cur = conn.cursor()
cur.execute("SELECT * FROM person")

people = cur.fetchall()
for person in people:
     print(person)