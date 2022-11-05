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
        # Only needs to be ran once for creation of the DB


        # myCursor.execute('CREATE DATABASE testDb')
        # myCursor.execute("CREATE TABLE User (PID int PRIMARY KEY AUTO_INCREMENT, user_name varchar(50), password varchar(50))")
        # myCursor.execute("SET PASSWORD FOR 'root'@'localhost' = 'pass'")

        # CREATE TABLE `testdb`.`user` (
            # `PID` INT NOT NULL AUTO_INCREMENT,
            # `user_name` VARCHAR(45) NOT NULL,
            # `password` VARCHAR(45) NULL,
            # `mSunny` INT NOT NULL,
            # `mSnowy` INT NOT NULL,
            # `mRainy` INT NOT NULL,
            # `mWindy` INT NOT NULL,
            # PRIMARY KEY (`PID`));

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
            "SELECT * from user"
        )
        
        # PID = cursor.execute("Select MAX PID from user")
        userName = "testMySqlConnection"
        password = "pass"
        mSunny = 1
        mRainy = 2
        mSnowy = 3
        mWindy = 4
        Location = "79401"

        insertStatement = (
            "insert into user (user_name, password, mSunny, mWindy, mSnowy, mRainy, Location)  "
            f"VALUES({userName}, {password}, {mSunny},{mRainy}, {mSnowy}, {mWindy}, {Location})"
        )
        
        
        data = ["testMySqlConnection", "pass", mSunny, mSnowy, mRainy, mRainy, Location]      # INSERT USER INPUT HERE ---------------------------

        # Execute, Commit, and Close database
        cursor.execute(insertStatement, data)
        db.commit()
        db.close()






AddNewUser()
