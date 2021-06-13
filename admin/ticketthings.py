from os import system 
from utils.menu_en_contole import controle_int, controle_jn, print_opdrachtregel, print_titel, menu_opbouw, menu_keuze_controle, bepaal_prijs
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



def ft_ticket_bewerken():
    while True:
        TO_DO_list= ["Ticket verkopen",  "Ticket verwijderen", "Tickets tonen"]
        TO_DO_list_header = ["keuze", "WAT WIL JE DOEN"]
        afsluiten="TERUG NAAR VORIG MENU"
        system ('cls')    
        print_titel ("TICKETS BEWERKEN")
        x, rijteller = menu_opbouw (TO_DO_list_header, TO_DO_list, afsluiten)
        print (x)
        print_opdrachtregel (f"MAAK UW KEUZE AUB (tussen 0 en {rijteller}) ")
        keuze = input()
        menu_keuze_controle(rijteller, keuze)
        if keuze == "0":
            break
        if keuze == "1":
            ft_ticket_verkopen()
        if keuze == "2":
            ft_ticket_verwijderen()


def ft_ticket_verkopen():

    
    while True :
        vandaag = datetime.now()
        datum = vandaag.strftime("%Y-%m-%d")
 
        aant_kind = 0
        aant_volw = 0        
        ticket_id_list =[]
        film_id_list = []
        vertoning_id_list=[]

        x = PrettyTable()

        x.field_names=['ID', "film titel", "duur", "KT/KNT"]

        dm = Datamanager()
        system ("cls")
        print_titel ("Ticket VErkopen")

        print("<green>\n LET OP\n\n geef de juiste waardes in!!! let op hetgeen gevraagd wordt!! </green>")
        print(" <green>\n door ENTER te drukken verlaat u het menu</green>\n")
        #
        # toon alle actieve vertoningen
        #
        vertoningen = dm.alle_actieve_vertoningen()
        for vertoning in vertoningen :
            #print (vertoning)
            #print (vertoning.film.id)
            #
            # toon de actieve films slechts 1 maal (sppelt misschien in meerdere zalen en tijdstippen...)
            if vertoning.film.id not in film_id_list :
                film_id_list.append(vertoning.film.id)
                x.add_row([vertoning.film.id,vertoning.film.titel,vertoning.film.duurtijd, "NO-KIDS" if vertoning.film.knt=="KNT" else "KIDS Allowed"])
            #print (dm.film_by_id(vertoning.film.id))
        x.sortby="film titel"
        print (x)
        #print (film_id_list)
        print_opdrachtregel("geef de ID van de film die je wil kijken")
        film_id=input()
        #
        # terug naar vorig minu indien geen input
        if not film_id :
            break 
        #
        # controleren of film_id een integer is
        #  
        film_id=controle_int(film_id)
        while not film_id :
            print_opdrachtregel("geef de ID van de film die je wil kijken")
            film_id=input()
            film_id=controle_int(film_id) 
        #
        # enkel indien de film ID in de filmID_list voorkomt mogen we verder gaan
        # de film speelt niet indien hij niet in deze lijst zit!!!
        #
        if int(film_id) in film_id_list :
            
            vertoningen = dm.vertoning_actief_by_film_id(int(film_id))
            x=PrettyTable()
            x.field_names = ["id","zaal","uur", "KNT", "2D/3D"]
            for vertoning in vertoningen :
                
                #
                # toon al de vertoningen van vandaag van de film
                vertoning_id_list.append(vertoning.id)
                x.add_row([vertoning.id,vertoning.zaal, vertoning.uur, vertoning.film.knt, vertoning.drie_d])
            x.sortby="uur"    
            system ('cls')
            print_titel(f" {vertoning.film.titel} ZAALKEUZE ")
            print (x)
            #print (vertoning_id_list)
            print_opdrachtregel("geef de ID van de vertoning die je wil kijken")
            vertoning_id=input()
            #
            # terug naar vorig minu indien geen input
            if not vertoning_id :
                break 
            #
            # controleren of vertoning_id een integer is
            #  
            vertoning_id=controle_int(vertoning_id)
            # als de vertoning niet in de lijst van vertoningen zit...
            #if int(vertoning_id) not in vertoning_id_list :
            #    vertoning_id=None
            while not vertoning_id or (int(vertoning_id) not in vertoning_id_list):
                print_opdrachtregel("geef de ID van de vertoning die je wil kijken")
                vertoning_id=input()
                vertoning_id=controle_int(vertoning_id) 
            #    if int(vertoning_id) not in vertoning_id_list :
            #        vertoning_id=None
            #while vertoning_id not in vertoning_id_list :
            # de volgende if is niet nodig!!!
            # op deze plaats zit de vertoning_id zowiezo in de vertoning_id_list    
            if int(vertoning_id) in vertoning_id_list:
                vertoning = dm.vertoning_by_id(vertoning_id)
                system ('cls')
                print (vertoning)
                print_titel ("TICKETVERKOOP")
                prijs_volw, prijs_kind = bepaal_prijs (vertoning)
                print (f"{prijs_volw:>5.2f}€/VOLW.    ", end="")
                print(f"{prijs_kind:>5.2f}€/KIND" if vertoning.film.knt == "KT" else "")
                print_opdrachtregel("geef het aantal volwassenen")
                aant_volw = input()
                aant_volw=controle_int(aant_volw)
                while not aant_volw :
                    print_opdrachtregel("geef het aantal volwassenen")
                    aant_volw = input()
                    aant_volw=controle_int(aant_volw)                
                if vertoning.film.knt == 'KT':
                    print_opdrachtregel("geef het aantal kinderen")
                    aant_kind = input()
                    while not aant_volw :
                        print_opdrachtregel("geef het aantal kinderen")
                        aant_kind = input()
                        aant_kind=controle_int(aant_kind) 
                #indien KNT dan prijs kind op nul
                else : 
                    prijs_kind= 0

                prijs = int(aant_kind)*prijs_kind+ int(aant_volw)*prijs_volw
                #print (prijs_volw,aant_volw)

                print (f"totaal :   ", f"{prijs:5.2f}   ", datum)
                print_opdrachtregel (f"verkoop {vertoning} j/n?")
                jn = input()
                jn = controle_jn (jn)
                while not jn :
                
                    print (f"verkoop {vertoning} j/n?")
                    jn=input()
                    jn=controle_jn(jn)
                ticket = Ticket(datum,str(prijs_volw), str(prijs_kind), str(aant_volw),str(aant_kind), vertoning)
                if jn == 'J':
                    system('cls')
                    print (f"<red> {ticket.vertoning.film.titel} wordt toegevoegd</red>")
                    #ticket = Ticket(datum,prijs_volw, prijs_kind, aant_volw,aant_kind, vertoning)
                    #print(f"ticketteke toevoegen man {ticket}")
                    #input()
                    dm.ticket_toevoegen(ticket)
                    print_opdrachtregel("\n Even Wachten")
                    sleep (1)
                    system ('cls')
                    print ("<red>ticket printen? j/n</red>")
                    jn=input()
                    jn=controle_jn(jn)
                    while not jn :
                        print ("<red>ticket printen? j/n</red>")
                        jn=input()
                        jn=controle_jn(jn)
                    if jn == "J":
                        system ('cls')
                        print (ticket)
                        print_opdrachtregel("\n Even Wachten")
                        sleep (4)

                else :
                    print (f"{ticket} <red>wordt niet toegevoegd!!!</red>")
                    print_opdrachtregel("\n Even Wachten")
                    sleep (2)
       


        else :
            print ("deze film speelt niet maakt korrecte keuze aub!!!")
            sleep (2) 
            continue   
        

