studenti = {}
projekti = {}
trenutni_projekt = None

while True:
    vnos = input()


    if vnos == "0":#ko zares končamo
        break


    if vnos == "1": #ko naredimo en kos
        projekti = sorted(projekti.items(), key=lambda x: (-x[1], x[0])) #lambda gre po -x[1]zato da uredimo po padajočem vrstnem redu prijav
        for projekt, stevec in projekti:
            print(projekt, stevec)


        studenti = {}
        projekti = {}
        trenutni_projekt = None
        continue


    if vnos.isupper():
        trenutni_projekt = vnos
        projekti[trenutni_projekt] = 0 #pišemo slovar projektov na zecetuku ima 0 studentov
    elif vnos in studenti: #če je oseba že pri študentih
        if studenti[vnos] != trenutni_projekt: #če oseba še ni pri projektu
            if studenti[vnos] is not None: #če je študent ze prijavljen na kakšen projekt
                projekti[studenti[vnos]] -= 1 #projekt ki ima to osebo -1 oseba
                studenti[vnos] = None #oseba ni na nobenem projektu
    else:#oseba ni pr studentih
        studenti[vnos] = trenutni_projekt #studentu dodamo trenuten projekt
        projekti[trenutni_projekt] += 1#projektu dodamo stevilo prijavljenih oseb