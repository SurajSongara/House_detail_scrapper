from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utility import get_house_data
import time

#using selenium to load entire page

chrome_options = Options()

#if we dont want to open browser window enable chrome options
# chrome_options.add_argument("--headless")
# driver=webdriver.Chrome(options=chrome_options)

driver=webdriver.Chrome()
url='https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi'
driver.get(url)


#for loading all the house details 
old_height=driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height=driver.execute_script('return document.body.scrollHeight')
    if old_height==new_height:
        break
    old_height=new_height
    


#getting the source code 
page_source=driver.page_source

#passing the source_code and filename to get house details
get_house_data(page_source=page_source,filename="output1.xlsx")




