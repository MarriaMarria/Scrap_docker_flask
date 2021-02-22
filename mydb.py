import mysql.connector
import logging

logging.basicConfig(filename='mydb.log', 
                    level=logging.INFO, 
                    format=f'%(asctime)s - %(name)s - %(threadName)s - %(message)s')


mydb = mysql.connector.connect(
    # logging.info("connecting to my DB")
    
    host="ms",
    database="scraping_DB",
    user="root",
    password="password"
)
mycursor = mydb.cursor()

# mycursor.execute("DROP TABLE Job_Offers")
logging.info("creating table")
mycursor.execute("CREATE TABLE IF NOT EXISTS Job_Offers (id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(100), company VARCHAR(100), location VARCHAR(100), salary VARCHAR(100), date_published VARCHAR(100), more_info TEXT, description TEXT)")
mydb.commit()

def insert_data(mydata):
    logging.info("inserting to the table")
    query = "INSERT INTO Job_Offers (title, company, location, salary, date_published, more_info, description) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    args = mydata

    mycursor.executemany(query, args)
    mydb.commit()
