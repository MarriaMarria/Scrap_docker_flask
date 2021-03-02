import mysql.connector
import logging
import json

logging.basicConfig(filename='mydb.log', 
                    level=logging.INFO, 
                    format=f'%(asctime)s - %(name)s - %(threadName)s - %(message)s')

# logging.info("connecting to my DB")   
mydb = mysql.connector.connect(

    host="ms",
    database="scraping_DB",
    user="root",
    password="password",
    # auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()


def create_table():

    try:
        logging.info("creating table")
        mycursor.execute("CREATE TABLE IF NOT EXISTS Job_Offers \
            (id INT PRIMARY KEY AUTO_INCREMENT, scraped TIMESTAMP default NOW(), title VARCHAR(100),\
            company VARCHAR(100), location VARCHAR(100), \
            salary VARCHAR(100), date_published VARCHAR(100), more_info TEXT)")
        mydb.commit()
    except Exception as e:
        logging.info(f"There is an error, code {e}")


def insert_data(mydata):

    try:
        logging.info("inserting to the table")
        query = "INSERT INTO Job_Offers (title, company, location, salary, date_published, more_info) VALUES (%s, %s, %s, %s, %s, %s)"
        args = mydata
        # print(f"Printing {query}")
        # print(f"Printing {args}")
        mycursor.executemany(query, args)
        mydb.commit()

    except Exception as e:
        logging.info(f"Couldn't insert into table, error code is: {e}")


        mydb.close()

    # mycursor.execute("Select * From Job_Offers")
    # result = mycursor.fetchall()
    # with open(job_offers.json, mode="a+") as file: 
    #     json.dump(result.json(), file) 





######################################################################
# doesn't work


# def save_search():

#     try:
#         mycursor.execute("SELECT title, scraped, date_published FROM Job_Offers")
#         result = mycursor.fetchall()
#         print(f"PRINTING RESULT OF SAVE_SEARCH: {result}")
#         mydb.commit()
#         mydb.close()


#         with open(test.csv, mode="w", newline='') as f: 
#             csv_writer = csv.writer(f, delimiter=';')
#             csv_writer.writerow([result])

#     except Exception as e:
#         logging.info(f"Could not save csv, error : {e}")




# def save_search():

#     try:
#         mycursor.execute("SELECT title, date_published FROM Job_Offers\
#                     INTO OUTFILE 'job_offers.txt'")
#         mydb.commit()
#         mydb.close()
#     except Exception as e:
#         logging.info(f"Could not save csv, error : {e}")


# save_search()

# SELECT order_id,product_name,qty
# FROM orders
# WHERE foo = 'bar'
# INTO OUTFILE '/var/lib/mysql-files/orders.csv'
# FIELDS TERMINATED BY ','
# ENCLOSED BY '"'
# LINES TERMINATED BY '\n';





# ALTER TABLE table
# ADD [COLUMN] column_name column_definition [FIRST|AFTER existing_column];

