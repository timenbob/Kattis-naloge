def faktor():
    vnost = input() #input na dva kosa

    list_vnos = vnost.split(" ")#naredimo seznam iz vnosa

    clanki = list_vnos[0]#poberemo po delih
    faktor =list_vnos[1]

    st_znanstveniki = (int(clanki) * (int(faktor) - 1)) + 1 #formulca faktor-1 ker zmeraj zaokrozujemo navzgor.....+1 da presežemo mejo

    return(st_znanstveniki)

print(faktor())