import os
import datetime
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
        cursor.execute("DELETE FROM Friends WHERE name in ('jim','bob')")
        connection.commit()
finally:
    # Close Connection to SQL
    connection.close()
