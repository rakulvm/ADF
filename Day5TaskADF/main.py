import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rakul123#",
    database="pyapplication"
)
mycursor=mydb.cursor()
mycursor.execute("select * from request_info")
for db in mycursor:
    print(db)