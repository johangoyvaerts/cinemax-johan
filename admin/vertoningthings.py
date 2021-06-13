from models.vertoning import Vertoning
from os import system
from ansimarkup import ansiprint as print
import prettytable
from DATA.datamanager import Datamanager
from prettytable import PrettyTable
from time import sleep
#from menu_en_controle import controle_int, menu_keuze_controle, menu_opbouw, controle_jn
from utils.menu_en_contole import controle_int, menu_keuze_controle, menu_opbouw, controle_jn, print_opdrachtregel, print_titel



def ft_vertoning_bewerken():
    while True:
        TO_DO_list= ["Vertoning Verwijderen",  "Vertoning Toevoegen", "Wissel Actief/Non-actief",  "Wissel 2D/3D", "Actieve vertoningen tonen","Alle vertoningen tonen"]
        TO_DO_list_header = ["keuze", "WAT WIL JE DOEN"]
        afsluiten="TERUG NAAR HOODFDMENU"
        system ('cls')    
        print_titel ("VERTONING BEWERKEN")
        x, rijteller = menu_opbouw (TO_DO_list_header, TO_DO_list, afsluiten)
        print (x)
        print_opdrachtregel (f"MAAK UW KEUZE AUB (tussen 0 en {rijteller}) ")
        keuze = input()
        menu_keuze_controle(rijteller, keuze)
        if keuze == "0":
            break
        if keuze == "1":
            ft_vertoning_verwijderen()
        if keuze == "2":
            ft_vertoning_toevoegen()
        if keuze =="3":
            ft_vertoning_actief_non_maken()
        if keuze =="4":
            ft_vertoning_drie_d_wisselen()
        if keuze =="5":
            ft_vertoning_actief_tonen()
        if keuze =="6":
            ft_alle_vertoningen_tonen()



def ft_vertoning_verwijderen():
# indien er tickets van vertoningen bestaan, mag j die niet verwijderen!!! NOG TOEVOEGEN
# indien er tickets van vertoningen bestaan, mag j die niet verwijderen!!! NOG TOEVOEGEN
# indien er tickets van vertoningen bestaan, mag j die niet verwijderen!!! NOG TOEVOEGEN
# indien er tickets van vertoningen bestaan, mag j die niet verwijderen!!! NOG TOEVOEGEN
#    
    keuze = None
    dm=Datamanager()

    while True :
        x= PrettyTable()
        id_list=[]
        x.field_names=(["ID", "zaal", "uur", "2D/3D", "AC/NA", "filmtitel"])

        #
        #  TOON ALLE films
        #
        vertoningen=dm.alle_vertoningen()
        #print (vertoningen)
        #input()
        for vertoning in vertoningen :
            #titel = dm.film_by_id(vertoning.film.id)
            x.add_row([vertoning.id, vertoning.zaal, vertoning.uur, vertoning.drie_d, vertoning.vertoning_actief, vertoning.film.titel])
            # MAAK THEVENS EEN LIJST VAN ALLE ID SIE IN DE DB ZITTEN
            id_list.append(vertoning.id)
        system("cls")
        print_titel ("VERTONING VERWIJDEREN")
        print (x)
        

        #
        # GEEF DE ID VAN DE FILM DIE VERWIJDERD MOET WORDEN
        #
        print ("<red>Welke vertoning moet worden verwijderd ")
        print_opdrachtregel ("Maak uw keuze (ID)  (eindig met enter) ")
        keuze = input()
        if keuze == "":
            break

        keuze = controle_int(keuze)
        while not keuze :
            print_opdrachtregel ("Maak uw keuze (ID)  (eindig met enter) ")
            keuze = input()
            keuze = controle_int(keuze)

        # Enkel de film verwijderen als die in de DB zit!!!
        if int(keuze) in id_list :
            vertoning=dm.vertoning_by_id(int(keuze))
            print (f"Wenst u {vertoning} toe te VERWIJDEREN. druk j/n ", end = "")
            jn=input()
            jn=controle_jn(jn)            
            while not jn :
        
                print (f"Wenst u {vertoning} toe te VERWIJDEREN. druk j/n ", end = "")
                jn=input()
                jn=controle_jn(jn)
                if jn =="N" :
                    break
                continue
    
            if jn == "J":
                print ("\n <red>WORDT VERWIJDERD!!</red>")
                dm.vertoning_verwijderen_by_id(int(keuze))
                sleep (1.5)
            else :
                print (f"\n {vertoning} werd <b><red>NIET</red></b> VERWIJDERD", end ="")
                sleep (2)
            
            
        else :
            print ("<red> vertoning niet in lijst !!! </red>")
            sleep (1.5)
    return
    


