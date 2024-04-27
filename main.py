import requests
import os
from yandev import skimjson
from gettierlist import getTL
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

class DIFF:
    hold2 = ["OL","VH","H","M","E","NR"]
    def __init__(self,x): #overleveled,veryhard,hard,medium,easy,notrated
        if x != 27:
            hold = getTL(x,modes[0])
            hold2 = getTL(x,modes[1])
            self.OL = hold[0] + hold2[0]
            self.VH = hold[1] + hold2[1]
            self.H = hold[2] + hold2[2]
            self.M = hold[3] + hold2[3]
            self.E = hold[4] + hold2[4]
            self.NR = hold[5] + hold2[5]
        else:
            hold2 = getTL(x,modes[1])
            self.OL = hold2[0]
            self.VH = hold2[1]
            self.H = hold2[2]
            self.M = hold2[3]
            self.E = hold2[4]
            self.NR = hold2[5]
    def getvalues(self,VALUE):
        return self.hold2[VALUE]


def things():
    fifteen = []
    sixteen = []
    seventeen = []
    eighteen = []
    nineteen = []
    twenty = []
    twentyone = []
    twentytwo = []
    twentythree = []
    twentyfour = []
    twentyfive = []
    twentysix = []
    twentyseven = []
    twentyeight = []
    values = {}
    x=15
    z=0
    y=0
    while True:
            if x == 15: #lord we gotta do better
                hold = DIFF(x)
                fifteen = fifteen.append(f"{hold.OL}")
                fifteen = fifteen.append(hold.VH)
                fifteen = fifteen.append(hold.H)
                fifteen = fifteen.append(hold.M)
                fifteen = fifteen.append(hold.E)
                fifteen = fifteen.append(hold.NR)
                x+=1
                y+=1
            else:
                break
    print (fifteen)

if __name__ == "__main__":
    main()
    things()