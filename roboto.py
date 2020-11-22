from selenium import webdriver
from selenium.webdriver.firefox.options import Options

fx = webdriver.Firefox()
fx.get("https://bandcamp.com")
fx.find_element_by_xpath(
    "/html/body/div[3]/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/a"
).click()
tracks = fx.find_elements_by_class_name("discover-item")
len(tracks)
tracks[3].click()
