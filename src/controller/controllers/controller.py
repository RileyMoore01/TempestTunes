#pip install mysql-connector

#Still needed: 
#   Connection to html to add the user input for user and password

import mysql.connector as sql

##########################
#       Db Info          #
##########################
#Host: 127.0.0.1
#Port: 3306 
#User: root
#Pass: 
db = sql.connect(host='127.0.0.1',
                user='root',
                password='pass',
                database='testDb')

myCursor = db.cursor()
##########################
#    Table creation      #
##########################
# myCursor.execute('CREATE DATABASE testDb')
# myCursor.execute("CREATE TABLE User (PID int PRIMARY KEY AUTO_INCREMENT, user_name varchar(50), password varchar(50))")

############################        
# PID |  USER  |  PASS     #        PID must be a unqiue value in the table
# -------------------------#        
# 0  |  test1  |  pass     #        All attributes within the table wil are non-nullable
# 1  |  test2  |  pass     #
############################

##########################
#    Logic Handeling     #
##########################
# myCursor.execute("set password for 'testDb'@'localhost' = PASSWORD('pass')")
# myCursor.execute("SET PASSWORD FOR 'root'@'localhost' = 'pass'")

print(myCursor.execute('DESCRIBE user'))
# mycursor.execute("insert into User (PID, user_name, password) values (1, 'riley', 'pass')")

