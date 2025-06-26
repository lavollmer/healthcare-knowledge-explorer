from flask import Flask
from neo4j import GraphDatabase

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

if __name__ == '__main__':
    app.run(debug=True) 