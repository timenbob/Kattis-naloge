from math import pi

M,N,R=input().split()
M=int(M) #ravne črte
N=int(N) #polkrogi
R=float(R) #radi mesta

m1,n1,m2,n2=map(int,input().split())
dolzina_enote=R/N

if n1 == 0:#ena točka v izhodišču/na prvem(o-čtem)polkrogu
    print(f"{n2}") 
elif n2 == 0:#ena točka v izhodišču
    print(f"{n1}")
elif m1 == m2:#ista segmenta(kos torte) ista črta na drugem polkrogu
    print(f"{abs(n1-n2) * dolzina_enote}") #koliko enot*dolzina enote
else:
    sez=[]
    for x in range(0,N+1):#ker gre DO N+1
        #racun se razdeli na 2 dela prvi do + nam poda mozne dolzine za prehod iz enega polkroga na drugega
        #po + dobimo možne dolžine na ravnih črtah
        sez.append(abs(m1-m2)*(x/N)*R/M * pi + (abs(x-n1) + abs(x-n2)) * dolzina_enote)
    print(min(sez))