def ft_ticket_verwijderen():
    system('cls')
    keuze = None
    dm=Datamanager()
    vandaag = datetime.now()
    datum = vandaag.strftime("%Y-%m-%d")
    print_titel ("TICKET VERWIJDEREN")
    print (f"\nINFO : Enkel de tickets van vandaag <b>{datum}</b> kunnen worden verwijderd\n")
    print ("De verwijderde tickets worden bewaard in bestand!!!\n")

    print_opdrachtregel ("Waarom wenst u het ticket te verwijderen? (geef een korte beschrijving (nihil : eindig met enter))")
    reden = input ()
    if reden =="":
        return
    x= PrettyTable()
    id_list=[]
    x.field_names=(["ID", "Prijs Volw", "Prijs Kind", "Aant Volw", "Aant Kind", "zaal", "filmtitel"])
    #
    #  TOON ALLE Tickets van VANDAAG
    #
    tickets=dm.tickets_vandaag(datum)
    for ticket in tickets :
        
        x.add_row([ticket.id, ticket.prijs_volw, ticket.prijs_kind, ticket.aant_volw, ticket.aant_kind, ticket.vertoning.zaal, ticket.vertoning.film.titel])
        # MAAK THEVENS EEN LIJST VAN ALLE ID dIE IN DE DB ZITTEN
        id_list.append(ticket.id)
    system("cls")
    print_titel ("TICKET VERWIJDEREN")
    print (x)
    
    #
    # GEEF DE ID VAN het ticket dat VERWIJDERD MOET WORDEN
    #
    print ("<red>Welk ticket moet worden verwijderd ")
    print_opdrachtregel ("Maak uw keuze (ID)  (eindig met enter) ")
    keuze = input()
    if keuze == "":
        return

    keuze = controle_int(keuze)

    while not keuze :
        print_opdrachtregel ("Maak uw keuze (ID)  (eindig met enter) ")
        keuze = input()
        keuze = controle_int(keuze)
    # Enkel de Ticket verwijderen als die in de DB zit!!!

    if int(keuze) in id_list :
        ticket=dm.ticket_by_id(int(keuze))
        print (f"Wenst u {ticket} toe te VERWIJDEREN. druk j/n ", end = "")
        jn=input()
        jn=controle_jn(jn)            
        while not jn :
    
            print (f"Wenst u {ticket} toe te VERWIJDEREN. druk j/n ", end = "")
            jn=input()
            jn=controle_jn(jn)
            if jn =="N" :
                break
            continue

        if jn == "J":
            print ("\n <red>WORDT VERWIJDERD!!</red>")
            # Ticket ophalen wat verwijderd dient te worden!!
            ticket = dm.ticket_by_id(int(keuze))
            sleep (1.5)
            # verwijderde Tickets wegschrijven in bestand om fraude van de kassier tegen te gaan
            # de manager kan dat steeds nakijken waarom welke tickets verwijderd werden....
            with open("DATA/verwijderde_tickets.csv","a",newline="")as bestand :
                schrijver=csv.writer(bestand)
                ticket_lijst =[
                    ticket.id, 
                    ticket.datum, 
                    ticket.aant_volw, 
                    ticket.aant_kind,
                    ticket.vertoning.zaal,
                    ticket.vertoning.film.titel,
                    reden

                ]
                schrijver.writerow(ticket_lijst)
            dm.ticket_verwijderen_by_id(int(keuze))    
        else :
            print (f"\n {ticket} werd <b><red>NIET</red></b> VERWIJDERD", end ="")
            sleep (2)
        
        
    else :
        print ("<red> ticket niet in lijst !!! </red>")
        sleep (1.5)
    return
        
        
