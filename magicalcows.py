from collections import defaultdict #defaultdict uporabimo zado da lahko dodamo vrednost elementu ki ni v dict
"""
	Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. 
	The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. 
	It provides a default value for the key that does not exists.
"""
(max_kravic, farme_z_vsaj_eno_k, dnevi) = input().split(" ")
max_kravic = int(max_kravic)
farme_z_vsaj_eno_k = int(farme_z_vsaj_eno_k)
dnevi = int(dnevi)

farme_slovar = defaultdict(lambda: 0)#slovar ki ko kličemo vrednost po ključu, če ključa ni vrne 0
"""
	defaultdict takes a zero-argument callable to its constructor, which is called when the key is not found, as you correctly explained. 
	lambda: 0 will of course always return zero, but the preferred method to do that is defaultdict(int) , which will do the same thing
"""
farme = []

for i in range(farme_z_vsaj_eno_k): #sprehodmo po farmah ka majo usaj1 kravo na začetku(dan0)
	vrednost = int(input()) #se vense koliko kravic
	if vrednost != 0:
		farme_slovar[vrednost] += 1
		#pogledat a je not al ni ce je povecamo ce ni dodamo tko da ma 1
#pisemo slovar vrednost st kravic st takih kmetij

for i in range(50+1): #ker gremo v navodilu do 50 tukaj pa moramo do 51 pač M kdaj regulator obišče
	novi = 0
	for ključ in farme_slovar: #st farm
		novi += farme_slovar[ključ]

	farme.append(novi)

	farme_slovar_2 = defaultdict(lambda:0)# nov slovar farama pa vrednosti

	for ključ in farme_slovar:
		if ključ * 2 > max_kravic:
			farme_slovar_2[ključ] += farme_slovar[ključ] * 2
		else:
			farme_slovar_2[ključ * 2] += farme_slovar[ključ]
	farme_slovar = farme_slovar_2


for i in range(dnevi): #kolkrat ins. pride obiskat
	indeks = int(input())
	print(farme[indeks])

	
