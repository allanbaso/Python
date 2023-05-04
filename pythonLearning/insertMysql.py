import mysql.connector

mydb = mysql.connector.connect(
  host="allan.ubuntu.com",
  user="allan2",
  password="allan2",
  database="newDB"
)

dato=input('Digite el valor que quiere agregar : ')
mycursor = mydb.cursor()

try:
  mycursor.execute("INSERT INTO table2 (nombre) VALUES ('"+dato+"')")

  mydb.commit()

  #print(mycursor.rowcount, "record inserted. con el id : ",mycursor.lastrowid)

  mycursor.execute("SELECT * FROM table2")

  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
except:
  print("Revise si el dato ya se encuentra agregado, no se permiten valores duplicados")