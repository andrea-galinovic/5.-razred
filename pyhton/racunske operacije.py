#ponavljane racunskihi operacija

#unos varjabli i pretvaranje u cijele brojeve

djeljenik=int(input('unesi djeljenika='))
djelitelj=int(input('unesi djelitelja='))

#idemo djeliti
print('kolicnik =',djeljenik/djelitelj)

#cjelobrojno djeljenje i ostatak
cjelobrojniKolicnik=djeljenik//djelitelj
print(djeljenik,'cjelobrojno podjeljeno s',djelitelj,' = ',cjelobrojniKolicnik)

ostatak=djeljenik%djelitelj
print('a ostatak je ',ostatak)

#mnozenje i zbrajanje
print(cjelobrojniKolicnik,' * ',djelitelj,' + ',ostatak,' = ',cjelobrojniKolicnik*djelitelj+ostatak)


