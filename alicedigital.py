for _ in range(int(input())):#prvi input koliko datasetov imamo/ kolikokrat moramo čez program

    m = int(input().split()[1])#prvega elementa za koliko je podatkov ne potrebujemo,,, drugi element je tisti ki lahko nastopi le enkrat

    teze=map(int,input().split())#naredimo seznam stevil
    #==============================================================
    najvec, vmesni, pojav_m = (0,0,0)  #kar je med znaki = , podobne kode za računanje sem našel na več spletnih straneh
    for w in teze: #vsebovati mora vsaj en m
        if w < m: #če smo mansi od m je za tisti košček konec
            najvec = max(najvec, pojav_m + vmesni if pojav_m else 0)#izbere best če se m se ni pojavil
            vmesni, pojav_m = 0, 0
        elif w == m:
            najvec = max(najvec, pojav_m + vmesni if pojav_m else 0)#izbere best če se m še ni pojavil
            pojav_m = m + vmesni#vrednos ko se pojavi m
            vmesni = 0#na pre zaenkrat pozabimo ker zdej lahko nadaljujemo do naslednjega m
        else:
            vmesni += w#v pre seštevamo podraporedje
    #================================================================
    if pojav_m != 0:
        print(max(najvec, pojav_m + vmesni)) #da ukjučimo še zadnjo verzijo
    else:
        print(najvec)    


