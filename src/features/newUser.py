#pip install mysql-connector
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
id = myCursor.execute("""select MAX(PID) from user""")
id += 1   #new users PID

###    Get user name and password from user     ###
userName = "test"
password = "pass"

myCursor.execute(f"insert into user ('PID', 'user_name','password' values('{id}', '{userName}', '{password}'")