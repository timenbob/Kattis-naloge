from math import *

vnos_m_n_t = input()
vnos_m_n_t = vnos_m_n_t.split()
#razdelimo vnos na 3 kose ki jih bomo rabili
m = int(vnos_m_n_t[0])
n = int(vnos_m_n_t[1])
t = int(vnos_m_n_t[2])

#zdefiniramo ker bomo potrebovali pri pogojih
fakultete = [1]
for i in range (1,14):
    fakultete.append(fakultete[i-1] * i)
 
vrednost = True
#pogoji ki jih moramo preveriti
if t == 1:
    if n > 14 or fakultete[n] > m:
        vrednost = False
elif t == 2:
    if 2 ** n > m:
        vrednost = False
elif t == 3:
    if n ** 4 > m:
        vrednost = False
elif t == 4:
    if n ** 3 > m:
        vrednost = False
elif t == 5:
    if n ** 2 > m:
        vrednost = False
elif t == 6:
    if n * log(n,2) > m:
        vrednost = False 
elif t == 7:
    if n > m:
        vrednost = False

if vrednost:  #preveri ali je vrednost True
    print("AC")
else:
    print("TLE")
