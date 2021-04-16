#import Libraries
import dash_html_components as html
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as mp

#Requests
def web_scrapping():
    url = "https://www.worldometers.info/coronavirus/#countries"
    page = requests.get(url).text

    # extract table and parse

    soup = BeautifulSoup(page, "lxml")  # lxml process xml and html in python language
    table = soup.find("table", id="main_table_countries_today")
    table_data = table.tbody.find_all("tr")
    #country names
    dic = {}
    for i in range(len(table_data)):
        try:
            key = (table_data[i].find_all('td')[0].string)
        except:
            key = (table_data[i].find_all('a', href=True)[0].string)

        #country values
        value = [j.string for j in table_data[i].find_all('td')]
        dic[key] = value  # baraye in be dictionary tabdil kardim ke rahatar betoonim be dataframe tabdil konim

    column_names = ["Total Cases", "New Cases", "Total Deaths", "New Deaths", "Total Recovered", "Active",
                    "Serious Critical", "Tot Cases/1M pop", "Tot Death/1M pop", "Total tests", "Tests/1M pop"]

    df = pd.DataFrame(dic).iloc[1:, 1:].T.iloc[:, :11]
   # iloc baraye dastresi be dadehaye chand radif va sotoon
    df.index.name = "country"
    df.columns = column_names
    #csv file
    df.to_csv("Corona_virus.csv")  # baraye dorost kardan file csv be onvan khoruji
    print("OK")

web_scrapping()
