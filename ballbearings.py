import math

vrstice = int(input())

for n in range(vrstice):
    
    vnos = list(map(float, input().split())) #input takoj raskosamo na floute in damo v seznam

    D = float(vnos[0])#premer kroga
    d = float(vnos[1])#premer mičkenega
    s = float(vnos[2])#kok med krogci
    
    stevilo = math.floor(math.pi/math.asin((d+s)/(D-d)))# preracun krogcov
    
    print(stevilo)
    