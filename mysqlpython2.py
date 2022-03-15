#import mysql.connector
#
#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685"
#)
#
#kursor = mydb.cursor()
#kursor.execute("create database latih3")
#kursor.execute("show databases")
#
#for i in kursor:
#    print(i)

#import mysql.connector
#
#db = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685",
#    database = "latih3"
#)
#
#kursor = db.cursor()
#kursor.execute("create table customers (name varchar(255), address varchar(255))")
#kursor.execute("show tables")
#
#for x in kursor:
#    print(x)

#import mysql.connector
#
#db = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    password = "Fadeelah9685",
#    database = "latih3"
#)
#kursor = db.cursor()
#kursor.execute("alter table customers add column id int auto_increment primary key")

#query = "insert into customers (name, address) values (%s,%s)"
#val = ("Arif", "Malabar")
#val = [
#  ('Peter', 'Lowstreet 4'),
#  ('Amy', 'Apple st 652'),
#  ('Hannah', 'Mountain 21'),
#  ('Michael', 'Valley 345'),
#  ('Sandy', 'Ocean blvd 2'),
#  ('Betty', 'Green Grass 1'),
#  ('Richard', 'Sky st 331'),
#  ('Susan', 'One way 98'),
#  ('Vicky', 'Yellow Garden 2'),
#  ('Ben', 'Park Lane 38'),
#  ('William', 'Central st 954'),
#  ('Chuck', 'Main Road 989'),
#  ('Viola', 'Sideway 1633')
#]
#kursor.execute(query, val)
#kursor.executemany(query, val)
#
#db.commit()
#
#print(kursor.rowcount,"record inserted")

