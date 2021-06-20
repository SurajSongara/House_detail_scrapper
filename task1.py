from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utility import get_house_data
import time



chrome_options = Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=chrome_options)
# driver=webdriver.Chrome()
url='https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi'
driver.get(url)

old_height=driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height=driver.execute_script('return document.body.scrollHeight')
    if old_height==new_height:
        break
    old_height=new_height
    

page_source=driver.page_source

print("getting data")
get_house_data(page_source=page_source,filename="output1.xlsx")




