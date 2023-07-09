#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


# In[2]:


def convert_to_decimal(coordinate):
    degrees, minutes = coordinate.split('°')[0], coordinate.split('°')[1].split('′')[0]
    if '″' in coordinate:
        seconds = coordinate.split('′')[1].split('″')[0]
    else:
        seconds = 0
    decimal_value = int(degrees) + (int(minutes) / 60) + (int(seconds) / 3600)
    return decimal_value


# In[3]:


def webscrape_wiki(list_of_cities):
  list_for_df = []

  for city in list_of_cities:

    url = "https://en.wikipedia.org/wiki/" + city

    headers = {'Accept-Language': 'en-US,en;q=0.8'}
    response = requests.get(url, headers = headers)

    wiki_soup = BeautifulSoup(response.content, "html.parser")

    response_dict = {}

    response_dict["city"] = wiki_soup.select("span.mw-page-title-main")[0].getText()
    response_dict["country"] = wiki_soup.select("table.infobox td.infobox-data")[0].getText()
    response_dict["latitude"] = wiki_soup.select("span.latitude")[0].getText()
    for key in ['latitude']:
      # Convert degrees, minutes, and seconds to decimal format
      response_dict["latitude"] = convert_to_decimal(response_dict[key])
    response_dict["longitude"] = wiki_soup.select("span.longitude")[0].getText()
    for key in ['longitude']:
      # Convert degrees, minutes, and seconds to decimal format
      response_dict["longitude"] = convert_to_decimal(response_dict[key])
    if wiki_soup.select_one('th.infobox-header:-soup-contains("Population")'):
      response_dict["population"] = wiki_soup.select_one('th.infobox-header:-soup-contains("Population")').parent.find_next_sibling().find(text=re.compile(r'\d+'))

    list_for_df.append(response_dict)

    cities_df = pd.DataFrame(list_for_df)


  return  cities_df


# In[4]:


list_of_cities = ["Berlin", "Hamburg", "Leipzig", "Frankfurt", "Munich", "Stuttgart", "Hanover"]


# In[5]:


Cities_data_df = webscrape_wiki(list_of_cities)


# In[9]:


Cities_data_df 


# # SQLAlchemy

# In[11]:


import sqlalchemy # install if needed


# Specify MySQL connection. You need to previously create the schema (also called database in MySQL) `iss_workshop` on your local instance of MySQL. 
# 
# You can do that with MySQLWorkbench by connecting to your local instance and typing `CREATE DATABASE iss_workshop;` in a new query tab.

# In[10]:


schema="sql_combined_scraped_cities_data_asim" # renamed from "iss_workshop"
host="127.0.0.1"
user="root"
password="Your_sql_Password"
port=3306
con = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'


# Use pandas method `to_sql` with the argument `if_exists=append` to create the table (only the first time we run it) and insert the new rows into it.

# In[14]:


Cities_data_df .to_sql('cities_wiki_data', # renamed from "iss_position"
              if_exists='append', 
              con=con, 
              index=False)


# In[ ]:


#selected_columns = ['column1', 'column2', 'column3']
#df[selected_columns].to_sql('table_name', engine, index=False, if_exists='replace')


# Check on MySQLWorkbench that a new table `iss_position` exists within the `iss_workshop` database, and that a new row has been inserted on it. If you run the whole notebook again, another row should appear there.
