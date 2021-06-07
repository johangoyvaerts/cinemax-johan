from models.vertoning import Vertoning
from os import system
from ansimarkup import ansiprint as print
import prettytable
from DATA.datamanager import Datamanager
from prettytable import PrettyTable
from time import sleep
from menu_en_controle import menu_keuze_controle, menu_opbouw, controle_jn



def ft_vertoning_bewerken():
    while True:
        TO_DO_list= ["Vertoning Verwijderen",  "Vertoning Toevoegen", "Vertoning Actief maken", "Vertoning Non Actief maken", "Vertoninge 2d/3D"]
        TO_DO_list_header = ["keuze", "WAT WIL JE DOEN"]
        system ('cls')    
        x, rijteller = menu_opbouw (TO_DO_list_header, TO_DO_list)
        print (x)
        print (f"<blue>MAAK UW KEUZE AUB (tussen 0 en {rijteller} ) </blue>", end = "")
        keuze = input()
        menu_keuze_controle(rijteller, keuze)
        if keuze == "0":
            break
        if keuze == "1":
            ft_vertoning_verwijderen()
        if keuze == "2":
            ft_vertoning_toevoegen()
        if keuze =="4":
            ft_vertoning_actief_maken()
        if keuze =="5":
            ft_vertoning_non_actief_maken()
        if keuze =="6":
            ft_vertoning_drie_d_wisselen()



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
        print (x)

        #
        # GEEF DE ID VAN DE FILM DIE VERWIJDERD MOET WORDEN
        #
        print ("<red>Welke vertoning moet worden verwijderd ")
        print ("<red>Maak uw keuze (ID) </red> (eindig met enter) ", end ="")
        keuze = input()
        if keuze == "":
            break
        # Enkel de film verwijderen als die in de DB zit!!!
        if int(keuze) in id_list :
            vertoning=dm.vertoning_by_id(int(keuze))
            while True :
        
                print (f"Wenst u {vertoning} toe te VERWIJDEREN. druk j/n ", end = "")
                jn=input()
                logic=controle_jn(jn)
                if logic :
                    break
                continue
    
            if jn.upper() == "J":
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
        print("       <b><GREEN>                                    </GREEN></b>")
        print("       <b><GREEN>        VERTONING TOEVOEGEN         </GREEN></b>")
        print("       <b><GREEN>                                    </GREEN></b>")
        print("<green>\n LET OP\n\n geef de juiste waardes in!!! let op hetgeen gevraagd wordt!!\n\n een ingegeven vertoning is <b>steeds AKTIEF!!</b></green>")
        print(" <green>\ndoor ENTER te drukken verlaat u het menu</green>")
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
        print (f"\n<blue>voor welke film maakt u een vertoning in zaal {zaal} om {uur} (GEEF DE ID!)</blue>", end="")
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
        print ("\n <red>TOEVOEGEN??? j/n </red>")
        jn = input ()
        jn=controle_jn(jn)
        #while jn.upper() != "J" or jn.upper() != "N":
        #    print ("geef de juiste waarde aub? ")
        #    jn = input ("TOEVOEGEN??? j/n ")
        #    continue
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


        
 

def ft_vertoning_actief_maken():
    pass

def ft_vertoning_non_actief_maken():
    pass

def ft_vertoning_drie_d_wisselen():
    pass