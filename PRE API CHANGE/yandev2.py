
def yandev():
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
    f=open("tierlistsnapshot.txt","r")
    fifteen.append(f"{f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()}")
    sixteen.append(f"{f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()}")
    seventeen.append(f"{f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()}")
    eighteen.append(f"{f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()}")
    nineteen.append(f"{f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()}")
    twenty.append(f"{f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()}")
    twentyone.append(f"{f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()}")
    twentytwo.append(f"{f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()}")
    twentythree.append(f"{f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()}")
    twentyfour.append(f"{f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()}")
    twentyfive.append(f"{f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()}")
    twentysix.append(f"{f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()} {f.readline()}")
    return fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix

def yandev2(string,list):
    if string in list[0]:
        return string
    if string in list[1]:
        pass





