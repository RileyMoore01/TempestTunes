print("--------- Current Databases ---------")
        cursor.execute("show databases")
        for x in cursor:
            print(x)
        print("--------- End of Databases ---------")