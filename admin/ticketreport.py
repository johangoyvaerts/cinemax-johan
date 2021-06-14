from os import system 
from utils.menu_en_contole import controle_datum, controle_int, controle_jn, geef_prijs_per_soort, print_opdrachtregel, print_titel, menu_opbouw, menu_keuze_controle, bepaal_prijs
from prettytable import PrettyTable
from DATA.datamanager import Datamanager
from models.film import Film
from ansimarkup import ansiprint as print
from time import sleep
from models.ticket import Ticket
from datetime import date, datetime
import locale
locale.setlocale(locale.LC_ALL,"")
import csv

def ft_ticket_rapport():
    while True:
        TO_DO_list= ["Ticket Rapport Film",  "Ticket Rapport Tijdsinterval", "Ticket Rapport Tijdsinteval Film", "Ticket Totaal Rapport"]
        TO_DO_list_header = ["keuze", "WAT WIL JE DOEN"]
        afsluiten="TERUG NAAR TICKET MENU"
        system ('cls')    
        print_titel ("TICKETS RAPPORTEN")
        x, rijteller = menu_opbouw (TO_DO_list_header, TO_DO_list, afsluiten)
        print (x)
        print_opdrachtregel (f"MAAK UW KEUZE AUB (tussen 0 en {rijteller}) ")
        keuze = input()
        menu_keuze_controle(rijteller, keuze)
        if keuze == "0":
            break
        if keuze == "1":
            ft_ticket_rapport_film()
        if keuze == "2":
            ft_ticket_rapport_tijdsinterval()
        if keuze == "3":
            ft_ticket_rapport_tijdsinterval_film()  
        if keuze == "4":
            ft_ticket_rapport_totaal()          
 

def ft_ticket_rapport_film():
    keuze = None
    dm=Datamanager()

    # toon alle films
    
    x= PrettyTable()
    id_list=[]
    x.field_names=(["ID", "TITEL"])
    #
    #  TOON ALLE films
    #
    films=dm.alle_films()
    for film in films :
        x.add_row([film.id, film.titel])
        # MAAK THEVENS EEN LIJST VAN ALLE ID DIE IN DE DB ZITTEN
        id_list.append(film.id)
    system("cls")
    print_titel("RAPPORT FILM")
    print (x)
    #
    # GEEF DE ID VAN DE FILM 
    #
    print_opdrachtregel("Van welke film wil je een rapport ")
    print_opdrachtregel ("Maak uw keuze (ID) (eindig met enter) ")
    keuze = input()
    if keuze == "":
        return
    keuze = controle_int(keuze)
    while not keuze :
        print_opdrachtregel ("Maak uw keuze (ID) (eindig met enter) ")
        keuze = input()
        keuze = controle_int(keuze)
    ticket=dm.tickets_by_film_id(int(keuze))
    if not ticket :
        print (" van deze film werden nog geen tickets verkocht")
        print_opdrachtregel ("druk toets")
        input ()
        return
    tot_prijs_volw = 0
    tot_prijs_kind = 0
    tot_aant_volw=0
    tot_aant_kind=0
    totaal_prijs=0
    totaal_aant_personen=0
    system('cls')
    
    
    print_titel ("TICKET RAPPORT FILM")
    #print (f"\nINFO : Enkel de tickets van vandaag <b>{datum}</b> kunnen worden verwijderd\n")
    #print ("De verwijderde tickets worden bewaard in bestand!!!\n")

    #print_opdrachtregel ("Waarom wenst u het ticket te verwijderen? (geef een korte beschrijving (nihil : eindig met enter))")
    #reden = input ()
    #if reden =="":
    #    return
    x= PrettyTable()
    id_list=[]
    x.field_names=([ "Tot. Prijs Volw", "TotPrijs Kind", "Tot. Aant Volw", "Tot. Aant Kind"])
    #
    #  TOON ALLE Tickets van VANDAAG
    #
    tickets=dm.tickets_by_film_id(int(keuze))
    for ticket in tickets :
        tot_prijs_volw = geef_prijs_per_soort(tot_prijs_volw,float(ticket.prijs_volw),int(ticket.aant_volw))
        tot_prijs_kind = geef_prijs_per_soort(tot_prijs_kind,float(ticket.prijs_kind),int(ticket.aant_kind))
        tot_aant_volw+=int(ticket.aant_volw)
        tot_aant_kind+=int(ticket.aant_kind)
    totaal_prijs=(tot_prijs_volw+tot_prijs_kind)
    totaal_aant_personen=(tot_aant_volw+tot_aant_kind)
        
        
    system("cls")
    print_titel ("TICKET FILM RAPPORT")
    x.add_row([tot_prijs_volw, tot_prijs_kind, tot_aant_volw, tot_aant_kind])
    print (x)
    print ()
    print (f"    TOTAAL voor {ticket.vertoning.film.titel}:           {totaal_prijs:>5.2f}€          {totaal_aant_personen} personen")
    print_opdrachtregel("Druk een toets")
    input()
    return


