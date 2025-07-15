# Handles SQLite connection

import sqlite3

def get_connection():
    return sqlite3.connect('healthcare.db')