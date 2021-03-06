# in the container python FLASK fl
from flask import Flask, render_template, request, redirect, jsonify
from mydb import mydb, mycursor
import logging
import json

app = Flask(__name__)


logging.basicConfig(filename='api_flask.log', 
                    level=logging.INFO, 
                    format=f'%(asctime)s - %(name)s - %(threadName)s - %(message)s')


@app.route('/')
def hello():
    app.logger.info('checking homepage')
    return 'Hello you'


# search by city

@app.route('/search/<city>')
def search_by_city(city):
    app.logger.info('searching with city name: start')
    mycursor.execute(f"SELECT title FROM Job_Offers WHERE location = '{city}'")
    # SELECT title FROM Job_Offers4 WHERE location = 'Paris (75)' // on met dans l'URL Paris (75)
    result = mycursor.fetchall()
    return jsonify(result)
    app.logger.info('searching with city name: end')


@app.route('/getting_last_element')
def get_last():
    app.logger.info('searching within last 12 hours: start')
    mycursor.execute("SELECT * FROM Job_Offers WHERE scraped >= DATE_SUB(NOW(),INTERVAL 12 HOUR);") 
    result = mycursor.fetchall()
    return jsonify(result)
    app.logger.info('searching within last 12 hours: start')


# all info
@app.route('/')
def choose_all():
    app.logger.info('searching all info: start')
    mycursor.execute("Select * From Job_Offers")
    result = mycursor.fetchall()
    return jsonify(result)
    # result_json = json.dump(result)
    # print(result_json)
    app.logger.info('searching all info: end')

# all titles
@app.route('/search/title')
def search_by_title():
    app.logger.info('searching by job title: start')
    mycursor.execute("SELECT title FROM Job_Offers")
    result = mycursor.fetchall()
    return jsonify(result)
    app.logger.info('searching by job title: end')


# def write_to_file(SOME INFO):

#     now = datetime.datetime.now()
#     date_formatted = now.strftime("%Y-%m-%d %H:%M:%S") # formatting time into YMD, H:M:S

#     try:
#         with open("job_offers.txt", "a+") as myfile:
#             myfile.write('Some text' + SOME INFO from parameters + date_formatted)
#             print(f"File updated on {date_formatted}")
#     except Exception as e:
#         logging.info(f"File not written, error: {e}")


@app.route('/search/latest')
def search_date():
    app.logger.info('searching latest upfates start')
    mycursor.execute("Select * From Job_Offers ORDER BY scraped < 24 hours")
    result = mycursor.fetchall()
    return jsonify(result)
    app.logger.info('searching by date published: end')



# # search by order published 
# @app.route('/search/date')
# def search_date():
#     app.logger.info('searching by date published: start')
#     mycursor.execute("Select * From Job_Offers ORDER BY date_published ASC")
#     result = mycursor.fetchall()
#     return jsonify(result)
#     app.logger.info('searching by date published: end')



# #search with a string in title (like front, php, angular...)
@app.route('/search/word/<word>')
def search_by_word(word):
    app.logger.info('searching with a string: start')
    mycursor.execute(f'SELECT * FROM Job_Offers WHERE title LIKE "%{word}%"')
                     # SELECT * FROM Job_Offers4 WHERE title LIKE "%FRONT%";
    result = mycursor.fetchall()
    return jsonify(result)
    app.logger.info('searching with a string: end')
    


#we search like that http://localhost:4050/search/city=?Paris
@app.route('/search/city')
def city_search():
    city = request.args.get('city')
    return city
    # return '''<h1>The city you are searching for a job at is {}'''.format(city)
    # The city you are searching for a job at is None

# POSSIBLE ENDPOINTS: 
# select title, location, salary from Job_Offers where salary >= 40;
# select * from Job_Offers where title like "%python%";

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3050, debug=True) #4050