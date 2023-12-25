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

items = result

# print(items)
   
cursor.close
conn.close


for i in range(len(items)):
     print(items[i][0:2])

user_input = input('Please enter a price: ')
user_input = int(user_input)
# print(user_price)

cursor = conn.cursor()
cursor.execute('CALL get_item_by_user_input(?)',[user_input])

cursor.close
conn.close

result = cursor.fetchall() 
print(result)


