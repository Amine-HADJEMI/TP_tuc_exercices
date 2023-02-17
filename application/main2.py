from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options

def return_title():
  chrome_options = Options()
  chrome_options.add_argument('--headless') 

  driver = webdriver.Chrome(options=chrome_options)

  driver.get("https://www.reddit.com/")
  title_of_driver = driver.title 
  print(title_of_driver)
  driver.close()

  return title_of_driver

return_title()