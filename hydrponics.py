from selenium import webdriver
from selenium.common import exceptions
import pandas as pd
# path of the driver in which it is installed.
browser = webdriver.Chrome('/home/faheem/PycharmProjects/scrapping_project/chromedriver_linux64/chromedriver')
browser.get('https://www.hydroponics.co.uk/online-store/fans-filters-environment/air-movement-fans?p=1')
all_product = browser.find_elements_by_css_selector('ol.products.list.items.product-items li')
#print(type(all_product))
Name = []
Price = []
i = 1
while i < 2:
    try:
        all_product = browser.find_elements_by_css_selector('ol.products.list.items.product-items li')
        for info in all_product:
            Name.append(info.find_element_by_xpath(".//div[@class='product info product-item-main']//strong").text)
            Price.append(info.find_element_by_xpath(".//div[@class='price-box price-final_price']").text)
        browser.find_elements_by_css_selector('a.action.next')
        i += 1
    except exceptions.StaleElementReferenceException:
        pass
df = pd.DataFrame(list(zip(Price, Name)), columns=['Product Price', 'Product Name'])
all_product_data = df.to_csv('hydroponics_data.csv', index=False)