def skimjson(string):
    string = string.replace("☆","")
    string = string.replace("{","")
    string = string.replace("}","")
    string = string.replace("'","")
    string = string.replace("[","")
    string = string.replace("]","")
    return string
    
