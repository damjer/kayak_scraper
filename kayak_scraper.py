from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import os
import streamlit as st

st.title("Flight Price Scraper")
st.write("Showcasing scraped flight prices!")

# Display results from your scraping script
for price in lst_prices:
    st.write(price)



driver = webdriver.Chrome()
to_location = 'PAR'
url = 'https://www.kayak.ae/flights/DXB-{to_location}/2024-12-24/2024-12-31?sort=bestflight_a'.format(to_location=to_location)

driver.get(url)

flight_rows = driver.find_elements(By.XPATH, '//div[@class="nrc6-wrapper"]')

lst_prices = [] 


for WebElement in flight_rows:
    elementHTML = WebElement.get_attribute('outerHTML')
    elementSoup = BeautifulSoup(elementHTML, 'html.parser')

    temp_price = elementSoup.find("div", {"class": "nrc6-price-section"})
    price = temp_price.find("div", {"class": "f8F1-price-text"})
    lst_prices.append(price.text)
clean_prices = [price.replace('\xa0', ' ') for price in lst_prices]
print("Raw Prices: ", lst_prices)
print("Cleaned Prices: ", clean_prices)

