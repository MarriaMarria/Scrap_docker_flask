# in the container python py
import requests
import logging
from bs4 import BeautifulSoup
import unicodedata # to get rid of xa0 in the string in python

logging.basicConfig(filename='scraper.log', 
                    level=logging.INFO, 
                    format=f'%(asctime)s - %(name)s - %(threadName)s - %(message)s')


URL = 'https://fr.indeed.com/jobs?q=developpeur+web&l=%C3%8Ele-de-France'

try:
    response = requests.get(URL)
except requests.exceptions.ConnectionError:
    logging.info("failed to access url")


soup = BeautifulSoup(response.content.decode('utf-8','ignore'),"lxml")
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
        for salary in salaries:
            salary = salary.text.strip()
            salary = unicodedata.normalize("NFKD", salary)

            # https://stackoverflow.com/questions/10993612/how-to-remove-xa0-from-string-in-python
            
            salary_list.append(salary)
    except:
        salaries = " "

    return salary_list
    logging.info("getting salaries: start")



def find_summary():

    logging.info("getting summaries: start")
    summaries = results.find_all('div', class_ = "summary")
    for summary in summaries:
        summary_list.append(summary.text.strip())
    return summary_list
    logging.info("getting summaries: end")


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
        title_list.append(title)
    return title_list

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
summary_var = find_summary()
salary_var = find_salary()

big_list = list(zip( title_list, company_list, locations_list, salary_list, date_lists, href_list, summary_list))

# print(company_var)
# print(links_var)
# print(titles_var)
# print(locations_var)
# print(dates_var)
# print(summary_var)
# print(salary_var)