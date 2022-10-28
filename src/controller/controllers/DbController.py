#pip install mysql-connector

import mysql.connector as sql

def testConnection():
    
    try:

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

        cursor = db.cursor(buffered=True)
        print("***** MySql database connection is open *****")



        ##########################
        #    Table creation      #
        ##########################

        #Only needs to be ran once for creation of the DB
        # myCursor.execute('CREATE DATABASE testDb')
        # myCursor.execute("CREATE TABLE User (PID int PRIMARY KEY AUTO_INCREMENT, user_name varchar(50), password varchar(50))")
        # myCursor.execute("SET PASSWORD FOR 'root'@'localhost' = 'pass'")

        print("--------- Current Databases ---------")
        cursor.execute("show databases")
        for x in cursor:
            print(x)
        print("--------- End of Databases ---------")


    except sql.Error as e:
        print("***** Error reading data from MySql database *****", e)


    finally:
        if db.is_connected():
            db.close()
            cursor.close()
            print("***** MySql database connection closed *****")


def AddNewUser():
        db = sql.connect(host='127.0.0.1',
                        user='root',
                        password='pass',
                        database='testDb')

        cursor = db.cursor(buffered=True)

        table = (
            "SELECT * from spUsername"
        )

        insertStatement = (
            "INSERT INTO spUsername (user_name) "
            "VALUES('first')"
        )
        data = ["..."]      # INSERT USER INPUT HERE ---------------------------

        # Execute, Commit, and Close database
        cursor.execute(insertStatement)
        db.commit()
        db.close()






testConnection()