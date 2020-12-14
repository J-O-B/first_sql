import os
import pymysql

# Get username From Git Workspace
username = os.getenv('first_sql')

# Connect to the database:
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')


try:
    # Run A Query
    with connection.cursor() as cursor:
        sql = "Select * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close Connection to SQL
    connection.close()
