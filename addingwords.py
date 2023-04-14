       #za lazje spremknjanje
d = {} #slovarček ključ vrednost
v = {} #slovarček vrednost kjuč

while True:
    try:
        line=input()
        s = line.split() #razdelimo na vse koščke

        if s[0] == 'def': #pogledamo prvi element da vemo ali bo def sepravi definiramo "element"
            if s[1] in d.keys(): #ce je element ze v slovarčku ga izbrisemo
                del v[int(d[s[1]])] #izbrisemo iz v
            d[s[1]] = s[2] #v obeh slobarčkih naredimo nov element dodamo v d
            v[int(s[2])] = s[1] #dodamo v v

        elif s[0] == 'calc':  #tuki bomo malo predelali podatke da bomo imeli novi stavek na katerem lahko uporabimo eval
            novi_stavek=""
            for element in s[1:]:
                if element == "=":
                    element=""
                elif element in d:
                    element=d[element]
                novi_stavek += element

            try:
                vrednost= eval(novi_stavek) #ce imamo vse vrednosti deluje
                if vrednost in v:
                    print(" ".join (s[1:]), v[vrednost])
                else:
                    print(" ".join (s[1:]), 'unknown')
            except:#drugače ne
                 print(" ".join (s[1:]), 'unknown')
        else:
            d.clear()#pobrisemo d in v kot po navodilih
            v.clear()

    except:
        break