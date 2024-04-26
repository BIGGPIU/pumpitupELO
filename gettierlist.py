import requests
from bs4 import BeautifulSoup 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#def tierlist(level,VER):
#    print ("access")
#    response = requests.get(f"https://piuscores.arroweclip.se/TierLists?Difficulty=18&ChartType=Singles")
#    soup = BeautifulSoup(response.content, 'html.parser') 
#    print(soup.prettify()) 
#    return
#
#if __name__ == "__main__":
#
#    tierlist(20,1)

driver = webdriver.Firefox()

driver.implicitly_wait(10)

driver.get("https://piuscores.arroweclip.se/TierLists?Difficulty=18&ChartType=Single") #this is a test I am just committing this so I can work on it between computers.
element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"mud-main-content"))
)
if element.text != (""):
    htmlsource = driver.page_source
    htmlsource = htmlsource.replace(">",">\n")

print (element.text)