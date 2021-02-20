import mysql.connector

mydb = mysql.connector.connect(
    host="ms",
    database="scraping_DB",
    user="root",
    password="password"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS Job_Offers4 (id INT PRIMARY KEY AUTO_INCREMENT, company VARCHAR(150), more_info TEXT, title VARCHAR(150), location VARCHAR(150), date_published VARCHAR(150))")
mydb.commit()

def insert_data(mydata):
    query = "INSERT INTO Job_Offers4 (company, more_info, title, location, date_published) VALUES (%s, %s, %s, %s, %s)"
    args = mydata

    mycursor.executemany(query, args)
    mydb.commit()
