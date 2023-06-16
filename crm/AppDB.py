import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '123qwe,./',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE AppDB")

print("All done")