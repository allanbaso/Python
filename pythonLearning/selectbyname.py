import mysql.connector

mydb = mysql.connector.connect(
  host="allan.ubuntu.com",
  user="allan2",
  password="allan2",
  database="newDB"
)
mycursor = mydb.cursor()
value=input('Digite el nombre : ')
mycursor.execute("SELECT * FROM table1 where name like '%"+value+"%'")

myresult = mycursor.fetchall()
if myresult:
  for x in myresult:
    print(x)
else:
  print('No hay nombres con ese dato...')