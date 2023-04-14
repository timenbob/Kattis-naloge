st_kand = int(input()) #koliko kandidatov bo 2 do 20

stranke = {}
for element in range(st_kand):
    kandidat = input()    
    stranka = input()    
    stranke[kandidat] = stranka

glasovnice = int(input())
rezultat = {}
for element in range(glasovnice):    # prestejemo glasove
    ime_glasovnice = input()
    if ime_glasovnice in stranke.keys():#pogledamo če je ime sploh mozno
        if ime_glasovnice in rezultat.keys():#dodamo glas kandidatu / nov člen v slovarju
            rezultat[ime_glasovnice] += 1
        else:
            rezultat[ime_glasovnice] = 1
            
if len(rezultat.items()) > 1:         # pregledamo če sploh kakšen kandidat za zmagovalca
    kandidat, stevilo = max(rezultat.items(), key = lambda x: x[1]) # lamdanam vrne kandidata, in po elementih koloko glasov je kdo prejel poišče max
    zmagovalci = list(rezultat.values())
    if zmagovalci.count(stevilo) > 1:    #preštejemo koliko strank ima enako max stevilo glasov
        print("tie")
    else:
        print(stranke[kandidat])         # en zmagovalec
else:                                    #če ni nobenega glasova
    print("tie")
    