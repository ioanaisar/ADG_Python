
import csv
import requests
from bs4 import BeautifulSoup

domain_url = 'https://allsportdb.com/Home/SportIndex'
sport = ['Sports']
folder_name = 'data/team_images'

standings = []
page = requests.get(domain_url)
soup = BeautifulSoup(page.content, features='html.parser')

table = soup.find('table', {"class": "table table-hover table-borderless"})
table_rows = table.find_all('tr')
table_rows.pop(0)

for row in table_rows:
    sports = []
    for td in row.find_all('td'):
        if td.find('a', class_='link-fav-selected text-warning') is not None:
            tex = td.text
            sports.append(tex)


    dict = {
        col: data
        for col, data in zip(sport, sports)
    }
    standings.append(dict)

with open('sports.csv', mode='w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(sports)
    csv_writer.writerows([team_data.values() for team_data in standings])