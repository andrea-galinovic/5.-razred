#crtanje pomoću kornjače

#uključi modul za crtanje i spoji imenički prostor - inače bi morala uvijek pisati turtle.
from turtle import*

#postavljanje naslova crteža
title('kuća')

#postavljanje na početak
home()

#unesi početnu X poziciju kuće
xpoz=int(input('Unesi početnu poziciju kuće x='))

#unesi početnu Y poziciju kuće
ypoz=int(input('Unesi početnu poziciju kuće y='))

#unesi dimenzije kuće
sirina=int(input('Unesi širinu kuće: '))

visina=int(input('Unesi visina kuće: '))

#brisanje ekrana
clear()

#digni olovku
penup()

#odi na početnu poziciju kuće
goto(xpoz,ypoz)

#spusti olovku
pendown()

#pokazi kornjaču
showturtle()

#crtaj pod
forward(sirina)
#okreni kornjaču za 90 stupnjeva u lijevo
left(90)
#crtaj desni zid
forward(visina)
#okreni kornjaču za 3*90 stupnjeva u u desno što je 90 u lijevo
right(90*3)
#crtaj plafon
forward(sirina)
#okreni kornjaču za 90 stupnjeva u lijevo
left(90)
#crtaj lijevi zid
forward(visina)
#vrati se na plafon
backward(visina)
#crtaj lijevu kosinu krova
goto(xcor()+sirina/2,ycor()+sirina/2)
#crtaj desnu kosinu krova
goto(xcor()+sirina/2,ycor()-sirina/2)