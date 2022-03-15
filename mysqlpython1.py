#import mysql.connector
#
#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="Fadeelah9685"
#)
#
#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE latih2")
#mycursor.execute("SHOW DATABASES")
#
#for x in mycursor:
#  print(x)

#import mysql.connector
#
#mydb = mysql.connector.connect(
#  host = "localhost",
#  user = "root",
#  password = "Fadeelah9685",
#  database = "latih2"
#)
#
#kursor = mydb.cursor()
#kursor.execute("create table customers (name varchar(255), #address varchar(255)) ")
#
#kursor.execute("show tables")

#for x in mycursor:
#  print(x)

#kursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#import mysql.connector
#
#mydb = mysql.connector.connect(
#  host = "localhost",
#  user = "root",
#  password = "Fadeelah9685",
#  database = "latih2"
#)
#mycursor = mydb.cursor()
#
#sql = "insert into customers (name, address) values (%s, %s)"
#val = ("arif", "bogor 12")
#mycursor.execute(sql, val)
#mydb.commit()
#
#print(mycursor.rowcount, "record inserted")

#import mysql.connector
#
#mydb = mysql.connector.connect(
#  host = "localhost",
#  user = "root",
#  password = "Fadeelah9685",
#  database = "latih2"
#)
#
#kursor = mydb.cursor()

#sql = "insert into customers (name, address) values (%s, %s)"
#val = [
#  ('Sisy', 'malabar 2'),
#  ('Susan', 'One way 98'),
#  ('Vicky', 'Yellow Garden 2'),
#  ('Ben', 'Park Lane 38'),
#  ('William', 'Central st 954'),
#  ('Chuck', 'Main Road 989'),
#  ('Viola', 'Sideway 1633')
#]

#kursor.executemany(sql, val)
#mydb.commit()
#print(kursor.rowcount, "was inserted.")

#kursor.execute("select * from customers")
#kursor.execute("select name,address from customers")
#myresult = kursor.fetchall()
#myresult = kursor.fetchone() #buat ambil 1 row

#for x in myresult:
#  print(x)

#sql = "select  * from customers where address = 'Park Lane 38'"
#sql = "select  * from customers where address like '%way%'"
#kursor.execute(sql)

#sql = "select * from customers where address = %s"
#adr = ("Yellow Garden 2",)
#
#kursor.execute(sql,adr)

#sql = "select * from customers order by name "
#sql = "delete from customers where address = 'Yellow Garden 2'"
#
#kursor.execute(sql)
#mydb.commit()
#
#print(kursor.rowcount, "record(s) deleted")

#sql = "delete from customers where address = %s"
#val = ("Main Road 989",)
#kursor.execute(sql,val)
#mydb.commit()

#print(kursor.rowcount,"record(s) deleted")

#sql = "update customers set address = 'bojonggede' where address #= 'bogor 12'"
#kursor.execute(sql)
#mydb.commit()
#print(kursor.rowcount,"record(s) affected")
#
#sql2 = "select * from customers"
#kursor.execute(sql2)
#
#myresult = kursor.fetchall()
#
#for x in myresult:
#  print(x)

import mysql.connector

conn = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Fadeelah9685",
  database = "latih2"
)
kursor = conn.cursor()

#kursor.execute("create table users (id INT AUTO_INCREMENT PRIMARY #KEY, name VARCHAR(255), fav VARCHAR(255))") 
#kursor.execute("create table products (id INT AUTO_INCREMENT #PRIMARY KEY, name VARCHAR(255))")
#
#kursor.execute("show tables")
#
#for x in kursor:
#  print(x)

#sql = "insert into users (id, name, fav) values (%s, %s, %s)"
#var = [
#  ('1', 'Arif', '154'),
#  ('2', 'Fadil', '154'),
#  ('3', 'Sisy', '155'),
#  ('4', 'Isywara', '156'),
#  ('5', 'Corry', '')
#]
#
#kursor.executemany(sql, var)
#conn.commit()
#print(kursor.rowcount, "inserted")

#sql = "insert into products (id, name) values (%s, %s)"
#var = [
#  ('154','Takoyaki'),
#  ('155','Sosisan'),
#  ('156','Tape bakar')
#]
#kursor.executemany(sql, var)
#conn.commit()
#print(kursor.rowcount,"inserted")

#kursor.execute("select * from products")
#result = kursor.fetchall()
#
#for x in result:
#  print(x)

sql = "select \
  users.name as user,\
  products.name as favorite \
  from users \
  right join products on users.fav = products.id  "
kursor.execute(sql)

result = kursor.fetchall()

for x in result:
  print(x)