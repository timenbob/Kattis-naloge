sez = []

for i in range(5):#max 5 elementou
    elemet = input()
    if "FBI" in elemet:
        sez.append(str(i + 1))# delamo seznam tko da uzamemo i pa damo +1 zato ker i začne z 0

if sez:#ce sez ni prazen nam ta vrne
    print (" ".join(sez))#seznam zdruzmo s presledki
else:
    print ("HE GOT AWAY!")