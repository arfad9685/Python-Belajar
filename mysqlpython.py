#create database
#import mysql.connector
#
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685"
#)
#
#mycursor = mydb.cursor()
##mycursor.execute("CREATE DATABASE latih1")
#mycursor.execute("SHOW DATABASES")
#
#for x in mycursor:
#  print(x) 


#create table

#import mysql.connector
#
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685",
#    database = "latih1"
#)
#
#mycursor = mydb.cursor()
#
##mycursor.execute("CREATE TABLE customers (name VARCHAR(255), #address VARCHAR(255))")
#mycursor.execute("SHOW TABLES")
#
#for x in mycursor:
#    print(x)

#create primary key
#import mysql.connector
#
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685",
#    database = "latih1"
#)
#
#mycursor = mydb.cursor()
#
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#insert 1 data

#import mysql.connector
#
##from Tkinter36 import database
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685",
#    database = "latih1"
#)
#
#mycursor = mydb.cursor()
#
#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("Arif", "malabar 2")
#mycursor.execute(sql, val)
#
#mydb.commit()
#print(mycursor.rowcount, "record inserted.")

#insert multiple data
#import mysql.connector
#
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685",
#    database = "latih1"
#)
#
#mycursor = mydb.cursor()
#
#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = [
#    ('Fadil', 'bogor 1'),
#    ('Amy', 'Apple st 652'),
#    ('Hannah', 'Mountain 21'),
#    ('Michael', 'Valley 345'),
#    ('Sandy', 'Ocean blvd 2'),
#    ('Betty', 'Green Grass 1'),
#    ('Richard', 'Sky st 331'),
#    ('Susan', 'One way 98'),
#    ('Vicky', 'Yellow Garden 2'),
#    ('Ben', 'Park Lane 38'),
#    ('William', 'Central st 954'),
#    ('Chuck', 'Main Road 989'),
#    ('Viola', 'Sideway 1633')
#]
#
#mycursor.executemany(sql, val)
#
#mydb.commit()
#
#print(mycursor.rowcount, "was inserted")


#Get Inserted ID
#import mysql.connector
#
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685",
#    database = "latih1"
#)
#
#mycursor = mydb.cursor()
#
#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("Isywara", "Bogor 5")
#mycursor.execute(sql, val)
#
#mydb.commit()
#
#print("1 record inserted, ID: ", mycursor.lastrowid)

#import mysql.connector
#
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685",
#    database = "latih1"
#)
#
#mycursor = mydb.cursor()
#
##mycursor.execute("select * from customers")
#mycursor.execute("select name, address from customers")
#myresult = mycursor.fetchall()
#
#for x in myresult:
#    print(x)

#import mysql.connector
#
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685",
#    database = "latih1"
#)
#
#mycursor = mydb.cursor()
#

#mycursor.execute("select * from customers")
#myresult = mycursor.fetchone()
#print(myresult)

#import mysql.connector
#
#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="Fadeelah9685",
#  database="latih1"
#)
#
#mycursor = mydb.cursor()
#
#sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
#
#mycursor.execute(sql)
#
#myresult = mycursor.fetchall()
#
#for x in myresult:
#  print(x)

#import mysql.connector
#
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685",
#    database = "latih1"
#)

#mycursor = mydb.cursor()
#sql = "select * from customers where address like '%way%'"
#
#mycursor.execute(sql)
#
#myresult = mycursor.fetchall()
#
#for x in myresult:
#    print(x)

#mycursor = mydb.cursor()
#
#sql = "SELECT * FROM customers WHERE address = %s"
#adr = ("Yellow Garden 2", )
#
#mycursor.execute(sql, adr)
#
#myresult = mycursor.fetchall()
#
#for x in myresult:
#  print(x) 

#mycursor = mydb.cursor()
#
#sql = "select * from customers order by name desc"
#
#mycursor.execute(sql)
#myresult = mycursor.fetchall()
#
#for x in myresult:
#    print(x)

#mycursor = mydb.cursor()
#
#sql = "delete from customers where address = 'Mountain 21'"
#
#mycursor.execute(sql)
#mydb.commit()
#
#mycursor.execute("select * from customers")
#myresult = mycursor.fetchall()
#
#print(mycursor.rowcount, "record(s) deleted")
#for x in myresult:
#    print(x)

#mycursor = mydb.cursor()
#
#sql = "delete from customers where address = %s"
#adr = ("Yellow Garden 2", )
#mycursor.execute(sql)
#mydb.commit()
#
#mycursor.execute("select * from customers")
#
#print(mycursor.rowcount, "record(s) deleted")

#drop table
#import mysql.connector
#
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685",
#    database = "latih1"
#)
#
#cursor = mydb.cursor()
#sql = "drop table customers"
# atau pake ini
#sql = "DROP TABLE IF EXISTS customers"
#cursor.execute(sql)

#import mysql.connector
#from mysql.connector.errors import MySQLFabricError
#
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685",
#    database = "latih1"
#)

#mycursor = mydb.cursor()
#sql = "update customers set address = 'Canyon 123' WHERE address #= 'Valley 345'"
#
#mycursor.execute(sql)
#mydb.commit()
#
#print(mycursor.rowcount,"record(s) affected")

#mycursor = mydb.cursor()
#
#sql = "UPDATE customers SET address = %s WHERE address = %s"
#val = ("Valley 345", "Canyon 123")
#
#mycursor.execute(sql, val)
#
#mydb.commit()
#
#(mycursor.rowcount, "record(s) affected") 

#LIMIT
#mycursor = mydb.cursor()
#mycursor.execute("select * from customers limit 5")
#
#myresult = mycursor.fetchall()
#for x in myresult:
#    print(x)

#import mysql.connector
#
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685",
#    database = "latih1"
#)
#
#mycursor = mydb.cursor()
##mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav VARCHAR(255))") 
#mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))") 
#mycursor.execute("SHOW TABLES")
#
#for x in mycursor:
#    print(x)

#import mysql.connector
#
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685",
#    database = "latih1"
#)

#kursor = mydb.cursor()
#sql = "insert into users (id,name,fav) values (%s, %s, %s)"
#val = [
#     ('1', 'John', '154'),
#     ('2', 'Peter','154'),
#     ('3', 'Amy', '155'),
#     ('4', 'Hannah',''),
#     ('5', 'Michael','')
#]
#kursor.executemany(sql,val)
#mydb.commit()
#
#print(kursor.rowcount, "was inserted")

#kursor = mydb.cursor()
#sql = "insert into products (id,name) values (%s, %s)"
#val = [
#     ('154', 'Chocolate Heaven'),
#     ('155', 'Tasty Lemons'),
#     ('156', 'Vanilla Dreams')
#]
#kursor.executemany(sql,val)
#mydb.commit()
#
#print(kursor.rowcount, "was inserted")

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Fadeelah9685",
    database = "latih1"
)

kursor = mydb.cursor()
sql = "select \
    users.name as user, \
    products.name as favorite \
    from users \
    right join products on users.fav = products.id" #inner,left,right

kursor.execute(sql)
myresult = kursor.fetchall()

for x in myresult:
    print(x)

