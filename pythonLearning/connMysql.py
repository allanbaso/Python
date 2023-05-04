import mysql.connector
##conx a bd de una maquina virutal
#revisando cambios
mydb = mysql.connector.connect(
  host="192.168.122.206",
  user="allan2",
  password="allan2",
  database="newDB"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM table1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
