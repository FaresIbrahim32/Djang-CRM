import mysql.connector

# Establishing a connection to the database
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='FaresIbrahim32'
)

# Cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE football")

# Database created
if dataBase.is_connected():
    print("Connection successfully established!")
