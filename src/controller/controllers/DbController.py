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

        ############################        Example model
        # PID |  USER  |  PASS     #        PID must be a unqiue value in the table
        # -------------------------#        
        # 0  |  test1  |  pass     #        All attributes within the table are non-nullable
        # 1  |  test2  |  pass     #
        ############################


        ##########################
        #    Logic Handeling     #
        ##########################

        print("--------- Current Databases ---------")
        cursor.execute("show databases")
        for x in cursor:
            print(x)
        print("--------- End of Databases ---------")

        ##########################
        #    Insert Statement    #
        ##########################
        table = (
            "SELECT * from spUsername"
        )

        insertStatement = (
            "INSERT INTO spUsername (user_name) "
            "VALUES('first')"
        )
        data = ["jacob"]

        # Execute, Commit, and Close database
        cursor.execute(insertStatement)
        db.commit()
        db.close()



    except sql.Error as e:
        print("***** Error reading data from MySql database *****", e)


    finally:
        if db.is_connected():
            db.close()
            cursor.close()
            print("***** MySql database connection closed *****")

testConnection()