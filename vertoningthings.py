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
    ZALEN = [1, 2, 3, 4, 5, 6]
    SETTING = ["2D","3D"]
    VERT_ACT = ["AC", "NA"]
    zaal = 0


    while True :
        zaal = 0
        drie_d =""
        vertoning_actief=""
        x = PrettyTable()
        dm = Datamanager()
        while zaal not in ZALEN :
            zaal = int(input("Geef een getal 1, 2, 3, 4, 5, 6 "))

        
        uur = int(input("uur"))
        
        drie_d = input ("2D/3D")
        
        vertoning_actief= input("AC/NC")
        
        films=dm.alle_films()
        for film in films :
            x.add_row([film.id, film.titel])
        print (x)    
        print ("selecteer film")
        film_id= input()
        
        film= dm.film_by_id(film_id)
        vertoning= Vertoning(zaal, uur, drie_d, vertoning_actief, film)
        dm.vertoning_toevoegen(vertoning)
        jn= input ("jn")
        if jn == "n":
            break


        
 

def ft_vertoning_actief_maken():
    pass

def ft_vertoning_non_actief_maken():
    pass

def ft_vertoning_drie_d_wisselen():
    pass