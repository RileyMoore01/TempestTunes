#pip install mysql-connector
import mysql.connector as sql

db = sql.connect(host='120.0.01',
                user = 'root',
                password = 'pass',
                database = 'testDb')

myCursor = db.cursor()

myCursor.execute("select * from testDb root where PID = '1'")