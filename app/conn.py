import mysql.connector

conn = mysql.connector.connect(host='localhost',
                               database='kinerja_kit',
                               user='root',
                               password='')
cur = conn.cursor()