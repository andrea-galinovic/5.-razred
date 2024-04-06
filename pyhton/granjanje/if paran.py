#zadatak 3 udbenik str 59

#unos broja
broj=int(input('unesi prirodni broj:'))

#provjera da li je broj prirodan
if broj>0: 
    #provjera da li je broj paran
    if broj%2==0:
        #broj je paran
        print('broj je paran')
    else:
        #broj nije paran
        print('broj nije paran')
else:
    #broj nije prirodan
    print('broj nije prirodan')
