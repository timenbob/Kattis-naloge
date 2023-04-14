slovar={'upper':2,'middle':1,'lower':0}

for _ in range(int(input())):
    n=int(input())
    a=[0]*n #naredimo seznamček da bomo lahko notr dajal osebe lepo
    k=0 #če je oseba brez klasa
    for i in range(n):
        w,c,_=input().split() #input osebe rezdelimo na osebo, klas/nivo v drubi in _ nepomemben člen
        f=[-slovar[x] for x in c.split('-')]
        f.reverse()
        k=max(k,len(f))
        a[i]=(f, w[:-1]) #v a damo na mesto i zapis (kao si sledijo statusi, oseba),w gre od :-1 zato da ne vzamemo :
    for i in range(n):
        f=a[i][0] #pogledamo tabelco s statusi
        f.extend([-1]*(k-len(f))) #dodamo -1 tolkrat da bojo usi enako dolgi
    a.sort()
    for i in range(n): print(a[i][1])


    print('='*30)
