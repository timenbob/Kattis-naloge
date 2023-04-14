stevilo_vrstic=int(input())

stevec_besed = {}
uporabnik_besede = {}

for _ in range(stevilo_vrstic):

    podatki = input().split()
    ime=podatki[0]
    besede=podatki[1:]
    
    for beseda in besede:
        if ime in uporabnik_besede.keys(): #slovarček oseba...mnozica besed
            uporabnik_besede[ime].add(beseda)
        else:
            uporabnik_besede[ime] = {beseda}

        if beseda in stevec_besed.keys():#pisemo slovarček ...beseda, ponovitve
            stevec_besed[beseda] += 1
        else:
            stevec_besed[beseda] = 1

mn_besed = set(stevec_besed.keys())#mnozica vseh besed
for s in uporabnik_besede.values():
    mn_besed = mn_besed.intersection(s)#naredimo presek od vseh besed in besed ki jih je uporabil vsak uporabnik da dubimo katere so uporabili vsi

tabela = sorted(mn_besed, key=lambda x: (-stevec_besed[x],x))# ta vrstica nam razvrsti besede glede na to, kolikokrat se pojavijo - zato da gre v obratnem vrsten redu ne 123 amoak 321
#stevec_besed[x] gre pogledat kolikokrat sej je beseda x ponovila, pogleda besedo

if mn_besed:#ce mnozica ni prazna
    print('\n'.join(tabela))
else:
    print('ALL CLEAR')