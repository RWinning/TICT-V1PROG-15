leeftijd = eval(input ('Geef je leeftijd: '))
paspoort = input('Nederlands paspoord: ')

if leeftijd >= 18 or paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Je mag niet stemmen')
