import re
link = "https://piuimages.arroweclip.se/songs/ed6166ff-e750-4778-a7ec-ec64e706fb52.png&quot"
temp = re.sub(r'^.*?/songs/', '', link)
temp = temp.replace ("&quot","")
print (temp)