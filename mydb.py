import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password'
)

#Prepare a curcor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute('CREATE DATABASE crmdb')

print("crmdb created!!")