def ft_ticket_rapport_tijdsinterval():
    
    dm=Datamanager()
    system ('cls')

    

    datum1 = input("geef de eerste datum (formaat YYYY-MM-DD) ")
    if datum1=="":
        return
    datum1= controle_datum (datum1)
    while not datum1 :
        datum1 = input("geef de eerste datum (formaat YYYY-MM-DD) ")

        datum1= controle_datum (datum1)  
              
    


    datum2 = input("geef de tweede datum (formaat YYYY-MM-DD) ")
    if datum2=="":
        return
    datum2= controle_datum (datum2)
    while not datum2 :
        datum2 = input("geef de tweede datum (formaat YYYY-MM-DD) ")

        datum2= controle_datum (datum2)





    tot_prijs_volw = 0
    tot_prijs_kind = 0
    tot_aant_volw=0
    tot_aant_kind=0
    totaal_prijs=0
    totaal_aant_personen=0
    system('cls')
    
    
    print_titel ("TICKET RAPPORT TIJDSINTERVAL")
    #print (f"\nINFO : Enkel de tickets van vandaag <b>{datum}</b> kunnen worden verwijderd\n")
    #print ("De verwijderde tickets worden bewaard in bestand!!!\n")

    #print_opdrachtregel ("Waarom wenst u het ticket te verwijderen? (geef een korte beschrijving (nihil : eindig met enter))")
    #reden = input ()
    #if reden =="":
    #    return
    x= PrettyTable()
    id_list=[]
    x.field_names=([ "Tot. Prijs Volw", "TotPrijs Kind", "Tot. Aant Volw", "Tot. Aant Kind"])
    #
    #  TOON ALLE Tickets van VANDAAG
    #
    tickets=dm.tickets_tss_data(datum1, datum2)
    for ticket in tickets :
        tot_prijs_volw = geef_prijs_per_soort(tot_prijs_volw,float(ticket.prijs_volw),int(ticket.aant_volw))
        tot_prijs_kind = geef_prijs_per_soort(tot_prijs_kind,float(ticket.prijs_kind),int(ticket.aant_kind))
        tot_aant_volw+=int(ticket.aant_volw)
        tot_aant_kind+=int(ticket.aant_kind)
    totaal_prijs=(tot_prijs_volw+tot_prijs_kind)
    totaal_aant_personen=(tot_aant_volw+tot_aant_kind)
        
        
    system("cls")
    print_titel ("TICKET RAPPORT TIJDSINTERVAL")
    x.add_row([tot_prijs_volw, tot_prijs_kind, tot_aant_volw, tot_aant_kind])
    print (x)
    print ()
    print (f"    TOTAAL voor {datum1} tot {datum2}:           {totaal_prijs:>5.2f}€          {totaal_aant_personen} personen")
    print_opdrachtregel("Druk een toets")
    input()
    return 


