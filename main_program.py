import pandas as pd
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import numpy as np

"""
As my current expertise has not been particularly in the field of web scraping, to display my data processing and analysis skills, I have taken some sample data to do the remaining tasks
"""

### Data Processing


gst_rates = pd.read_csv("gst_rates.csv")
products = pd.read_csv("products.csv")

merged_df = pd.merge(products,gst_rates,on="Category")
products['GST_amount'] = merged_df['Price']*merged_df['Rate']/100


### Data Analysis

#average of gst_rates across categories
print("--------")
print("Average")
print(products.groupby("Category")["GST_amount"].mean())


#max gst rate in each category
print("--------")
print("Maximum GST amount")
print(products.groupby("Category")["GST_amount"].max())
print("--------")




### Web Scraping ###
"""
link1 = "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_nav_0"
# link2 = "https://www.flipkart.com/offers-list/content?screen=dynamic&pk=themeViews%3DDOTD%3Aviewalldesktop~widgetType%3DdealCard~contentType%3Dneo&wid=2.dealCard.OMU&fm=neo%2Fmerchandising&iid=M_c6c0d41e-e415-492c-ba12-cc384a0316a5_1_372UD5BXDFYS_MC.G6ZC4RAJ9OHU&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Top%2BOffers_G6ZC4RAJ9OHU&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L0_view-all&cid=G6ZC4RAJ9OHU"

html_doc = requests.get(link1)
soup = BeautifulSoup(html_doc.text, 'html.parser')

# tag_type="ol"
# class_name = "a-carousel"

# print(soup.descendant.find('ol'))
# print([i for i in soup['a-page'].contents if 'carousel' in i])
# for child in soup.descendants:
#     print(child)
# print(soup.find_all("div", {"id": "anonCarousel1"}))
# print(soup.find('ol'))
# for child in soup.children:
#     print(child.find_all("div", {"class": "a-carousel-viewport"}))
# # pprint(all_objects)
# # for s in all_objects.find_all('img',alt=True):
#     # print(s)


"""