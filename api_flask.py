# in the container python FLASK fl
from flask import Flask, render_template, request, redirect, jsonify
from mydb import mydb, mycursor
##connection to my DB + requests to


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello you'


# search by city

@app.route('/search/<city>')
def search_by_city(city):
    mycursor.execute(f"SELECT title FROM Job_Offers4 WHERE location = '{city}'")
    # SELECT title FROM Job_Offers4 WHERE location = 'Paris (75)' // on met dans l'URL Paris (75)
    result = mycursor.fetchall()
    return jsonify(result)

# all info
@app.route('/')
def choose_all():

    mycursor.execute("Select * From Job_Offers4")
    result = mycursor.fetchall()
    return jsonify(result)

# all titles
@app.route('/search/title')
def search_by_title():

    mycursor.execute("SELECT title FROM Job_Offers4")
    result = mycursor.fetchall()
    return jsonify(result)

# search by order published 
@app.route('/search/date')
def search_date():

    mycursor.execute("Select * From Job_Offers4 ORDER BY date_published")
    result = mycursor.fetchall()
    return jsonify(result)


# #search with a string DOESN'T WORK
# @app.route('search/word/<word>')
# def search_by_word(word):

#     # # mycursor.execute(f'SELECT * FROM Job_Offers4 WHERE title LIKE "%{word};%"')
#     result = mycursor.fetchall()
#     return jsonify(result)

# @app.route('search/test')
# def test_search():
#     city = requests.args.get('city')

#     return '''<h1>The city you are searching for a job at is {}'''.format(city)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3050, debug=True)