# Python 2.x
# Librerie
import random


# Banner
def banner():
    print '''
 _____                           _                     _               __  __          _____       _           _  
/ ____|                         | |                   | |             |  \/  |        |  __ \    | |         | |  
| |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ ___    | |__  _   _    | \ / |_ __    | |__) |___ | |__   ___ | |_
| | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__/ _ \  | '_ \| | | |   | |\/| | '__|   |  _  // _ \| '_ \ / _ \| __|
| |__| |  __/ | | |  __/ | | (_| | || (_) | | |  __/   | |_) | |_| |   | |  | | |      | | \ \ (_) | |_) | (_) | |_
\_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|  \___|   |_.__/ \__, |   |_|  |_|_|      |_|  \_\___/|_.__/ \___/ \__|
                                                              __/ |                                            
                                                             |___/
'''





def genera():
    print "\n"
    while True:
        scelta = raw_input("Che tipo di account vuoi generare?" +
                           "\n 1 - Spotify" +
                           "\n 2 - Twitter" +
                           "\n 3 - Instagram" +
                           "\n 4 - Pandora" +
                           "\n 5 - Generatore Premium" +
                           "\n 6 - Torna indietro ")

        if scelta == "1":
            array = ['business@christianpf.com:AGEbob11', 'jonelley33@hotmail.com:gymnast33',
                     'rtwalker1@gmail.com:yogurt45', 'rtwalker1@gmail.com:yogurt45' 'rtwalker1@gmail.com:yogurt45', 'vtkachev@gmail.com:warlock', 'business@christianpf.com:AGEbob11', 'caseyprice@gmail.com:Starwars1', 'codygman.consulting@gmail.com:dbowen12', 'javiergarza4@gmail.com:solo1212', 'jay.wiles@gmail.com:orangekiwi100', 'Mrawson0928@yahoo.com:Ghost1472']
            stampa(array)
            break
        elif scelta == "2":
            array = ['kmeyer25@optonline.net:ultra2', 'thecantwells@att.net:browndog', 'alanreid99@yahoo.com:arwtn901',
                     'manuelfraunholz@yahoo.de:wasser4321', 'geemee_2001@yahoo.com:dg121803', 'Naora87@web.de:daja2005']
            stampa(array)
            break
        elif scelta == "3":
            array = ['Coming soon']
            stampa(array)
            break
        elif scelta == "4":
            array = ['kwallye@yahoo.com:boh3m3', 'alacang211@aol.com:Agent211', 'erinlikesblue@gmail.com:therealme', 'auryn1026@gmail.com:denial', 'rincon012000@yahoo.com:gbpackers260', 'classictaste101@aol.com:trust1', 'twitterpaited08@aol.com:kody2005', 'farrisadam15@yahoo.com:asdf12', 'fl6timber@msn.com:ruano214']
            stampa(array)
            break
        elif scelta == "5":
            array = ['Cooming Soon']
            stampa(array)
            break
        elif scelta == "6":
            break
        else:
            print "Errore: scelta non valida"


# Stampa random un elemento di un array ricevuto come parametro
def stampa(array):
    print "\n"
    secure_random = random.SystemRandom()
    print secure_random.choice(array)


# Richiesta di continuazione
def menu():
    print "\n"
    while True:
        continua = raw_input("Vuoi generare un altro account (y/n)? ")
        if continua == "y":
            return 1
        elif continua == "n":
            return 0
        else:
            print "Errore: scelta non valida. Devi scrivere 'y' o 'n'"


# Main
banner()
while True:
    genera()
    if menu() == 0:
        break
