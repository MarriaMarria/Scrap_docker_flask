from mydb import *

mydb = mysql.connector.connect(

    host="ms",
    database="scraping_DB",
    user="root",
    password="password",
    # auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

# difference du temps

def find_doubles():

    try:
        logging.info("finding doubles")
        mycursor.execute("SELECT * FROM Job_Offers WHERE scraped >= DATE_SUB(NOW(),INTERVAL 20 MINUTE);") 
        mydb.commit()
    except Exception as e:
        logging.info(f"There is an error, code {e}")




def delete_dubles():

    try:
        logging.info("deleting doubles")
        mycursor.execute("DELETE FROM Job_Offers WHERE id NOT IN (SELECT * FROM (SELECT MAX(id) FROM Job_Offers GROUP BY scraped);")
        mydb.commit()
    except Exception as e:
        logging.info(f"There is an error, code {e}")   


# DELETE FROM `tablename` 
#   WHERE id NOT IN (
#     SELECT * FROM (
#       SELECT MAX(id) FROM tablename 
#         GROUP BY name
#     ) 
#   )

#   "DELETE FROM mirror WHERE id NOT IN (SELECT * 
#   FROM (SELECT MIN(id) FROM mirror GROUP BY 
#   mirror_description, mirror_price, mirror_named) 
#   as mirror_duplicate)"