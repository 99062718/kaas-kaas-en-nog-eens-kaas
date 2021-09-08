vragenNummer = 0

kaasVragen = [
    "Is de kaas geel?",
    "Zitten er gaten in?",
    "Is de kaasbelachelijk duur?",
    "Is de kaas hard als steen?",
    "Heeft de kaas blauwe schimmel?",
    "Heeft de kaas een korst?",
    "Heeft de kaas een korst?"
]

kaasSoorten = [
    "Emmenthaler",
    "Leerdammer",
    "Parmigiano Reggiano",
    "Goudse kaas",
    "Bleu de Rochbaron",
    "Fourme d'Ambert",
    "Camembert",
    "Mozzarella"
]

def vragenMaker(jaNummer, neeNummer, kaasJa, kaasNee):
    global vragenNummer

    antwoord = input(kaasVragen[vragenNummer] + "\n").lower()
    if antwoord == "ja":
        vragenNummer += jaNummer
        kaas = kaasJa
    elif antwoord == "nee":
        vragenNummer += neeNummer
        kaas = kaasNee
    else:
        print("Dit is geen mogelijk antwoord! Beantwoord deze vraag alleen met ja of nee.")
        vragenMaker(jaNummer, neeNummer, kaasNee, kaasJa)

    if kaas is not None:
        kaasAntwoord(kaas)

def kaasAntwoord(kaas):
    print("Uw beschreven kaas is: " + kaasSoorten[kaas] + "!")

vragenMaker(1, 4, None, None)

vragenMaker(1, 2, None, None)

if vragenNummer == 2:
    vragenMaker(0, 0, 0, 1)
elif vragenNummer == 3:
    vragenMaker(0, 0, 2, 3)
elif vragenNummer == 5:
    vragenMaker(0, 0, 4, 5)
elif vragenNummer == 6:
    vragenMaker(0, 0, 6, 7)
