##Creado por Allan B., se conecta a un contenedor de mysql -- pasos de configuracion antes del cod de python.
#docker run --name=test --env="MYSQL_ROOT_PASSWORD=qwerty" -p 3306:3306 -d mysql:latest
#docker exec -it test mysql -uroot -pqwerty
#CREATE DATABASE test_db;
#use test_db;
#CREATE TABLE test_table (userId INT NOT NULL AUTO_INCREMENT PRIMARY KEY, firstName VARCHAR(20), lastName VARCHAR(20));

#CREATE USER 'allan'@'%' IDENTIFIED BY 'allan1';

#GRANT ALL PRIVILEGES ON test_db.* to 'allan'@'%';
#revisar siempre W3schools codigo mas sencillo y conciso.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port= 3306,
  user="allan",
  password="allan1",
  database="test_db"
)

mycursor = mydb.cursor()

sql = "INSERT INTO test_table (firstName, lastName) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

try:
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "registros fueron insertados...")
    # ... YOUR CODE HERE ... #
except Exception as e:
    # ... PRINT THE ERROR MESSAGE ... #
    if e != "":
        print("No se permiten registros duplicados...")



