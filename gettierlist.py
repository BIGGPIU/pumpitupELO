import requests
from bs4 import BeautifulSoup 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

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

def Find(string):
 
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]

driver.get("https://piuscores.arroweclip.se/TierLists?Difficulty=18&ChartType=Single") #this is a test I am just committing this so I can work on it between computers.
driver.implicitly_wait(10)
element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR,"div.mud-grid:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)"))
)
if element != (""):
    x=0
    piulinks = []
    htmlsource = driver.page_source
    htmlsource = htmlsource.replace(">",">\n")
    htmlsource = htmlsource.replace("<!--!-->","\n")
    f = open("tierlistinfo.txt","w")
    hold = htmlsource.replace("\U0001f5d9","")
    hold2 = Find(hold)
    f = f.write(f"{hold} \n \n {hold2}")
    while True:
        try:
            if "piuimages" in hold2[x]:
                piulinks.append(hold2[x])
                x+=1
            else:
                x+=1
        except:
            break

    print (htmlsource)
    print (piulinks)

print (element.text)