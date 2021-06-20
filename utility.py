from bs4 import BeautifulSoup
import pandas as pd

#for getting house details from source code
def get_house_data(page_source,filename="output.xlsx"):
    soup=BeautifulSoup(page_source,'html5lib')
    soup=soup.find_all('div',attrs={'class':'filter-property-list detailurl'})
    flat_list=[]
    for s in soup:
        heading_html = s.find('h1',attrs={'class':'filter-pro-heading'})
        heading = heading_html.find(text=True, recursive=False) 
        place= s.find('span').text
        price=s.find('span',attrs={'class':'price'}).text
        price_per_unit=s.find('span',attrs={'class':'price-per-unit'}).text
        details_div=s.find('div',attrs={'class':'row filter-pro-details'})
        area=details_div.find('div',attrs={'class':'col-4'}).find(text=True, recursive=False)
        area_unit=details_div.find('div',attrs={'class':'col-4'}).find('span',attrs={'class':'inline'}).text
        facing=details_div.find('div',attrs={'class':'col-3'}).find(text=True, recursive=False)
        status=details_div.find('div',attrs={'class':'col-5'}).find(text=True, recursive=False)
        prolist=s.find('ul',attrs={'class':'pro-list'}).find_all('li')
        owner=s.find('span',attrs={'class':'owner-name'}).text
        posted=s.find('span',attrs={'class':'owner-post'}).text[8:]
        pros=''
        for item in prolist:
            pros+=item.text+'\n'
        data=(heading,place,price,price_per_unit,area+area_unit,status,facing,pros,owner,posted)
        flat_list.append(data)
    columns=['Heading','Place','Price','Price_per_unit','Area','Status','Facing','Pros','Owner','Posted']
    df = pd.DataFrame(flat_list, columns = columns)
    df.to_excel(filename)