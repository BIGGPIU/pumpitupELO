from gettierlist import getTL
modes = ["Single","Double"]

class DIFF:
    hold2 = ["OL","VH","H","M","E","NR"]
    def __init__(self,x): #overleveled,veryhard,hard,medium,easy,notrated
        if x != 27:
            hold = getTL(x,modes[0])
            hold2 = getTL(x,modes[1])
            self.OL = str(hold[0]) + str(hold2[0])
            self.VH = str(hold[1]) + str(hold2[1])
            self.H = str(hold[2]) + str(hold2[2])
            self.M = str(hold[3]) + str(hold2[3])
            self.E = str(hold[4]) + str(hold2[4])
            self.NR = str(hold[5]) + str(hold2[5])
        if x == 28:
            hold2 = getTL(x,modes[1])
            self.OL = hold2[0]
            self.VH = hold2[1]
            self.H = hold2[2]
            self.M = hold2[3]
            self.E = hold2[4]
            self.NR = hold2[5]
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
                print (hold.OL)
                fifteen.append(f"{hold.OL}")
                fifteen.append(hold.VH)
                fifteen.append(hold.H)
                fifteen.append(hold.M)
                fifteen.append(hold.E)
                fifteen.append(hold.NR)
                x+=1
                y+=1
            if x == 16: #this is some yandev ass code but Idc
                hold = DIFF(x)
                print (hold.OL)
                sixteen.append(f"{hold.OL}")
                sixteen.append(hold.VH)
                sixteen.append(hold.H)
                sixteen.append(hold.M)
                sixteen.append(hold.E)
                sixteen.append(hold.NR)
                x+=1
                y+=1
            if x == 17: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                seventeen.append(f"{hold.OL}")
                seventeen.append(hold.VH)
                seventeen.append(hold.H)
                seventeen.append(hold.M)
                seventeen.append(hold.E)
                seventeen.append(hold.NR)
                x+=1
                y+=1
            if x == 18: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                eighteen.append(f"{hold.OL}")
                eighteen.append(hold.VH)
                eighteen.append(hold.H)
                eighteen.append(hold.M)
                eighteen.append(hold.E)
                eighteen.append(hold.NR)
                x+=1
                y+=1
            if x == 19: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                nineteen.append(f"{hold.OL}")
                nineteen.append(hold.VH)
                nineteen.append(hold.H)
                nineteen.append(hold.M)
                nineteen.append(hold.E)
                nineteen.append(hold.NR)
                x+=1
                y+=1
            if x == 20: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twenty.append(f"{hold.OL}")
                twenty.append(hold.VH)
                twenty.append(hold.H)
                twenty.append(hold.M)
                twenty.append(hold.E)
                twenty.append(hold.NR)
                x+=1
                y+=1
            if x == 21: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twentyone.append(f"{hold.OL}")
                twentyone.append(hold.VH)
                twentyone.append(hold.H)
                twentyone.append(hold.M)
                twentyone.append(hold.E)
                twentyone.append(hold.NR)
                x+=1
                y+=1
            if x == 22: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twentytwo.append(f"{hold.OL}")
                twentytwo.append(hold.VH)
                twentytwo.append(hold.H)
                twentytwo.append(hold.M)
                twentytwo.append(hold.E)
                twentytwo.append(hold.NR)
                x+=1
                y+=1
            if x == 23: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twentythree.append(f"{hold.OL}")
                twentythree.append(hold.VH)
                twentythree.append(hold.H)
                twentythree.append(hold.M)
                twentythree.append(hold.E)
                twentythree.append(hold.NR)
                x+=1
                y+=1
            if x == 24: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twentyfour.append(f"{hold.OL}")
                twentyfour.append(hold.VH)
                twentyfour.append(hold.H)
                twentyfour.append(hold.M)
                twentyfour.append(hold.E)
                twentyfour.append(hold.NR)
                x+=1
                y+=1
            if x == 25: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x) # I forgot to get rid of the comment before I copied it :skull:
                print (hold.OL)
                twentyfive.append(f"{hold.OL}")
                twentyfive.append(hold.VH)
                twentyfive.append(hold.H)
                twentyfive.append(hold.M)
                twentyfive.append(hold.E)
                twentyfive.append(hold.NR)
                x+=1
                y+=1
            if x == 26: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twentysix.append(f"{hold.OL}")
                twentysix.append(hold.VH)
                twentysix.append(hold.H)
                twentysix.append(hold.M)
                twentysix.append(hold.E)
                twentysix.append(hold.NR)
                x+=1
                y+=1
            if x == 27: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twentyseven.append(f"{hold.OL}")
                twentyseven.append(hold.VH)
                twentyseven.append(hold.H)
                twentyseven.append(hold.M)
                twentyseven.append(hold.E)
                twentyseven.append(hold.NR)
                x+=1
                y+=1
            if x == 28: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twentyeight.append(f"{hold.OL}")
                twentyeight.append(hold.VH)
                twentyeight.append(hold.H)
                twentyeight.append(hold.M)
                twentyeight.append(hold.E)
                twentyeight.append(hold.NR)
                x+=1
                y+=1
            else: 
                break
    print (fifteen)
    return fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twentyone, twentytwo, twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight