import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="jkdatabase"
)

# print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE jkdatabase")

# mycursor.execute("CREATE TABLE Users (id INT, name VARCHAR(300))")

# sql = "INSERT INTO users(id,name) VALUES (%s,%s)"
# val = [
#     (1,'ama'),
#     (2,'nii'),
#     (3,'kofi'),
#     (4,'adjoa')
# ]
# mycursor.executemany(sql,val)

# mydb.commit()

# print(mycursor.rowcount,"data was inserted ")


# sql= "SELECT* FROM Users ORDER BY id"

# mycursor.execute(sql)
# myresult= mycursor.fetchall()

# for user in myresult:
#     print(user)

# print(mycursor.execute("DROP TABLE Users"))

# print(mycursor.rowcount,'table was deleted')

# mycursor.execute("CREATE TABLE person (id INT, name VARCHAR(300))")

# mycursor.execute('DROP TABLE person')

