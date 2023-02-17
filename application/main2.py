from selenium import webdriver
from selenium.webdriver.common.by import By 

def return_title():
  driver = webdriver.Chrome()

  driver.get("https://www.reddit.com/")
  title_of_driver = driver.title 
  print(title_of_driver)
  driver.close()

  return title_of_driver


if __name__ == "__main__":
    return_title()