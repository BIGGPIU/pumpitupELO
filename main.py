import requests
import os
from yandev import skimjson
from gettierlist import getTL
from time import sleep
from makelocaltierlist import things
modes = ["Single","Double"]
KEY = "710a11f3-2ec6-48eb-9d51-28116672d435"
plates = ["Ultimate Game","Perfect game","Fair Game"]#I'm bored I'll do the rest later.
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
    writetxt(response.json())
    hold = readtext()
    hold2 = splt(hold)
    
    i = 0
    while i != len(hold2):
        print (hold2[i])
        i += 1


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

def splt(string):
    hold = string.split(",")
    print (hold)
    return hold 





if __name__ == "__main__":
    main()
    things()