from flask import Flask
from neo4j import GraphDatabase
import dotenv
import os

app = Flask(__name__)

uri='neo4j://localhost:5173'
username = USERNAME
password= PASSWORD

load_status = dotenv.load_dotenv()
if not load_status:
    print("Failed to load environment variables.")
    exit(1)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

if __name__ == '__main__':
    app.run(debug=True) 