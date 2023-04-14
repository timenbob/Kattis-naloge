intervali = []
for _ in range(int(input())):
	intervali.append(list(map(int, input().split())))#seznam oblike[[1,2],..]

intervali.sort() #uredimo da lahko nato gledamo sosednje(po prvem)

idx = 1#ker bomo gledali enga prej
while idx < len(intervali):
	if intervali[idx][0] <= intervali[idx - 1][1]:#[1,3][0]<=[0,2][1]..1<=2 preverimo če se sekata 2 sosednja intervala
		intervali[idx] = [intervali[idx - 1][0], min(intervali[idx - 1][1], intervali[idx][1])]#naredimo nekakšen presek intrvalov kjer za spodnjo mejo uzamemo mejo od 
        #prejšnega za zgornjo pa minimum 
		intervali.pop(idx - 1)#izbrišemo prejšnega
	else:
		idx += 1#če se ne pokriva ostane vse isto samo index povečamo
print(len(intervali))
