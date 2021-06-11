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

        print("<green>\n LET OP\n\n geef de juiste waardes in!!! let op hetgeen gevraagd wordt!!\n </green>")
        print(" <green>\n door ENTER te drukken verlaat u het menu</green>")
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
            
            vertoningen = dm.vertoning_by_film_id(int(film_id))
            x=PrettyTable()
            x.field_names = ["id","zaal","uur", "KNT"]
            for vertoning in vertoningen :
                
                #
                # toon al de vertoningen van vandaag van de film
                vertoning_id_list.append(vertoning.id)
                x.add_row([vertoning.id,vertoning.zaal, vertoning.uur, vertoning.film.knt])
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
                    print ("<red> wordt toegevoegd</red>")
                    #ticket = Ticket(datum,prijs_volw, prijs_kind, aant_volw,aant_kind, vertoning)
                    dm.ticket_toevoegen(ticket)
                    print_opdrachtregel("\n Even Wachten")
                    sleep (1)
                    print ("<red>ticket printen? j/n</red>")
                    jn=input()
                    jn=controle_jn(jn)
                    while not jn :
                        print ("<red>ticket printen? j/n</red>")
                        jn=input()
                        jn=controle_jn(jn)
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
        
       
"""        
        
        print ("\n<blue>Geef een uur formaat HH00 of HH30 : </blue>", end ="")
        uur = input()
        if not uur : 
            break
        print("\n<blue>Geef 2D of 3D : </blue>", end="")
        drie_d = input ()
        if not drie_d :
            break
        vertoning_actief= "AC"
        films=dm.alle_films()
        for film in films :
            x.add_row([film.id, film.titel])
            film_id_list.append(film.id)
        print (x)    
        print (f"\n<blue> voor welke film maakt u een vertoning in zaal {zaal} om {uur} (GEEF DE ID!)</blue>", end="")
        film_id= input()
        if not film_id :
            break
        film= dm.film_by_id(film_id)
        try :
            vertoning= Vertoning(zaal, uur, drie_d, vertoning_actief, film)
        except ValueError :
            print ("\n<RED>  GEEF de JUISTE WAARDES IN!!!  </RED>")
            sleep (2)
            continue
        print (f"\n  voor {film.titel.upper()} wil u een vertoning in zaal {vertoning.zaal} om {vertoning.uur}??")
        print ("\n TOEVOEGEN??? (j/n) ", end="")
        jn = input ()
        jn=controle_jn(jn)
        if jn == "J" :
            print (f"\n<green> {vertoning} TOEVOEGEN !</green>")
            dm.vertoning_toevoegen(vertoning)
            sleep(1)
            
        else :
            print (f"\n<red> {vertoning} werd <b>NIET</b> TOEGVOEGD</red>")
            sleep (2)
            continue
        print("\n nog vertoningen invoeren j/n? ", end="")
        jn= input ()
        jn = controle_jn(jn)
        if jn == "N":
            break


        """