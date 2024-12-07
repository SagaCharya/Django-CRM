import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='new_user',
    password='new_password',
)

## perpare a cursor object

cursorObject = dataBase.cursor()


#Create database

cursorObject.execute(" CREATE DATABASE saga")


print(" all done")