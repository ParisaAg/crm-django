import mysql.connector




DataBase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
)


cursor_object=DataBase.cursor()

cursor_object.execute('CREATE DATABASE mysqlcrm')

print("Database created successfully")
