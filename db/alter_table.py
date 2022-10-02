import db.conn as conn

base_command = ("ALTER TABLE {table_name} ADD column {column_name} {data_type}")
sql_command = base_command.format(table_name='tes', column_name='trip', data_type='INTEGER')


conn.cur.execute(sql_command)
conn.conn.commit()
conn.conn.close()