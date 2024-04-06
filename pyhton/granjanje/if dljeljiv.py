#zadatak 6 udbenik str 63 s dodatkom unosa djeljitelja

#unos broja
broj=int(input('unesi prirodni broj:'))

#unos visekratnika
visekratnik=int(input('unesi visekratnik (prirodni broj):'))

#provjera da li je broj prirodan
if broj>0 and visekratnik>0: 
    #provjera da li je broj paran
    if broj%visekratnik==0:
        #broj je djeljiv s visekratnikom
        print('broj je djeljiv s ',visekratnik)
    else:
        #broj nije djeljiv s visekratnikom
        print('broj nije nije djeljiv s',visekratnik)
else:
    #broj nije prirodan
    print('broj i/ili visekratnik nisu prirodni brojevi')
    
