st_razlike=int(input())
zaporedje_ljudi1=input()
zaporedje_ljudi=[] #iz str naredimo niz
for i in zaporedje_ljudi1:
    zaporedje_ljudi.append(i)

#stejemo M in W
zensek=0
moski=0

for i in range(len(zaporedje_ljudi)):
    if zaporedje_ljudi[i]=="M":
        if(abs((moski+1)-zensek)>st_razlike): #ce je razlika vecja ko dodamo se enega M 
            if zaporedje_ljudi[i+1]=="W":     #pogledamo naslednjega ce je W dodamo zenskam +1 in zamenjamo zaporedje M damo na mesto kjer je bil W
                zensek+=1
                zaporedje_ljudi[i+1]="M"
            else:
                break
        else: #ce je razlika manjsa
            moski += 1
        
    elif zaporedje_ljudi[i]=="W":    #podobno kot vzgoraj samo da M = W
        if(abs(moski-(zensek+1))>st_razlike):
            if zaporedje_ljudi[i+1]=="M":
                moski+=1
                zaporedje_ljudi[i+1]="W"
            else:
                break
        else:
            zensek += 1
    
print(zensek + moski)

