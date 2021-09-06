# Lukas Bellaart PizzaCalculator
import webbrowser
import time

print('Welkom u krijgt zo de keuze uit 3 pizzas. de prijzen zijn: \nSmall pizza €7.99\nMedium pizza €9.99\nLarge pizza €12.99')

pizzaPrijzen = { #Prijzen van de pizzas in een dictionary
    "small": 7.99,
    "medium": 9.99,
    "large": 12.99
}

besteldePizzas = [] #slaat de gekozen pizzas op

while True: #loops totdat hij wordt doorbroken
    optie = input("Wat wilt u doen? (betalen of pizza kopen) -> ")
    optie = optie.lower() # zonder caps
    if optie == "pizza kopen": # Pizza selectie
        pizza = input("Wat voor pizza wilt u? -> ")
        pizza = pizza.lower() # zonder caps
        if pizza in pizzaPrijzen: # kijkt of de pizza in pizzaprijzen zit
            quantity = input("Hoeveel " +pizza+" pizza wilt u bestellen? -> ")
            quantity = int(quantity) #omzetten naar int

            for x in range(0, quantity): # for loop
                besteldePizzas.append(pizza) # voegt de gekozen pizzas toe aan de array

            smallPizzaCount = 0
            mediumPizzaCount = 0
            largePizzaCount = 0
            totalPizzaCount = 0

            for x in besteldePizzas: #kijkt hoevel pizzas er in de besteldePizzas array zit
                if x == "small":
                    totalPizzaCount = totalPizzaCount + 1
                    smallPizzaCount = smallPizzaCount + 1
                elif x == "medium":
                    totalPizzaCount = totalPizzaCount + 1
                    mediumPizzaCount = mediumPizzaCount + 1
                elif x == "large":
                    totalPizzaCount = totalPizzaCount + 1
                    largePizzaCount = largePizzaCount + 1

            # prijsberekening
            smallPrijs = smallPizzaCount * pizzaPrijzen["small"]
            mediumPrijs = mediumPizzaCount * pizzaPrijzen["medium"]
            largePrijs = largePizzaCount * pizzaPrijzen["large"]

            totalPrijs = smallPrijs + mediumPrijs + largePrijs #totaalprijs berekent


            print("Wij hebben "+str(quantity) + " " + pizza + " pizza('s) in uw boodschappenmandje gedaan.")
            print(" ----------------------------------------------------")
            print("|  Small Pizza      : "+str(smallPizzaCount)+" - "+str(smallPrijs)+"                ")
            print("|  Medium Pizza     : "+str(mediumPizzaCount)+" - "+str(mediumPrijs)+"           ")               
            print("|  Large Pizza      : "+str(largePizzaCount)+" - "+str(largePrijs)+"   ")   
            print("|  Total Pizza      : "+str(totalPizzaCount)+" - "+str(totalPrijs)+"    ")           
            print('----------------------------------------------------')       


        else: 
            print("Die pizza hebben wij niet")
    elif optie == "betalen": # betaal optie
        smallPizzaCount = 0
        mediumPizzaCount = 0
        largePizzaCount = 0
        totalPizzaCount = 0

        #berekeningen
        for x in besteldePizzas:
            if x == "small":
                totalPizzaCount = totalPizzaCount + 1
                smallPizzaCount = smallPizzaCount + 1
            elif x == "medium":
                totalPizzaCount = totalPizzaCount + 1
                mediumPizzaCount = mediumPizzaCount + 1
            elif x == "large":
                totalPizzaCount = totalPizzaCount + 1
                largePizzaCount = largePizzaCount + 1

        # prijsberekening

        smallPrijs = smallPizzaCount * pizzaPrijzen["small"]
        mediumPrijs = mediumPizzaCount * pizzaPrijzen["medium"]
        largePrijs = largePizzaCount * pizzaPrijzen["large"]

        totalPrijs = smallPrijs + mediumPrijs + largePrijs


        print("Uw boodschappenmandje.")
        print(" ----------------------------------------------------")
        print("|  Small Pizza('s)       : "+str(smallPizzaCount)+" - "+str(smallPrijs)+"                ")
        print("|  Medium Pizza('s)      : "+str(mediumPizzaCount)+" - "+str(mediumPrijs)+"           ")               
        print("|  Large Pizza('s)       : "+str(largePizzaCount)+" - "+str(largePrijs)+"   ")   
        print("|  Totale Pizza('s)      : "+str(totalPizzaCount)+" - "+str(totalPrijs)+"    ")           
        print('----------------------------------------------------\n')       

        print("U wordt nu doorverwezen naar de betaling.")
        time.sleep(5) #wacht 5 seconden
        webbrowser.open('https://example.com/') # doorverwijzing naar https://example.com/
        break #stopt de loop
    else:
        print("Dat is geen optie")