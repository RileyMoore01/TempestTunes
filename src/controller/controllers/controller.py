#pip install mysql-connector
import mysql.connector as sql

db = sql.connect(host='localhost',
                user='root',
                password='password.',
                database='testDb')

myCursor = db.cursor()
##########################
#    Table creation      #
##########################
# myCursor.execute('CREATE DATABASE testDb')
# myCursor.execute("CREATE TABLE User (PID int PRIMARY KEY AUTO_INCREMENT, user_name varchar(50), password varchar(50))")

##########################
#    Logic Handeling     #
##########################
myCursor.execute("set password for 'testDb'@'localhost' = PASSWORD('pass')")

myCursor.execute('DESCRIBE User')
# mycursor.execute("insert into User (PID, user_name, password) values (1, 'riley', 'pass')")

