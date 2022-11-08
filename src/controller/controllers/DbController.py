# pip install mysql-connector
import mysql.connector as sql

# Global Properties
MAX_ROW_ID = 0


#
#       USER INPUT ON LINES 61 - 69 NEEDED
#



def testConnection():
    try:

        # --- DATABASE INFORMATION ---
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
        

        # Only needs to be ran once for creation of the DB
        # myCursor.execute('CREATE DATABASE testDb')
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

        if db.is_connected():
            cursor = db.cursor(buffered=True)
            
            userName = 'user_name'
            password = 'password'
            mSunny = 1
            mRainy = 2
            mSnowy = 3
            mWindy = 4
            Location = '79401'

            insertStatement = "insert into user (user_name, password, mSunny, mWindy, mSnowy, mRainy, Location, row_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            data = (userName, password, mSunny, mWindy, mSnowy, mRainy, Location, MAX_ROW_ID)

            cursor.execute(insertStatement, data)
            db.commit()
            cursor.close()
            db.close()






def showAllRecords():
    db = sql.connect(host='127.0.0.1',
                        user='root',
                        password='pass',
                        database='testDb')

    if db.is_connected():
        cursor = db.cursor(buffered=True)
        statement = "select * from user"
        cursor.execute(statement)
        result = cursor.fetchall()
        print(result)

        cursor.close()
        db.close()






def getMaxPid():
    db = sql.connect(host='127.0.0.1',
                        user='root',
                        password='pass',
                        database='testDb')

    if db.is_connected():
        cursor = db.cursor(buffered=True)
        cursor.execute("select MAX(row_id) as RowId from user;")

        arr  = cursor.fetchone()
        for i in arr:
            result = i

        cursor.close()
        db.close()

        MAX_ROW_ID = result




def updateWeatherStatus():
        db = sql.connect(host='127.0.0.1',
                    user='root',
                    password='pass',
                    database='testDb')

        if db.is_connected():
            cursor = db.cursor(buffered=True)
            
            rowId = 5
            mSunny = 4
            mRainy = 4
            mSnowy = 4
            mWindy = 4
            Location = '76210'

            updateStatement = "update user set mSunny = %s, mWindy = %s, mSnowy=%s, mRainy=%s where row_id=%s"
            data = (mSunny, mWindy, mSnowy, mRainy, rowId)

            cursor.execute(updateStatement, data)
            db.commit()
            cursor.close()
            db.close()


def updateLocation():
        db = sql.connect(host='127.0.0.1',
                user='root',
                password='pass',
                database='testDb')

        if db.is_connected():
            cursor = db.cursor(buffered=True)
            
            rowId = 5
            Location = '76219'

            updateStatement = "update user set Location=%s where row_id=%s"
            data = (Location, rowId)

            cursor.execute(updateStatement, data)
            db.commit()
            cursor.close()
            db.close()

def updateUsername():
        db = sql.connect(host='127.0.0.1',
                user='root',
                password='pass',
                database='testDb')

        if db.is_connected():
            cursor = db.cursor(buffered=True)
            
            rowId = 4
            userName = 'testUpdate'

            updateStatement = "update user set user_name=%s where row_id=%s"
            data = (userName, rowId)

            cursor.execute(updateStatement, data)
            db.commit()
            cursor.close()
            db.close()

def updatePassword():
        db = sql.connect(host='127.0.0.1',
                user='root',
                password='pass',
                database='testDb')

        if db.is_connected():
            cursor = db.cursor(buffered=True)
            
            rowId = 4
            password = 'newPasswordUpdate'

            updateStatement = "update user set password=%s where row_id=%s"
            data = (password, rowId)

            cursor.execute(updateStatement, data)
            db.commit()
            cursor.close()
            db.close()



# -------------------------------------
#          Function Calls            --
# -------------------------------------

# testConnection()

# AddNewUser()
# getMaxPid()

# updateWeatherStatus()
# updateLocation()
# updateUsername()
# updatePassword()

# showAllRecords()
