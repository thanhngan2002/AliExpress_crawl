from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

import undetected_chromedriver as uc
options = uc.ChromeOptions()
# options.headless=True
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('start-maximized')
options.accept_untrusted_certs = True # Here
driver = uc.Chrome(options=options)

product_links = []
# Crawl sản phẩm trong 20 trang đầu tiên
# url = 'https://www.aliexpress.com/p/calp-plus/index.html?spm=a2g0o.home.category.2.5f5d2145iDrDzL&categoryTab=jewelry_%2526_watches'




# Thực hiện cuộn xuống cuối trang bằng JavaScript
for i in range(1):
    url_category_page = 'https://www.aliexpress.com/w/wholesale-Mechanical-Watches.html?isFromCategory=y&categoryUrlParams=%7B%22q%22%3A%22Mechanical+Watches%22%2C%22s%22%3A%22qp_nw%22%2C%22osf%22%3A%22category_navigate%22%2C%22sg_search_params%22%3A%22on___%2528%2520prism_tag_id%253A%25271000554757%2527%2520%2529%22%2C%22guide_trace%22%3A%226d773ba7-dcd6-47ab-bb9a-4dedf783d467%22%2C%22scene_id%22%3A%2232124%22%2C%22searchBizScene%22%3A%22openSearch%22%2C%22recog_lang%22%3A%22en%22%2C%22bizScene%22%3A%22category_navigate%22%2C%22guideModule%22%3A%22category_navigate_vertical%22%2C%22postCatIds%22%3A%2236%2C1511%2C44%22%2C%22scene%22%3A%22category_navigate%22%7D&page='+str(i)+'&g=y&SearchText=Mechanical+Watches'
    driver.get(url_category_page)
    
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(7)  # Nghỉ 30s để tránh bị chặn API 

links = driver.find_elements(By.CSS_SELECTOR, ".list--galleryWrapper--29HRJT4 .search-card-item")  # Vị trí chứa đường dẫn sản phẩm
print(links[0].get_attribute("href"))

name = driver.find_elements(By.CSS_SELECTOR, '.list--galleryWrapper--29HRJT4 .search-card-item .multi--title--G7dOCj3')
print(name[0].get_attribute("title"))

price = driver.find_element(By.CSS_SELECTOR, '.list--galleryWrapper--29HRJT4 .search-card-item .multi--price-original--1zEQqOK span')
print(price.text)

## save
pd.DataFrames()
