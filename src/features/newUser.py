#pip install mysql-connector
import mysql.connector as sql
##########################
#       Db Info          #
##########################
#Host: 127.0.0.1
#Port: 3306 
#User: root
#Pass: pass
db = sql.connect(host='127.0.0.1',
                user='root',
                password='pass',
                database='testDb')

myCursor = db.cursor()




#Get current max PID
myCursor.execute("User spUsername")

###    Get user name and password from user     ###
userName = "test"

myCursor.execute(f"insert into spUsername (user_name) values('{userName}')'")