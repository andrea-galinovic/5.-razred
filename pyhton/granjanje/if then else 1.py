#zadatak 1 udbenik str 57

#definiranje cijanog broja sadnica
cilj=int(input('unesi ciljani broj sadnica:'))

#provjera da li cilj ima smisla
if cilj<=0:
    print('cilj mora biti veci od 0')
else:
    #unos broja sadnica za ucenika
    sadnice=int(input('unesi broj sadnica koje je posadio ucenik:'))

    #provjera da li uneseni broj satnica ima smisla
    if sadnice>=0:        

        #provjera dali je ucenik zadovoljio cilj
        if sadnice>=cilj:
            print('ucenik je zadovoljio cilj')
        else:
            print('ucenik nije zadovoljio cilj')
    else:
        print('broj mora biti veci ili jednak nuli')

    


