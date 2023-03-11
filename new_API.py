import requests
import sqlite3

response =   requests.get("https://rickandmortyapi.com/api/character/135")

print(response.json()["name"])
print(response.json()["species"])
print(response.json()["status"])
print(response.status_code)

