import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user= "root",
    passwd = "password",
    database="mydatabase"
)
mycursor = mydb.cursor()

sql_command = """
                 UPDATE student
                 SET first_name = "KKP"
                 WHERE roll = 2;

 
             """
mycursor.execute(sql_command)
mydb.commit()