MOD=1000000007

def funkcija(n,cas,seznam):
    skupni_cas=0
    kazne = 0
    for i,t in enumerate(seznam):#cifra problema,casek
        if skupni_cas + t > cas:# pogledamo ce smo ze prisli cez cas
            return i, kazne
        skupni_cas += t
        kazne = (kazne + skupni_cas) % MOD #po formuli
    return n, kazne #če nismo prišli čez čas

n,cas = map(int,input().split())
a,b,c,t0 = map(int,input().split())
lis = [t0]
for _ in range(1,n):  #nardimo seznam casov ki jih potrebujemo za resevanje problemov
    lis.append(((a*lis[-1]+b) % c) + 1)

n,kazen=funkcija(n,cas,sorted(lis))#sort zato da imamo manše na začetku ker iščemo koliko največ
print(f"{n} {kazen}")




