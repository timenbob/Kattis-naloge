n=int(input())
def funkcije(n):
    sumi=0
    for i in range(n):
        if input()=="O":
            sumi+= 2**(n-i-1)#prerečunamo za vsak O ko ga naletimo da bomo moreli vse živali pod šeekrat spremeniti
    return sumi
print(funkcije(n))