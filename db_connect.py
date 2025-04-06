import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # change if your username is different
        password="root",  # replace with your MySQL password
        database="cs665_project1"
    )