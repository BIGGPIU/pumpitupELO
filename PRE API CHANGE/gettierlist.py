import requests
from bs4 import BeautifulSoup 
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
ONELEVELOVER=[]
VERYHARD=[]
HARD=[]
MEDIUM=[]
EASY=[]
NR=[]#NR stands for not rated
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






def Find(string):
 
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]

def getTL(DIFF,MODE):
    ONELEVELOVER=[]
    VERYHARD=[]
    HARD=[]
    MEDIUM=[]
    EASY=[]
    NR=[]#NR stands for not rated
    driver = webdriver.Firefox()
    driver.get(f"https://piuscores.arroweclip.se/TierLists?Difficulty={DIFF}&ChartType={MODE}") #this is a test I am just committing this so I can work on it between computers.
    driver.implicitly_wait(10)
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"div.mud-grid:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)"))
    )
    if element != (""):
        x=0
        piulinks = []
        y = 0
        htmlsource = driver.page_source
        htmlsource = htmlsource.replace(">",">\n")
        htmlsource = htmlsource.replace("<!--!-->","\n")
        f = open("tierlistHTML.txt","w")
        hold = htmlsource.replace("\U0001f5d9","")
        hold2 = Find(hold)
        f.write(f"{hold} \n \n {hold2}")
        f.close
        while True:
            try:
                if "piuimages" in hold2[x]:
                    piulinks.append(hold2[x])
                    x+=1
                else:
                    x+=1
            except:
                break
        f = open("tierlistHTML.txt","r")
        #print (piulinks)
        while True:
            y+=1
            line = f.readline()
            #print (line)
            hold3 = Find(line)
            hold3 = str(hold3)
            hold3 = hold3.replace("[]","")
            if  hold3 != "":
                if y >= 1765 and 1864 >= y:
                    ONELEVELOVER = ONELEVELOVER + [hold3]

                if y >= 1865 and 3482 >= y:
                    VERYHARD = VERYHARD + [hold3]

                if y >= 3493 and 6101 >= y:
                    HARD = HARD + [hold3]

                if y >= 6102 and 7160 >= y:
                    MEDIUM = MEDIUM + [hold3]

                if y >= 7161 and 7709 >= y:
                    EASY = EASY + [hold3]
                
                if y >= 7710 and 8069 >= y:
                    NR = NR + [hold3]

            if not line:
                #print (f"\n{ONELEVELOVER}\n")
                #print (f"\n{VERYHARD}\n")
                #print (f"\n{HARD}\n")
                #print (f"\n{MEDIUM}\n")
                #print (f"\n{EASY}\n")
                #print (f"\n{NR}\n") 
                break
            #print (f"Line {y} {line}")
    return ONELEVELOVER,VERYHARD,HARD,MEDIUM,EASY,NR

