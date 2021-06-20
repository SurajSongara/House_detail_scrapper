from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utility import get_house_data
import time



#using selenium to load entire page



#if we dont want to open browser window enable chrome options by uncommenting below two lines
# chrome_options.add_argument("--headless")
# driver=webdriver.Chrome(options=chrome_options)

driver=webdriver.Chrome()
url='https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi'
driver.get(url)
time.sleep(2)

#for selecting BHK value
driver.find_element_by_css_selector(css_selector='#navbarNavDropdown > ul.navbar-nav.mr-md-no > li.nav-item.dropdown.bedroomdropdown').click()
time.sleep(2)
driver.find_element_by_css_selector(css_selector='#navbarNavDropdown > ul.navbar-nav.mr-md-no > li.nav-item.dropdown.bedroomdropdown.show > ul > li > div > ul > li:nth-child(3) > label > span').click()
time.sleep(2)
driver.find_element_by_css_selector(css_selector='#navbarNavDropdown > ul.navbar-nav.mr-md-no > li.nav-item.dropdown.bedroomdropdown.show > ul > li > div > ul > li:nth-child(4) > label > span').click()
time.sleep(2)

#for loading entire page
old_height=driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height=driver.execute_script('return document.body.scrollHeight')
    if old_height==new_height:
        break
    old_height=new_height 

page_source=driver.page_source


#passing the source_code and filename to get house details
get_house_data(page_source=page_source,filename='output2.xlsx')