
#OL,VH,H,M,E,NR
f = open("tierlistsnapshot.txt","r")
class DIFF:
    def __init__(self,x):
        while True:
            hold = f.readline()
            if get(hold) == str(x):
                self.OL = (hold)
                self.VH = f.readline()
                self.H = f.readline()
                self.M = f.readline()
                self.E = f.readline()
                self.NR = f.readline()
                break


def get(string):
    return string[:2]