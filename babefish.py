
slovar = {}
vrednost = True
while(True):
    
    try: #poskusimo narediti ta del če ne pridemo do error idejo da uporabim try in exept na prosojnicah

        besede = input()

        if vrednost:

            if besede != "":  #če ni prazen damo v slovar ker prazen razdvoji slovar in besede
                beseda1, beseda2 = besede.split(" ")
                slovar[beseda2]=beseda1
            else: #če je prazen bomo imeli if false torej ta del spustimo za naprej
                vrednost = False

        else:
            if besede in slovar:
                print(slovar[besede]) #pogledamo v slovar
            else:
                print("eh") 

    except EOFError as error: #če pride do error končamo, EOFError se sproži ko input ne dobi več nič
        break
#dela tut brez da damo eoferror
#lahko bi pa gledal kdaj pride drug " " vnos



    




    
