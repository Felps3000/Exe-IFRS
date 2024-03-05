import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456789",
  database="dados da escola"
)

mycursor = mydb.cursor()