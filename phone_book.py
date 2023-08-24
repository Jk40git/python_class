import mysql.connector
import bcrypt

mydb=mysql.connector.connect(
    host= "localhost",
    user= "root",
    password="",
    database= "phonebook"
)

myCursor=mydb.cursor()

# myCursor.execute('CREATE DATABASE PHONEBOOK')

myCursor.execute('CREATE TABLE users (id INT, name VARCHAR(300), email VARCHAR(400), phonenumber INT)')

id_data=input("enter you id number :")
name_data= input("enter your name :")
email_data =input("enter your email :")
phone_number= input("enter your phone number :")