def ft_ticket_rapport_tijdsinterval_film():
    
    dm=Datamanager()
    system ('cls')

    

    datum1 = input("geef de eerste datum (formaat YYYY-MM-DD) ")
    if datum1=="":
        return
    datum1= controle_datum (datum1)
    while not datum1 :
        datum1 = input("geef de eerste datum (formaat YYYY-MM-DD) ")

        datum1= controle_datum (datum1)  
              
    


    datum2 = input("geef de tweede datum (formaat YYYY-MM-DD) ")
    if datum2=="":
        return
    datum2= controle_datum (datum2)
    while not datum2 :
        datum2 = input("geef de tweede datum (formaat YYYY-MM-DD) ")

        datum2= controle_datum (datum2)


    tickets = dm.tickets_tss_data(datum1,datum2)
    keuze = None


    
    x= PrettyTable()
    id_list=[]
    x.field_names=(["ID", "TITEL"])
    #
    #  TOON ALLE films
    #
    
    for ticket in tickets :
        if ticket.vertoning.film.id not in id_list :
            x.add_row([ticket.vertoning.film.id, ticket.vertoning.film.titel])
            # MAAK THEVENS EEN LIJST VAN ALLE ID DIE IN DE DB ZITTEN
            id_list.append(ticket.vertoning.film.id)
    system("cls")
    print_titel("FILM RAPPORT TIJDSINTERVAL")
    print (x)
    #
    # GEEF DE ID VAN DE FILM DIE JE WIL RAPPORTEREN
    #
    
    print_opdrachtregel ("Maak uw keuze (ID) (eindig met enter) ")
    keuze = input()
    if keuze == "":
        return
    keuze = controle_int(keuze)
    while not keuze :
        print_opdrachtregel ("Maak uw keuze (ID) (eindig met enter) ")
        keuze = input()
        keuze = controle_int(keuze)
    #
    # nagaan of de film in een vertoning is opgenomen
    # indien ja : niet verwijderen omdat er misschien tickets van verkocht zijn!!! 
    # anders is de link tussen het Ticket en de film verloren en kan men niet meer de omzet
    # per film opvragen!! 

    if int(keuze) in id_list :
        ticket=dm.tickets_film_tss_data(datum1,datum2,int(keuze))




    tot_prijs_volw = 0
    tot_prijs_kind = 0
    tot_aant_volw=0
    tot_aant_kind=0
    totaal_prijs=0
    totaal_aant_personen=0
    system('cls')
    
    
    print_titel ("TICKET RAPPORT TIJDSINTERVAL")
    #print (f"\nINFO : Enkel de tickets van vandaag <b>{datum}</b> kunnen worden verwijderd\n")
    #print ("De verwijderde tickets worden bewaard in bestand!!!\n")

    #print_opdrachtregel ("Waarom wenst u het ticket te verwijderen? (geef een korte beschrijving (nihil : eindig met enter))")
    #reden = input ()
    #if reden =="":
    #    return
    x= PrettyTable()
    id_list=[]
    x.field_names=([ "Tot. Prijs Volw", "TotPrijs Kind", "Tot. Aant Volw", "Tot. Aant Kind"])
    #
    #  TOON ALLE Tickets van VANDAAG
    #
    tickets=dm.tickets_film_tss_data(datum1, datum2, int(keuze))
    for ticket in tickets :
        tot_prijs_volw = geef_prijs_per_soort(tot_prijs_volw,float(ticket.prijs_volw),int(ticket.aant_volw))
        tot_prijs_kind = geef_prijs_per_soort(tot_prijs_kind,float(ticket.prijs_kind),int(ticket.aant_kind))
        tot_aant_volw+=int(ticket.aant_volw)
        tot_aant_kind+=int(ticket.aant_kind)
    totaal_prijs=(tot_prijs_volw+tot_prijs_kind)
    totaal_aant_personen=(tot_aant_volw+tot_aant_kind)
        
        
    system("cls")
    print_titel ("TICKET RAPPORT TIJDSINTERVAL")
    x.add_row([tot_prijs_volw, tot_prijs_kind, tot_aant_volw, tot_aant_kind])
    print (x)
    print ()
    print (f"    TOTAAL voor {datum1} tot {datum2}:           {totaal_prijs:>5.2f}€          {totaal_aant_personen} personen")
    print_opdrachtregel("Druk een toets")
    input()
    return 


def ft_ticket_rapport_totaal():
    tot_prijs_volw = 0
    tot_prijs_kind = 0
    tot_aant_volw=0
    tot_aant_kind=0
    totaal_prijs=0
    totaal_aant_personen=0
    system('cls')
    keuze = None
    dm=Datamanager()
    #vandaag = datetime.now()
    #datum = vandaag.strftime("%Y-%m-%d")
    print_titel ("TICKET TOTAAL RAPPORT")
    #print (f"\nINFO : Enkel de tickets van vandaag <b>{datum}</b> kunnen worden verwijderd\n")
    #print ("De verwijderde tickets worden bewaard in bestand!!!\n")

    #print_opdrachtregel ("Waarom wenst u het ticket te verwijderen? (geef een korte beschrijving (nihil : eindig met enter))")
    #reden = input ()
    #if reden =="":
    #    return
    x= PrettyTable()
    id_list=[]
    x.field_names=([ "Tot. Prijs Volw", "TotPrijs Kind", "Tot. Aant Volw", "Tot. Aant Kind"])
    #
    #  TOON ALLE Tickets van VANDAAG
    #
    tickets=dm.alle_tickets()
    for ticket in tickets :
        tot_prijs_volw = geef_prijs_per_soort(tot_prijs_volw,float(ticket.prijs_volw),int(ticket.aant_volw))
        tot_prijs_kind = geef_prijs_per_soort(tot_prijs_kind,float(ticket.prijs_kind),int(ticket.aant_kind))
        tot_aant_volw+=int(ticket.aant_volw)
        tot_aant_kind+=int(ticket.aant_kind)
    totaal_prijs=(tot_prijs_volw+tot_prijs_kind)
    totaal_aant_personen=(tot_aant_volw+tot_aant_kind)
        
        
    system("cls")
    print_titel ("TICKET TOTAAL RAPPORT")
    x.add_row([tot_prijs_volw, tot_prijs_kind, tot_aant_volw, tot_aant_kind])
    print (x)
    print ()
    print (f"    TOTAAL :           {totaal_prijs:>5.2f}€          {totaal_aant_personen} personen")
    print_opdrachtregel("Druk een toets")
    input()
    return