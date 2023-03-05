#varijable
visina=int(input('visina='))
dubina=int(input('dubina='))
broj=int(input('broj stepenica='))

#gdje pocinje
xpoz=int(input('Unesi pocetnu poziciju stepenica x='))
ypoz=int(input('Unesi pocetnu poziciju stepenica y='))

from turtle import*
#naslov crteza
title('stepenice')

#odi na pocetnu poziciju
penup()
goto(xpoz,ypoz)
pendown()
showturtle()

#crtaj stepenice 
for i in range(broj):
    left(90);forward(visina)
    right(90);forward(dubina)
#dolje
right(90);forward(visina*broj)
#lijevo
right(90);forward(dubina*broj)
