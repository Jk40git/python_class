import mysql.connector
import bcrypt

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database= 'Registration' 
)

mycursor= mydb.cursor()

# mycursor.execute('CREATE DATABASE Registration')

# mycursor.execute('CREATE TABLE Users (id INT, name VARCHAR(250), email VARCHAR(300), password VARCHAR(200))')

# sql='INSERT INTO Users(id,name,email,password) VALUES(%s,%s,%s,%s)'

# val= [
#     (1, 'ama','amaka@gmail.com', '125dsdsdg'),
#     (2, 'kofi', 'kofija@yahoo.com', '454f44df4'),
#     (3, 'susu', 'susufor@hotmai.com', '5844wqqa45')
# ]

# mycursor.executemany(sql,val)

# mydb.commit()

# id_data=input("enter you id number :")
# name_data= input("enter your name :")
# email_data =input("enter your email :")
# password_data = input("enter your password :")

 
# salt = bcrypt.gensalt()
# hashed = bcrypt.hashpw(password_data.encode(), salt)

# def create_user():
#     sql="INSERT INTO users(id, name, email, password) VALUES (%s,%s,%s,%s)"
#     val = id_data,name_data,email_data,hashed
#     mycursor.execute(sql,val)

#     mydb.commit()

# create_user()

# def delete_user(num_id):
#     sql = f"DELETE FROM users WHERE id= {num_id}"
#     mycursor.execute(sql)
#     mydb.commit()

# delete_user()

# set= input("Enter your new name: ") 
# where= input(" Enter your current name: ")

# def update_user():
#     sql= "UPDATE users SET name= %s  WHERE name= %s "
#     val= set, where
#     mycursor.execute(sql,val)
#     mydb.commit()

# update_user()


# id_data=input("enter you id number: ")
# name_data= input("enter your name: ")
# email_data =input("enter your email: ")
# password_data = input("enter your password: ")

salt = bcrypt.gensalt()


class user:
    def __init__(self, id_data, name_data, email_data, password_data):
        self.id= id_data
        self.name= name_data
        self.email= email_data
        self.password= password_data  
        self.hashed = bcrypt.hashpw(password_data.encode(), salt) 

    def create_user(self):
        sql="INSERT INTO users(id, name, email, password) VALUES (%s,%s,%s,%s)"
        val = self.id, self.name,self.email,self.hashed
        mycursor.execute(sql,val)

        mydb.commit()

    def delete_user(self):
        sql = f"DELETE FROM users WHERE id= {self.id}"
        mycursor.execute(sql)
        mydb.commit()


    def update_user(self,set,where):
        sql= "UPDATE users SET name= %s  WHERE name= %s "
        val= set, where
        mycursor.execute(sql,val)
        mydb.commit()


    
        

        # if  and input_password== select:
        #     print('credential was correct, proceed')
        # else: 
        #     print("credential was wrong")

user1= user(1,'josh', 'josh25@gmail.com','fd125467')    
user1.create_user()

# user.delete_user(2)
# user()



def user_login(email,password):
    sql= "SELECT* FROM Users WHERE email=%s password=%s"
    val= (email,password)
    mycursor.execute(sql,val)
    myresult= mycursor.fetchall()
    # x=[]
    # for user in myresult:
    #     print(user[3])
    #     x.append(user[3])

    if myresult == email and password :
        print('credential was correct, proceed')
    else:
        print('credential was wrong')
   
user_login('susufor@hotmai.com','5844wqqa45')