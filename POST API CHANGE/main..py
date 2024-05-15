from getinfofromtierlist import allinfo
from values import baseelo
import glicko2

player = glicko2.Player()
player.setRd(1)
player.setRating(1500)

#hey me remember to add a way to send what your API key is 
def main():
    ratinginfo = allinfo()
    print (2+2)
    i=0
    try:
        while True:
            temp = (ratinginfo[i])
            hold = int(temp["level"])
            ELO = baseelo[hold]
            print(ELO)
            i+=1
            if temp["standing"] != "Easy":
                adjusted = ELO-50
                print (glicko(ELO))
                print (temp)
            
            if temp["standing"] == "Medium":
                adjusted = ELO-0
                glicko(ELO)
    except:
        pass
    return

#just make the rd low
def glicko(elo):
    player.update_player([elo],[1],[1])
    hold = player.getRating()
    f = open("ELO.txt","w")
    f.write(f"{hold[:6]}")
    elo = player.getRating()
    return elo



if __name__ == "__main__":
    main()