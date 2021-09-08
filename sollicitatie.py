punten = 0
vragen = [
    "Hoeveel jaren ervaring heeft met dieren-dressuur, jongleren of acrobatiek?\n",
    "Wat voor school diploma heeft u?\n",
    "Heeft u ervaring in het rijden van een voertuig? Zo ja, welk voertuig?\n",
    "Draagt u hoge hoeden?\n",
    "Wat is uw geslacht?\n",
    "Bent u ooit naar een circus geweest?\n",
    "Hoe breed is uw snor?\n",
    "Hoe lang is uw haar?\n",
    "Hoe lang bent u?\n",
    "Heeft u hiervoor een baan in het circus gehad?\n"
    "Hoe zwaar bent u?\n",
    "Heeft u een certificaat 'Overleven met gevaarlijk personeel'?\n",
    "Vind u clowns leuk?\n",
    "bb"
]

def vragenMaker(vragenNummer):
    antwoord = str(input(vragen[vragenNummer]))
    return antwoord

antwoord = vragenMaker(0)
if int(antwoord) >= 4:
    punten += 1

antwoord = vragenMaker(1)
if antwoord.lower() == "mbo-4 ondernemen":
    punten += 1

antwoord = vragenMaker(2)
if antwoord.lower() == "vrachtwagen":
    punten += 1

antwoord = vragenMaker(3)
if antwoord.lower() == "ja":
    punten += 1

antwoord = vragenMaker(4)
if antwoord.lower() == "man":
    antwoord = vragenMaker(6)
    if int(antwoord) >= 10:
        punten += 1
elif antwoord.lower() == "vrouw":
    antwoord = vragenMaker(7)
    if int(antwoord) >= 20:
        punten += 1

antwoord = vragenMaker(5)
if antwoord == 0:
    punten = punten

antwoord = vragenMaker(8)
if int(antwoord) > 150:
    punten += 1

antwoord = vragenMaker(9)
if antwoord == 0:
    punten = punten

antwoord = vragenMaker(10)
if int(antwoord) > 90:
    punten += 1

antwoord = vragenMaker(11)
if antwoord.lower() == "ja":
    punten += 1

antwoord = vragenMaker(12)
if antwoord == 0:
    punten = punten

if punten >= 8:
    print("Gefeliciteert! U heeft de baan!")
else:
    print("Helaas! U heeft niet alle qualificaties voor de baan.")