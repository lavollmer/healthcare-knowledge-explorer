from flask import Flask
from neo4j import GraphDatabase
import dotenv
import os

app = Flask(__name__)

URL=
AUTH=

# Verify connectivity of Neo4j database
with GraphDatabase.driver(URL, auth=AUTH) as driver:
    driver.verify_connectivity()
    print("Connected to Neo4j database successfully!")


@app.route('/')
def home():
    return "Welcome to the Flask App!"

if __name__ == '__main__':
    app.run(debug=True) 