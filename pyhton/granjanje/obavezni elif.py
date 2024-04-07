#unesi boju na hrvatskom i ispisi ime boje na engleskom

#unesi boju
boja=input('unesi ime boje na hrvatskom:')

#ispisi boju na hrvatskom
print('boja je:',boja)

#definiranje pocetnog teksta
tekst='engleski naziv je'

#provjera da li je boja plava
if boja=='plava':
    print(tekst,'blue')
elif boja=='crvena':
    print(tekst,'red')
elif boja=='zelena':
    print(tekst,'green')
elif boja=='bjela':
    print(tekst,'white')
elif boja=='crna':
    print(tekst,'black')
elif boja=='ljubicasta':
    print(tekst,'purpule')
elif boja=='roza':
    print(tekst,'pink')
elif boja=='zuta':
    print(tekst,'yellow')
else:
    print('boja mi nije poznata')
