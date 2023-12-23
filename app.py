import mariadb
import dbcreds


conn = mariadb.connect(
    user=dbcreds.user, 
    password=dbcreds.password,
    host=dbcreds.host, 
    port=dbcreds.port, 
    database=dbcreds.database
   )
cursor = conn.cursor()
cursor.execute('CALL return_all_items()')
result = cursor.fetchall()

print (result)
   
