# in the container python py
import requests
import logging
from bs4 import BeautifulSoup
import unidecode
import unicodedata  # to get rid of xa0 in the string in python
# from unidecode import unidecode

logging.basicConfig(filename='scraper.log', 
                    level=logging.INFO, 
                    format=f'%(asctime)s - %(name)s - %(threadName)s - %(message)s')


URL = 'https://fr.indeed.com/jobs?q=developpeur+alternance&l=%C3%8Ele-de-France'

try:
    response = requests.get(URL)
# except requests.exceptions.ConnectionError:
except Exception as e:
    logging.info(f"failed to access url, error {e}")


soup = BeautifulSoup(response.content, 'html.parser')
    #response.text, 'html.parser')
results = soup.find(id='resultsCol')
a_links = results.find_all('a', class_ = 'jobtitle turnstileLink')
divs = results.find_all('div', class_ = 'jobsearch-SerpJobCard')

title_list = []
locations_list = []
date_lists = []
href_list = []
company_list = []
summary_list = []
salary_list = []

def find_salary():

    logging.info("getting salaries: start")
    try:
        salaries = results.find_all('span', class_ = "salaryText")
        print(f'SALARIES ############################################## {salaries}')
        for salary in salaries:
            print(f"ONE SALARY ######################################## {salary}")
            salary = salary.text.strip()
            salary = unicodedata.normalize("NFKD", salary)
            # https://stackoverflow.com/questions/10993612/how-to-remove-xa0-from-string-in-python    
            salary_list.append(salary)
    except:
        salaries = " "

    return salary_list
    logging.info("getting salaries: end")


def find_and_store_links():
    logging.info("getting job links: start")

    for link in a_links:
        href = link.get('href')
        href = "https://indeed.fr" + href
        href_list.append(href)


def find_companies():
    logging.info("getting company names: start")

    companies = results.find_all('span', class_ = 'company')
    for company in companies:
        text = company.getText()
        text2 = text.strip()
        company_list.append(text2)
    return company_list

    logging.info("getting company names: end")


def find_and_store_titles():
    logging.info("getting job titles: start")
    for title in a_links:
        title = title.get('title')
        # unidecodizer = unidecode.unidecode(title)
        # title_list.append(unidecodizer)
        title_list.append(title)
    

    try:
        for i in title_list:
            print(i)
            if len(i.split(" - ")) == 2:
                unaccented_string = unidecode.unidecode(i)
                title_list.append(unaccented_string.split(" - ")[0])
                return title_list
    except Exception as e:
        logging.error(f"Error, type: {e}")

    logging.info("getting job links: end")


def find_locations():

    logging.info("getting job location: start")
    locations = results.find_all(['div', 'span'], {'class': 'location'})
    for location in locations:
        locations_list.append(location.text)
    return locations_list

    logging.info("getting job location: end")


def date_when_posted():

    logging.info("getting date when posted: start")
    date_result = results.findAll('span', {'class': 'date'})
    for date in date_result:
        date_lists.append(date.text)
    return date_lists

    logging.info("getting date when posted: end")


company_var = find_companies()
links_var = find_and_store_links()
titles_var = find_and_store_titles()
locations_var = find_locations()
dates_var = date_when_posted()
salary_var = find_salary()


# print(f"COMPANIES : {company_list}")
# print(f"URLS: {href_list}")
# print(f"TITLES: {title_list}")
# print(f"LOCATIONS: {locations_list}")
# print(f"DATES: {date_lists}")
# print(f"SALARIES: {salary_list}")


big_list = list(zip( title_list, company_list, locations_list, salary_list, date_lists, href_list))
print(f"PRINTING BIG LIST: {big_list}")