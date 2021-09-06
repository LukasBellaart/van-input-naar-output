
personen = int(input("Met hoeveel personen ga je?\n-> "))
perVijfMinPP = int(float(input("Hoeveel euro kost het per 5 minuten pp?\n-> "))*100)
minuten = int(input("Hoe lang minuten wil je gaan?\n-> "))
koste = minuten / float(5) * perVijfMinPP * personen
print('Dit geweldige dagje-uit met ' + str(personen) + ' mensen in de Speelhal met ' + str(minuten) + ' minuten VR kost je maar ' + str(koste) + ' cent ('+str(koste/float(100))+' euro)')

