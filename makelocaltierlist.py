from gettierlist import getTL
import datetime
modes = ["Single","Double"]
currentday1 = datetime.datetime.now()
currentday2 = currentday1.strftime("%m %d %Y %A")

class DIFF:
    hold2 = ["OL","VH","H","M","E","NR"]
    def __init__(self,x): #overleveled,veryhard,hard,medium,easy,notrated
        if x <= 26:
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
        if x == 27:
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
    f = open("tierlistsnapshot.txt","a")
    while True:
            if x == 15: #lord we gotta do better
                hold = DIFF(x)
                print (hold.OL)
                fifteen.append(f"{hold.OL}")
                f.write (f"{x} {hold.OL}\n")
                fifteen.append(hold.VH)
                f.write (f"{x} {hold.VH}\n")
                fifteen.append(hold.H)
                f.write (f"{x} {hold.H}\n")
                fifteen.append(hold.M)
                f.write (f"{x} {hold.M}\n")
                fifteen.append(hold.E)
                f.write (f"{x} {hold.E}\n")
                fifteen.append(hold.NR)
                f.write (f"{x} {hold.NR}\n")
                x+=1
                y+=1
            if x == 16: #this is some yandev ass code but Idc
                hold = DIFF(x)
                print (hold.OL)
                sixteen.append(f"{x} {hold.OL}")
                f.write (f"{x} {hold.OL}\n")
                sixteen.append(hold.VH)
                f.write (f"{x} {hold.VH}\n")
                sixteen.append(hold.H)
                f.write (f"{x} {hold.H}\n")
                sixteen.append(hold.M)
                f.write (f"{x} {hold.M}\n")
                sixteen.append(hold.E)
                f.write (f"{x} {hold.E}\n")
                sixteen.append(hold.NR)
                f.write (f"{x} {hold.NR}\n")
                x+=1
                y+=1
            if x == 17: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                seventeen.append(f"{hold.OL}")
                f.write (f"{x} {hold.OL}\n")
                seventeen.append(hold.VH)
                f.write (f"{x} {hold.VH}\n")
                seventeen.append(hold.H)
                f.write (f"{x} {hold.H}\n")
                seventeen.append(hold.M)
                f.write (f"{x} {hold.M}\n")
                seventeen.append(hold.E)
                f.write (f"{x} {hold.E}\n")
                seventeen.append(hold.NR)
                f.write (f"{x} {hold.NR}\n")
                x+=1
                y+=1
            if x == 18: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                eighteen.append(f"{hold.OL}")
                f.write (f"{x} {hold.OL}\n")
                eighteen.append(hold.VH)
                f.write (f"{x} {hold.VH}\n")
                eighteen.append(hold.H)
                f.write (f"{x} {hold.H}\n")
                eighteen.append(hold.M)
                f.write (f"{x} {hold.M}\n")
                eighteen.append(hold.E)
                f.write (f"{x} {hold.E}\n")
                eighteen.append(hold.NR)
                f.write (f"{x} {hold.NR}\n")
                x+=1
                y+=1
            if x == 19: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                nineteen.append(f"{hold.OL}")
                f.write (f"{x} {hold.OL}\n")
                nineteen.append(hold.VH)
                f.write (f"{x} {hold.VH}\n")
                nineteen.append(hold.H)
                f.write (f"{x} {hold.H}\n")
                nineteen.append(hold.M)
                f.write (f"{x} {hold.M}\n")
                nineteen.append(hold.E)
                f.write (f"{x} {hold.E}\n")
                nineteen.append(hold.NR)
                f.write (f"{x} {hold.NR}\n")
                x+=1
                y+=1
            if x == 20: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twenty.append(f"{hold.OL}")
                f.write (f"{x} {hold.OL}\n")
                twenty.append(hold.VH)
                f.write (f"{x} {hold.VH}\n")
                twenty.append(hold.H)
                f.write (f"{x} {hold.H}\n")
                twenty.append(hold.M)
                f.write (f"{x} {hold.M}\n")
                twenty.append(hold.E)
                f.write (f"{x} {hold.E}\n")
                twenty.append(hold.NR)
                f.write (f"{x} {hold.NR}\n")
                x+=1
                y+=1
            if x == 21: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twentyone.append(f"{hold.OL}")
                f.write (f"{x} {hold.OL}\n")
                twentyone.append(hold.VH)
                f.write (f"{x} {hold.VH}\n")
                twentyone.append(hold.H)
                f.write (f"{x} {hold.H}\n")
                twentyone.append(hold.M)
                f.write (f"{x} {hold.M}\n")
                twentyone.append(hold.E)
                f.write (f"{x} {hold.E}\n")
                twentyone.append(hold.NR)
                f.write (f"{x} {hold.NR}\n")
                x+=1
                y+=1
            if x == 22: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twentytwo.append(f"{hold.OL}")
                f.write (f"{x} {hold.OL}\n")
                twentytwo.append(hold.VH)
                f.write (f"{x} {hold.VH}\n")
                twentytwo.append(hold.H)
                f.write (f"{x} {hold.H}\n")
                twentytwo.append(hold.M)
                f.write (f"{x} {hold.M}\n")
                twentytwo.append(hold.E)
                f.write (f"{x} {hold.E}\n")
                twentytwo.append(hold.NR)
                f.write (f"{x} {hold.NR}\n")
                x+=1
                y+=1
            if x == 23: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twentythree.append(f"{hold.OL}")
                f.write (f"{x} {hold.OL}\n")
                twentythree.append(hold.VH)
                f.write (f"{x} {hold.VH}\n")
                twentythree.append(hold.H)
                f.write (f"{x} {hold.H}\n")
                twentythree.append(hold.M)
                f.write (f"{x} {hold.M}\n")
                twentythree.append(hold.E)
                f.write (f"{x} {hold.E}\n")
                twentythree.append(hold.NR)
                f.write (f"{x} {hold.NR}\n")
                x+=1
                y+=1
            if x == 24: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twentyfour.append(f"{hold.OL}")
                f.write (f"{x} {hold.OL}\n")
                twentyfour.append(hold.VH)
                f.write (f"{x} {hold.VH}\n")
                twentyfour.append(hold.H)
                f.write (f"{x} {hold.H}\n")
                twentyfour.append(hold.M)
                f.write (f"{x} {hold.M}\n")
                twentyfour.append(hold.E)
                f.write (f"{x} {hold.E}\n")
                twentyfour.append(hold.NR)
                f.write (f"{x} {hold.NR}\n")
                x+=1
                y+=1
            if x == 25: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x) # I forgot to get rid of the comment before I copied it :skull:
                print (hold.OL)
                twentyfive.append(f"{hold.OL}")
                f.write (f"{x} {hold.OL}\n")
                twentyfive.append(hold.VH)
                f.write (f"{x} {hold.VH}\n")
                twentyfive.append(hold.H)
                f.write (f"{x} {hold.H}\n")
                twentyfive.append(hold.M)
                f.write (f"{x} {hold.M}\n")
                twentyfive.append(hold.E)
                f.write (f"{x} {hold.E}\n")
                twentyfive.append(hold.NR)
                f.write (f"{x} {hold.NR}\n")
                x+=1
                y+=1
            if x == 26: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twentysix.append(f"{hold.OL}")
                f.write (f"{x} {hold.OL}\n")
                twentysix.append(hold.VH)
                f.write (f"{x} {hold.VH}\n")
                twentysix.append(hold.H)
                f.write (f"{x} {hold.H}\n")
                twentysix.append(hold.M)
                f.write (f"{x} {hold.M}\n")
                twentysix.append(hold.E)
                f.write (f"{x} {hold.E}\n")
                twentysix.append(hold.NR)
                f.write (f"{x} {hold.NR}\n")
                x+=1
                y+=1
            if x == 27: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twentyseven.append(f"{hold.OL}")
                f.write (f"{x} {hold.OL}\n")
                twentyseven.append(hold.VH)
                f.write (f"{x} {hold.VH}\n")
                twentyseven.append(hold.H)
                f.write (f"{x} {hold.H}\n")
                twentyseven.append(hold.M)
                f.write (f"{x} {hold.M}\n")
                twentyseven.append(hold.E)
                f.write (f"{x} {hold.E}\n")
                twentyseven.append(hold.NR)
                f.write (f"{x} {hold.NR}\n")
                x+=1
                y+=1
            if x == 28: # I could probably find a better way somewhere but that would take more effort than this 
                hold = DIFF(x)
                print (hold.OL)
                twentyeight.append(f"{hold.OL}")
                f.write (f"{x} {hold.OL}\n")
                twentyeight.append(hold.VH)
                f.write (f"{x} {hold.VH}\n")
                twentyeight.append(hold.H)
                f.write (f"{x} {hold.H}\n")
                twentyeight.append(hold.M)
                f.write (f"{x} {hold.M}\n")
                twentyeight.append(hold.E)
                f.write (f"{x} {hold.E}\n")
                twentyeight.append(hold.NR)
                f.write (f"{x} {hold.NR}\n")
                x+=1
                y+=1
            else: 
                break
    print (fifteen)
    return fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twentyone, twentytwo, twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight