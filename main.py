#I'm not going to lie man im so burnt out I cant do this shit right now. I'll leave this to whoever wants to do it.
#you know what instead of quitting in general I'm just going to lessen the scope of it. I'll just have it read one difficulty. 
#check out my other projects ig :/
import requests
import os
import re
from yandev import skimjson
from gettierlist import getTL
from time import sleep
from yandev2 import yandev
#from makelocaltierlist import things #you can comment this out if you dont want to remake your tierlist snapshot.
#from getinfofromlocal import DIFF
modes = ["Single","Double"]
KEY = "710a11f3-2ec6-48eb-9d51-28116672d435"
plates = ["Ultimate Game","Perfect game","Fair Game"]#I'm bored I'll do the rest later.
checkdiff = 15
try:
    f = open("temp.txt","x")
    f.close
except: 
    pass
def main():
    sheaders = {
    'accept: */*'
    'Authorization: Basic VEhFUkVJU0FCT01CU1RSQVBQRURUT01ZQ0hFU1Q6NzEwYTExZjMtMmVjNi00OGViLTlkNTEtMjgxMTY2NzJkNDM1'
}
    response = requests.get("https://piuscores.arroweclip.se/api/phoenixScores?Page=1&Count=50", headers={
    'accept':'*/*',
    'Authorization':'Basic VEhFUkVJU0FCT01CU1RSQVBQRURUT01ZQ0hFU1Q6NzEwYTExZjMtMmVjNi00OGViLTlkNTEtMjgxMTY2NzJkNDM1'
})
    #print (response.json())
    #writetxt(response.json())
    hold = readtext()
    hold = hold.replace(".jpg",".png")
    colle = hold.split(".png")
    f = open(f"{checkdiff}.txt","r")
    i = 0 
    a = f.readline()
    b = f.readline()
    c = f.readline()
    d = f.readline()
    e = f.readline()
    while i != len(colle):
        if "level: 15," in colle[i]:
            temp = re.sub(r'^.*?/songs/', '', colle[i])
            temp = temp.replace ("&quot","")
            if temp in a:
                print ("+1")
            if temp in b:
                print ("+2")
            if temp in c:
                print ("+3")
            if temp in d:
                print ("+4")
            if temp in e:
                print ("+5")    



    #print (colle[0])
    #print (colle)
    
    i = 0
    x=0 #im going to commit this to work on at home but because you're a forgetful idiot what this is going to do is pull from the list in class DIFF. every time you finish a loop this should go up by 6 (or 7-1) every time you're done with a loop
    listofdiff = ["BLANK",]
    sett = 0
    while x != 27:
        pass

#actually when I think about it I think I should just put all the difficulties in different files. I think it would make it easier to do all ts :sob:
        





def goawayihateyou(test_str):
    x=3
    split = ","
    temp = test_str.split(split)
    res = split.join(temp[:x])
    return res


def writetxt(string):
    chars = ["'","}","{",","]
    hold = str(string)
    #hold = hold.replace("☆","") #why the actual fuck does this need to be removed 
    #hold = hold.replace("{","")
    #hold = hold.replace("}","") # I cant do ts anymore, actually im going to try to do this with a list 
    #hold = hold.replace(chars,"") # I am going to kill myself
    hold2 = skimjson(hold)
    f = open("temp.txt","w")
    f = f.write(hold2)

def readtext():
    f = open("temp.txt","r")
    string = f.read()
    f.close
    return string

def splt(test_str):
    x=12
    split = ","
    temp = test_str.split(split)
    res = split.join(temp[:x])
    return res 





if __name__ == "__main__":
    main()
    try:
        things()
    except:
        pass