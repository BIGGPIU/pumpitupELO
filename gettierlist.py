import requests
from bs4 import BeautifulSoup 
from time import sleep
from selenium import webdriver

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
driver.get("https://google.co.in") #this is a test I am just committing this so I can work on it between computers.