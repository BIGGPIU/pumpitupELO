from getinfofromtierlist import allinfo
from values import baseelo
import glicko2

player = glicko2.Player()
player.setRd(1)
player.setRating(1500)

#hey me remember to add a way to send what your API key is 
def main():
    ratinginfo = allinfo()
    i=0
    f = open("ELO.txt","w")
    try:
        while True:
            temp = (ratinginfo[i])
            hold = int(temp["level"])
            ELO = baseelo[hold]
            i+=1
            if temp["standing"] != "Easy":
                adjusted = ELO-50
                hold2 = glicko(adjusted)
            
            if temp["standing"] == "Medium":
                adjusted = ELO-0
                hold2 = glicko(adjusted)
            
            if temp["standing"] == "Overrated":
                adjusted = ELO-100
                hold2 = glicko(adjusted)
            
            if temp["standing"] == "Hard":
                adjusted = ELO+50
                hold2 = glicko(adjusted)

            if temp["standing"] == "VeryHard":
                adjusted = ELO+100
                hold2 = glicko(adjusted)

            if temp["standing"] == "Unrecorded":
                adjusted = ELO-200
                hold2 = glicko(adjusted)
                
    except:
        pass
    f.write(f"{hold2}")
    print (hold2)
    f.close()
    return

#just make the rd low
def glicko(elo):
    player.update_player([elo],[1],[1])
    hold = player.getRating()
    elo = player.getRating()
    return elo



if __name__ == "__main__":
    main()