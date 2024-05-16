import requests

def getuserscores():
    f = open("settings.txt","r")
    resultnum = f.readline()
    resultnum = resultnum.replace("RESULTCOUNT=","")
    authorization = f.readline()
    authorization = authorization.replace("API KEY=","")
    authorization = authorization.replace("\n","")

    response = requests.get(f"https://piuscores.arroweclip.se/api/phoenixScores?Page=1&Count={resultnum}", headers={
        'accept':'*/*',
        'Authorization':f'{authorization}'
    })
    request = response.json()
    i=0
    total = int(request["totalResults"])
    userscores=[]
    try:
        while i != total-1:
            identify = str(request["results"][i]["chart"]["id"])
            songtype = str(request["results"][i]["chart"]["type"])
            level = str(request["results"][i]["chart"]["level"])
            temp = {
                "id":identify,
                "type":songtype,
                "level":int(level)
            }
            userscores.append(temp)
            i+=1
    except:
        pass
    return userscores

def scoreposition(id,type,level):
    response = requests.get(f"https://piuscores.arroweclip.se/api/tierlist/passcount?ChartType={type}&Level={level}", headers={
        'accept':'*/*',
        'Authorization':'Basic VEhFUkVJU0FCT01CU1RSQVBQRURUT01ZQ0hFU1Q6NzEwYTExZjMtMmVjNi00OGViLTlkNTEtMjgxMTY2NzJkNDM1'
    })
    request = response.json()
    standing = []
    i=0
    try: 
        while True:
            identify = str(request[i]["chart"]["id"])
            rating = str(request[i]["category"])
            if identify == id:
                standing.append(rating)
                print (rating)
            i+=1
    except:
        pass
    return standing

def striplist(string):
    string = string.replace("'","")
    string = string.replace('"',"")
    string = string.replace("[","")
    string = string.replace("]","")
    return string

def allinfo():
    everything = getuserscores()
    i=0
    allresult = []
    try:
        while True:
            hold = everything[i]
            results = scoreposition(hold["id"],hold["type"],hold["level"])
            temp = str(results)
            results = striplist(temp)
            infodict = {
                "level":hold["level"],
                "standing":results
            }
            allresult.append(infodict)
            print (infodict)
            i+=1
    except:
        pass
    return allresult

if __name__ == "__main__":
    print (allinfo())    
