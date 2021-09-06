

crossaints = int(input("Hoeveel crossaints wil je?\n-> "))
cossaintsPrijs = int(float(input("Hoeveel euro kost 1 crossaint?\n-> "))*100)
stokbrood = int(input("Hoeveel stokbroden wil je?\n-> "))
stokbroodWaarde = int(float(input("Hoeveel euro kost 1 stokbrood?\n-> "))*100)
kortingBonnen = int(input("Hoeveel kortingsbonnen heb je?\n-> "))
kortingWaarde = int(float(input("Hoeveel zijn die kortingsbonnen waard in euro?\n-> "))*100)
koste = crossaints * cossaintsPrijs + stokbrood * stokbroodWaarde - kortingBonnen * kortingWaarde
print('De feestlunch kost je bij de bakker ' + str(koste) + ' cent ('+ str(koste/float(100)) +' euro) voor de ' + str(crossaints) + ' croissantjes en de '+ str(stokbrood)+' stokbroden als de '+str(kortingBonnen)+' kortingsbonnen nog geldig zijn')