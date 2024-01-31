from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

planets_data = []

def scrape():
    soup = BeautifulSoup(features="html.parser")
    for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
        li_tags = ul_tag.find_all("li")
        temp_list = []
        for index, li_tag in enumerate(li_tags):
            if index == 0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")     
        planets_data.append(temp_list)


scrape()

headers = ["name", "distance", "mass", "radius"]
planet_df_1 = pd.DataFrame(planets_data,columns = headers)
planet_df_1.to_csv("scraped_data.csv",index = True, index_label = "id")