def ft_vertoning_toevoegen():
    
    while True :
        zaal = 0
        drie_d =""
        film_id_list =[]
        vertoning_actief=""
        x = PrettyTable()
        dm = Datamanager()
        system ("cls")
        print_titel ("VERTONING TOEVOEGEN")
        print("<green>\n LET OP\n\n geef de juiste waardes in!!! let op hetgeen gevraagd wordt!!\n\n een ingegeven vertoning is <b>steeds AKTIEF!!</b></green>")
        print(" <green>\n door ENTER te drukken verlaat u het menu</green>")
        print("\n<blue>Geef een zaal 1, 2, 3, 4, 5, 6 : </blue>", end="")
        zaal = input()
        if not zaal :
            break
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


        
 

def ft_vertoning_actief_non_maken():
    while True :
        jn=""
        x = PrettyTable()
        x.field_names=(["ID", "zaal", "uur",  "filmtitel", "Act/NON-Act"])
        dm = Datamanager()
        vertoning_list=[]
        system ("cls")
        print_titel ("VERTONING ACTEF/NON-ACTIEF WISSELEN ")
        
        print("<green>\n  Als een vertoning ACTIEF is kan je ze hier op Non-Actief plaatsen\n\n  Geef de juiste waardes in!!! Let op hetgeen gevraagd wordt!! </green>")
        print(" <green>\n  door ENTER te drukken verlaat u het menu</green>") 
        vertoningen=dm.alle_vertoningen()
        for vertoning in vertoningen :
            x.add_row([vertoning.id, vertoning.zaal, vertoning.uur, vertoning.film.titel, "<red>ACTIEF</red>" if vertoning.vertoning_actief =="AC" else "<red>NON-ACTIEF</red>" ])
            vertoning_list.append(vertoning.id)

        print (x)
        print (vertoning_list)
        print ("\n<blue>  Welke vertoning (ID) moet ACTIEF/NON-ACTIEF</blue> ", end="")
        vertoning_ID = input()
        if not vertoning_ID :
            break
        #if not vertoning_ID :
        #    break
        vertoning_ID=controle_int(vertoning_ID)
        while not vertoning_ID :
            print ("\n<blue>  Welke vertoning (ID) moet ACTIEF/NON-ACTIEF</blue> ", end="")
            vertoning_ID = input()
            vertoning_ID=controle_int(vertoning_ID)
            if not vertoning_ID :
                continue            
                
        
        if int(vertoning_ID) in vertoning_list :
            vertoning=dm.vertoning_by_id(int(vertoning_ID))
            #print ("HOERA")
            #input()
            print (f"<blue>   {vertoning} </blue><red>{'AKTIEF' if vertoning.vertoning_actief=='AC' else 'NON-AKTIEF'}</red><blue> Wisselen in</blue> <red>{'NON-AKTIEF' if vertoning.vertoning_actief=='AC' else 'AKTIEF'}</red> <blue>?? (j/n)</blue>", end ="")
            jn=input ()
            #print (jn)
            #input()
            jn=controle_jn(jn)
            while not jn :
                print (f"<blue>   {vertoning} </blue><red>{'AKTIEF' if vertoning.vertoning_actief=='AC' else 'NON-AKTIEF'}</red><blue> Wisselen in</blue> <red>{'NON-AKTIEF' if vertoning.vertoning_actief=='AC' else 'AKTIEF'}</red> <blue>?? (j/n)</blue>", end ="")
                jn=input () 
                jn = controle_jn(jn)               
            if jn =="J":
                if vertoning.vertoning_actief == "AC":
                    print (" <red> WISSELEN </red>")
                    dm.set_vertoning_non_actief_by_id(int(vertoning_ID))
                else :
                    dm.set_vertoning_actief_by_id(int(vertoning_ID))


