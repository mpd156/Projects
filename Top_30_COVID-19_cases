import pandas as pd 
import requests 
from bs4 import BeautifulSoup 


wikipageurl="https://en.m.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory"
geturl=requests.get(wikipageurl) #requests to import/get the wikipage url



soup = BeautifulSoup(geturl.text, 'html.parser') #use of BeautifulSoup to parse the html
cumulativetable=soup.find('table',{'class':"wikitable sortable tpl-blanktable covid19-countrynames"}) #Beautifulsoup to import the table with class/table tag
covid_data=pd.read_html(str(cumulativetable)) #read the html/class


covid_data=pd.DataFrame(covid_data[0]) #This is needed to help frame the data chart from wiki into the output. / make dataframe using pandas
print(covid_data.head(31)) #This will print the top 30 countries with the most COVID-19 cases/deaths according to December 1, 2021.
#The output chart will update whenever the wikipedia page chart updates with the n

