import mysql.connector

utdb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = "Privateman3+",
)

my_cursor = utdb.cursor()

my_cursor.execute("CREATE DATABASE allmydata")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)