def ft_vertoning_actief_tonen():

    x = PrettyTable()
    x.field_names=(["ID", "zaal", "uur",  "filmtitel", "Act/NON-Act"])
    dm = Datamanager()
    vertoningen = dm.alle_actieve_vertoningen()
    
    for vertoning in vertoningen :
        x.add_row([vertoning.id, vertoning.zaal, vertoning.uur, vertoning.film.titel, "ACTIEF" ])
    system("cls")
    print_titel("ACTIEVE VERTONINGEN TONEN")
    #x.sortby="zaal"
    print (x)
    input ("\n druk toets")
   

def ft_vertoning_drie_d_wisselen():
    while True :
        jn=""
        x = PrettyTable()
        x.field_names=(["ID", "zaal", "uur", "Act/NON-Act", "filmtitel", "2D / 3D" ])
        dm = Datamanager()
        vertoning_list=[]
        system ("cls")
        print_titel("VERTONING 2D/3D WISSELEN")
        
        print("<green>\n  Als een vertoning 2D is kan je ze hier op 3D plaatsen\n\n  Geef de juiste waardes in!!! Let op hetgeen gevraagd wordt!! </green>")
        print(" <green>\n  door ENTER te drukken verlaat u het menu</green>") 
        vertoningen=dm.alle_actieve_vertoningen()
        for vertoning in vertoningen :
            x.add_row([vertoning.id, vertoning.zaal, vertoning.uur, vertoning.vertoning_actief, vertoning.film.titel, vertoning.drie_d ])
            vertoning_list.append(vertoning.id)

        print (x)
        print (vertoning_list)
        print ("\n<blue>  Welke vertoning (ID) moet 2D / 3D wisselen? </blue> ", end="")
        vertoning_ID = input()
        if not vertoning_ID :
            break
        #if not vertoning_ID :
        #    break
        vertoning_ID=controle_int(vertoning_ID)
        while not vertoning_ID :
            print ("\n<blue>  Welke vertoning (ID) moet 2D / 3D wisselen? </blue> ", end="")
            vertoning_ID = input()
            vertoning_ID=controle_int(vertoning_ID)
            if not vertoning_ID :
                continue            
                
        
        if int(vertoning_ID) in vertoning_list :
            vertoning=dm.vertoning_by_id(int(vertoning_ID))
            #print ("HOERA")
            #input()
            print (f"<blue>   {vertoning} </blue><red>{'2D' if vertoning.drie_d=='2D' else '3D'}</red><blue> Wisselen in</blue> <red>{'3D' if vertoning.drie_d=='2D' else '2D'}</red> <blue>?? (j/n)</blue>", end ="")
            jn=input ()
            #print (jn)
            #input()
            jn=controle_jn(jn)
            while not jn :
                print (f"<blue>   {vertoning} </blue><red>{'2D' if vertoning.drie_d=='2D' else '3D'}</red><blue> Wisselen in</blue> <red>{'3D' if vertoning.drie_d=='2D' else '3D'}</red> <blue>?? (j/n)</blue>", end ="")
                jn=input () 
                jn = controle_jn(jn)               
            if jn =="J":
                if vertoning.drie_d == "2D":
                    print (" <red> WISSELEN </red>")
                    dm.set_vertoning_3D_by_id(int(vertoning_ID))
                else :
                    dm.set_vertoning_2D_by_id(int(vertoning_ID))


def ft_alle_vertoningen_tonen():

    x = PrettyTable()
    x.field_names=(["ID", "zaal", "uur",  "filmtitel", "Act/NON-Act", "2D/3D"])
    dm = Datamanager()
    vertoningen = dm.alle_vertoningen()
    
    for vertoning in vertoningen :
        x.add_row([vertoning.id, vertoning.zaal, vertoning.uur, vertoning.film.titel, vertoning.vertoning_actief, vertoning.drie_d ])
    system("cls")
    print_titel("ALLE VERTONINGEN TONEN")
    print (x)
    input ("\n druk toets")
    