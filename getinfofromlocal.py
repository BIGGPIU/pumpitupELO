
#OL,VH,H,M,E,NR
#ok I think im just gonna make a new yandev file
f = open("tierlistsnapshot.txt","r")
dicts = {
    "15":"",
    "16":"",
    "17":"",
    "18":"",
    "19":"",
    "20":"",
    "21":"",
    "22":"",
    "23":"",
    "24":"",
    "25":"",
    "26":"",
}
file = []
while True:
    i = 0
    x = 15
    try:
        if len(str(f"{i/7}")) != 1:
            dicts[f"{x}"]+=file(i)
            print (i)
        else:
            x+=1
            print (i)
            print (x)
    except:
        break


try:
    while True:
        file.append(f.readline)
except:
    pass
class DIFF:
    def __init__(self,diff):
        self.OL = file[diff] # if diff == 1 it will return 1
        self.VH = file[diff] # if diff == 2 
        pass


def get(string):
    return string[:2]