#na internetu sem našel veliko rešitev za to nalogo tako da sem si pomagal s kakšno idejo
vrstica1 = input().split() #nrdimo sez


prejete_mol = vrstica1[0] #prvi element sez
st_molekul = int(vrstica1[1]) #drug el

zelene_mol = input()#želena mol


slovar_prejetih_mol = {} #slovarček za vnose
i = 0
while i < len(prejete_mol):
	trenutna_crka = prejete_mol[i]
	cifra = ""
	st_elementa = 1
	i += 1

	while(i < len(prejete_mol) and prejete_mol[i].isdigit()):#pru pogoj da smo sezmeri v prumu delu isdigit preveri če so cifre
		cifra += prejete_mol[i]#delamo tko da ce je cifra vec mestna 
		i += 1

	if cifra: #če smo cifro že nasli gremo naprej , npr ce cifre ni pomeni da je cifra 1 zato ze gor 1
		st_elementa = int(cifra)

	if  trenutna_crka in slovar_prejetih_mol: #ce ze je v slovarju dodamo
		slovar_prejetih_mol[trenutna_crka] += st_elementa

	else: #nov element v slovar
		slovar_prejetih_mol[trenutna_crka] = st_elementa



slovar_zelenih_mol = {} #slovarček za zelene stvari, zelo podobno kot zgoraj (isto)
i = 0
while i < len(zelene_mol):
	trenutna_crka = zelene_mol[i]
	cifra = ""
	st_elementa = 1
	i += 1

	while(i < len(zelene_mol) and zelene_mol[i].isdigit()):
		cifra += zelene_mol[i]
		i += 1

	if cifra:
		st_elementa = int(cifra)

	if trenutna_crka in slovar_zelenih_mol:
		slovar_zelenih_mol[trenutna_crka] += st_elementa

	else:
		slovar_zelenih_mol[trenutna_crka] = st_elementa


vrednost = True
najbol_vrjetne = 10**2500 #podobno cifro sem našel na večih spletnih rešitvah
for element, količina in slovar_zelenih_mol.items():#zaskosamo naš zelen slovar

	if element not in slovar_prejetih_mol:
		vrednost = False #vrednost rata False in takoj naprej sprintamo 0
	else:
		količina_mol = slovar_prejetih_mol[element] * st_molekul // slovar_zelenih_mol[element] #se sprehajamo čes da pregledamo vse in vzamemo tm ka mamo najmn
		if količina_mol < najbol_vrjetne:
			najbol_vrjetne = količina_mol

if vrednost:
	print(najbol_vrjetne)
else:
	print(0)