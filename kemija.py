
from sympy import *

stevilo_točk_kroga=int(input())
seznam_vnosov=[]

for _ in range(stevilo_točk_kroga):
    #naredim seznam list
    #in pol z i i+1 i+2 sprehajam čes
    vnos=int(input())
    seznam_vnosov.append(vnos)

#naredimo seznam spremenljiuk kjer so onlike "ai"
seznam=[]
for i in range(stevilo_točk_kroga):
    seznam.append(f"a_{i}")


slovar={}#oblike st vrstice(0....n-1):[3je podatki oz kateri so sosednji]
for i in range(stevilo_točk_kroga):
    if i == 0:
        slovar[0]=[seznam[stevilo_točk_kroga-1],seznam[0],seznam[1]]
    elif i == stevilo_točk_kroga-1:
        slovar[stevilo_točk_kroga]=[seznam[stevilo_točk_kroga-2],seznam[stevilo_točk_kroga-1],seznam[0]]
    else:
        slovar[i]=[seznam[i-1],seznam[i],seznam[i+1]]

matrika=[]
prazna_vrstica_matrike=[0]*stevilo_točk_kroga


for element_seznam in slovar.values():
    
    #najdem št v nizu da najdem pozicijo za v kodi
    ita_vrstica_matrike=[0]*stevilo_točk_kroga
    for element in element_seznam:#a_i
        #print(element)
        pozicija,st = (element.split("_")) #a_1 a_2... "a_1"
        #print(ita_vrstica_matrike)
        ita_vrstica_matrike[int(st)] = 1
        
    matrika.append(ita_vrstica_matrike)
    ita_vrstica_matrike=[]




zdruzena_matrika=[]
for i in range(len(matrika)):
    zdruzena_matrika.append(matrika[i]+[seznam_vnosov[i]])


#naredimo gausa na zdruzeni
augmented_A = Matrix(zdruzena_matrika)
resitev_matrika=augmented_A.rref()[0]


resitev_seznam_seznamov= resitev_matrika.tolist()


pranza_vrstica_v_resitvi=[0]*(stevilo_točk_kroga+1)
resitev_neodvisne=[]
#sprehodmo se čez resitev_seznam_seznamov ce naletimo na prazen seznam pomeni da so rešitve odvisne resitev damo na [] in moramo drugače
#če ne naletimo na prazen seznam naredimo seznam z resitvami ki ga bomo nato sprintali

for vrstica in resitev_seznam_seznamov:
    if vrstica==pranza_vrstica_v_resitvi:
        resitev_neodvisne=[]
        break
    else:
        resitev_neodvisne+=[vrstica[stevilo_točk_kroga]]

#ce smo dobili nodvisno resitev jo izpisemo drugače ne
if resitev_neodvisne != []:
    for resitev in resitev_neodvisne:
        print(int(resitev))

else:
    for i in range(stevilo_točk_kroga):#zaenkrat če rešitev ni enolična da smo ničle
        print(0)
    

"""
A = np.array(matrika)
b = np.array(seznam_vnosov)
x=np.linalg.solve(A,b)
print(x)



vnos:
5
1
2
3
4
5

kaj vrnejo printi
print(seznam_vnosov)
print(seznam)
print(slovar)

[1, 2, 3, 4, 5]
['a0', 'a1', 'a2', 'a3', 'a4']
{0: ['a4', 'a0', 'a1'], 1: ['a0', 'a1', 'a2'], 2: ['a1', 'a2', 'a3'], 3: ['a2', 'a3', 'a4'], 5: ['a3', 'a4', 'a0']}


"""

