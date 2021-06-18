
from DATA.datamanager import Datamanager
from os import system
import requests
from models.film import Film
from ansimarkup import ansiprint as print
from time import sleep
from prettytable import PrettyTable
from utils.menu_en_contole import controle_int, controle_jn, menu_opbouw, menu_keuze_controle,get_api_key, print_opdrachtregel, print_titel
from PIL import Image
import os

def ft_film_toevoegen():
    api_key= get_api_key()
    dm=Datamanager()
    jn=""
    endpoint1 = "https://api.themoviedb.org/3/movie/"
    endpoint2 ="?api_key="+api_key+"&language=nl&region=BE"
    #print (endpoint2)
    while True :
        system ("cls")
        print_titel("FILM TOEVOEGEN MET TMDB ID")
        print_opdrachtregel("Geef het Movie Data Base id aub ? (eindig met ENTER) ")
        MDB_id=input ()
        film=dm.film_by_MDB_id(MDB_id)
        
        # nakijken of film al in de datebase zit
        # indien ja : niet toevoegen
        if film : 
            print(f"\n <b><RED> BESTAAT AL IN DATABASE!!!</RED></b>\n \n <red>kan '{film.titel.upper()}' <b>NIET</b> toevoegen!!!!!!</red>")
            print_opdrachtregel("druk op toets")
            input ()
        else :

            #als enter wordt ingedrukt zonder een ingave, stoppen we deze funktie
            if MDB_id == "":
                return
            response= requests.get(endpoint1+MDB_id+endpoint2)
            # als de film bestaat , dan gaan we ermee aan de slag anders brengen we film niet gevonden op het scherm.
            if response.status_code == 200:
                movie_dict=response.json()
                #print (json.dumps(movie_dict, indent=2))

                film = Film.from_movie_dict(movie_dict) 
                while True :

                    print (f"\n Wenst u {film} toe te voegen. druk j/n ", end = "")
                    jn=input()
                    jn=controle_jn(jn)
                    if not jn :
                        continue
                    break
                
                if jn == "J":
                    print ("\n    WORDT TOEGEVOEGD!!   ")

                    dm.film_toevoegen(film)
                    sleep(1)
                    print ("BESCHRIJVING GENEREREN")
                    with open(f"DATA/discriptions/{str(movie_dict['id'])}.txt",'w') as bestand :
                        bestand.write(movie_dict["overview"])
                    sleep (1)
                    print ("POSTER GENEREREN")


                    # haal de poste op (JPG)
                    foto=requests.get("https://image.tmdb.org/t/p/w200"+movie_dict["poster_path"])
                    with open(f"DATA/posters/{str(movie_dict['id'])}.jpg",'wb') as bestand :
                        bestand.write(foto.content)
                    # Zet de opgeslagen poster.JPG om naar poster.png
                    im1=Image.open(f"DATA/posters/{str(movie_dict['id'])}.jpg")
                    im1.save(f"DATA//posters/{str(movie_dict['id'])}.png")
                    # Verwijder het JG bestand
                    if os.path.exists(f"DATA/posters/{str(movie_dict['id'])}.jpg") :
                        os.remove(f"DATA/posters/{str(movie_dict['id'])}.jpg")  

                    sleep (1.5)
                else :
                    print (f"\n {film} werd <b><red>NIET</red></b> toegevoegd\n \n ", end ="")
                    print_opdrachtregel("Druk op een toets")
                    input()

            else :
                print ("\n<red>    Film <b>NIET</b> gevonden bij TheMovieDB.org, \n\n    <b>CONTROLEER TMDB_ID !!!</b></red> ", end="")
                print_opdrachtregel("Druk op een toets")
                input()
    return

def ft_film_verwijderen_by_id():
    keuze = None
    dm=Datamanager()

    while True :
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
        print_titel("FILM VERWIJDEREN")
        print (x)

        #
        # GEEF DE ID VAN DE FILM DIE VERWIJDERD MOET WORDEN
        #
        print ("<red>Welke film moet worden verwijderd ")
        print_opdrachtregel ("Maak uw keuze (ID) (eindig met enter) ")
        keuze = input()
        if keuze == "":
            break

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
        film=dm.film_by_id(int(keuze))
        vertoning = dm.vertoning_by_film_id(int(keuze))
        
        if vertoning :
            print (f"\n Film kan <b><red>niet</red></b> worden verwijderd, {film.titel.upper()} is in een vertoning opgenomen")
            print()
            print_opdrachtregel ("Druk op een toets")
            input()
            continue
                
        # Enkel de film verwijderen als die in de DB zit!!!
        if int(keuze) in id_list :
            film=dm.film_by_id(int(keuze))

            while True :
        
                print (f"Wenst u {film} toe te VERWIJDEREN. druk j/n ", end = "")
                jn=input()
                jn=controle_jn(jn)
                if not jn :
                    continue
                break
    
            if jn == "J":
                print ("\n <red>WORDT VERWIJDERD!!</red>")
                if os.path.exists(f"DATA/posters/{film.MDB_id}.png") :
                    print ("Poster verwijderen!")
                    sleep(1)
                    os.remove(f"DATA/posters/{film.MDB_id}.png") 
                if os.path.exists(f"DATA/discriptions/{film.MDB_id}.txt") :
                    print("Discription verwijderen")
                    sleep(1)
                    os.remove(f"DATA/discriptions/{film.MDB_id}.txt")  
                print ("Film uit DB verwijderen")
                sleep(1)
                dm.film_verwijderen_by_id(int(keuze))
                sleep (1.5)
            else :
                print (f"\n {film} werd <b><red>NIET</red></b> VERWIJDERD", end ="")
                sleep (2)
            
            
        else :
            print ("<red> film niet in lijst !!! </red>")
            sleep (1.5)
    return

def ft_film_verwijderen_by_MDB_id():
    keuze = None
    dm=Datamanager()
    while True :
        x= PrettyTable()
        MDB_id_list=[]
        x.field_names=(["ID", "TITEL"])

        #Maak een tabel van alle films en toon die op het scherm
        films=dm.alle_films()
        for film in films :
            x.add_row([film.MDB_id, film.titel])
            # Maak thevens een lijst van alle MDB_id's die in de DB zitten 
            MDB_id_list.append(film.MDB_id)
        system("cls")
        print_titel("FILM VERWIJDERN MET TMDB ID")
        print (x)

        #print (id_list)
        #print (MDB_id_list)
        print ("<red>Welke film moet worden verwijderd ")
        print_opdrachtregel ("Maak uw keuze (TMDB id) (eindig met enter) ")
        keuze = input()
        if keuze == "":
            break
        
        if keuze in MDB_id_list :
            film=dm.film_by_MDB_id(keuze)

            vertoning = dm.vertoning_by_film_id(film.id)
        if vertoning :
            print (f"<red>film kan <b>NIET</b> worden verwijderd, {film.titel.upper()} is in een vertoning opgenomen</red>")
            input()
            continue

        if keuze in MDB_id_list : #kijk na of de film al in de db zit
            film=dm.film_by_MDB_id(keuze)
            while True :
        
                print (f"Wenst u {film} toe te VERWIJDEREN?\n")
                print_opdrachtregel ("druk j/n ")
                jn=input()
                jn=controle_jn(jn)
                if not jn :
                    continue
                else :
                    break
    
            if jn == "J":
                print ("\n <red>WORDT VERWIJDERD!!</red>")
                if os.path.exists(f"DATA/posters/{film.MDB_id}.png") :
                    print ("Poster verwijderen!")
                    sleep(1)
                    os.remove(f"DATA/posters/{film.MDB_id}.png") 
                if os.path.exists(f"DATA/discriptions/{film.MDB_id}.txt") :
                    print("Discription verwijderen")
                    sleep(1)
                    os.remove(f"DATA/discriptions/{film.MDB_id}.txt")  
                print ("Film uit DB verwijderen")
                sleep(1)
                dm.film_verwijderen_by_MDB_id(keuze)
                sleep (1.5)
            else :
                print (f"\n {film} werd <b><red>NIET</red></b> VERWIJDERD", end ="")
                sleep (2)
            
            
        else :
            print ("<red> film niet in lijst !!! </red>")
            sleep (1.5)

    return
    
def ft_film_KNT_KT_wisselen():
        #Color
    R = "\033[0;31;40m" #RED
    G = "\033[0;32;40m" # GREEN
    Y = "\033[0;33;40m" # Yellow
    B = "\033[0;34;40m" # Blue
    N = "\033[0m" # Reset
    while True :
        jn=""
        x = PrettyTable()
        x.field_names=(["ID",  "filmtitel", "KT/KNT"])
        
        dm = Datamanager()
        film_list=[]
        kt='   '+'<green>KT</green>'+'     '
        knt='KNT'
        system ("cls")
        print_titel ("FILM KT/KNT WISSELEN")
        print("<green>\n  Als een fim 'kinderen toegelaten' (KT) is kan je ze hier op 'Kinderen niet Toegelaten' (KNT) plaatsen\n\n  Geef de juiste waardes in!!! Let op hetgeen gevraagd wordt!! </green>")
        print(" <green>\n  door ENTER te drukken verlaat u het menu</green>") 
        films =dm.alle_films()
        for film in films :
            x.add_row([film.id, film.titel, G+"KIDS ALLOWED"+N if film.knt=='KT'else R+"NO KIDS ADMITTED"+N ])
            film_list.append(film.id)

        print (x)
        #print (film_list)
        print ("\n<blue>  Welke film (ID) moet KT/KNT wisselen ? </blue>  ", end="")
        print_opdrachtregel ("geef de ID aub?")
        film_ID = input()
        if not film_ID :
            break
        #if not vertoning_ID :
        #    break
        film_ID=controle_int(film_ID)
        while not film_ID :
            print_opdrachtregel ("geef de correcte ID aub?")
            film_ID = input()
            film_ID=controle_int(film_ID)
            if not film_ID :
                continue            
                
        
        if int(film_ID) in film_list :
            film=dm.film_by_id(int(film_ID))
            #print ("HOERA")
            #input()
            print (f"<blue>   {film} </blue><red>{'KT' if film.knt=='KT' else 'KNT'}</red><blue> Wisselen in</blue> <red>{'KNT' if film.knt=='KT' else 'KT'}</red> (j/n) ")
            
            jn=input ()
            #print (jn)
            #input()
            jn=controle_jn(jn)
            while not jn :
                print (f"<blue>   {film} </blue><red>{'KT' if film.knt=='KT' else 'KNT'}</red><blue> Wisselen in</blue> <red>{'KNT' if film.knt=='KT' else 'KT'}</red> ")
                print_opdrachtregel("geef j/n aub?")
                jn=input () 
                jn = controle_jn(jn)               
            if jn =="J":
                if film.knt == "KT":
                    print (" <red> WISSELEN </red>")
                    dm.set_film_KNT_by_id(int(film_ID))
                else :
                    print (" <red> WISSELEN </red>")
                    dm.set_film_KT_by_id(int(film_ID))

def ft_alle_films_tonen():
            #Color
    R = "\033[0;31;40m" #RED
    G = "\033[0;32;40m" # GREEN
    Y = "\033[0;33;40m" # Yellow
    B = "\033[0;34;40m" # Blue
    N = "\033[0m" # Reset
    dm=Datamanager()

    
    x= PrettyTable()
   
    x.field_names=(["ID", "TITEL", "KT/KNT",  "duur"])
    #
    #  TOON ALLE films
    #
    films=dm.alle_films()
    for film in films :
        x.add_row([film.id, film.titel, G+"KIDS ALLOWED"+N if film.knt=='KT'else R+"NO KIDS ADMITTED"+N, film.duurtijd])
        
    system("cls")
    print_titel("FILMS TONEN")
    x.sortby="TITEL"
    print (x)
    print_opdrachtregel ("druk enter")
    input()
    return

def ft_film_zoeken_met_zoekterm():
            #Color
    R = "\033[0;31;40m" #RED
    G = "\033[0;32;40m" # GREEN
    Y = "\033[0;33;40m" # Yellow
    B = "\033[0;34;40m" # Blue
    N = "\033[0m" # Reset
    keuze = None
    dm=Datamanager()
    
    system('cls')    
    print_titel("FILM ZOEKEN MET ZOEKTERM")
    
    print_opdrachtregel ("Geef een zoekterm (eindig met enter) ")
    keuze = input()
    print (keuze)
    if keuze == "":
        return
   
    x= PrettyTable()

    x.field_names=(["ID", "TITEL", "KT/KNT",  "duur"])
    films=dm.film_by_zoekterm(keuze)
    for film in films :
        x.add_row([film.id, film.titel, G+"KIDS ALLOWED"+N if film.knt=='KT'else R+"NO KIDS ADMITTED"+N, film.duurtijd])
    x.sortby="TITEL"
    print (x)
    print_opdrachtregel ("druk enter")

    input()
    return            


def ft_film_bewerken():
    while True:

        TO_DO_list= ["Film toevoegen",  "film verwijderen by id", "film verwijderen by TMDB id", "film KT/KNT wisselen", "Alle films tonen", "Film zoeken met zoekterm"]
        TO_DO_list_header = ["keuze", "WAT WIL JE DOEN"]
        afsluiten ="TERUG NAAR HOOFDMENU"
        system ('cls')
        print_titel ("FILMS BEWERKEN")
        x, rijteller = menu_opbouw (TO_DO_list_header, TO_DO_list,afsluiten)
        print (x)
        print_opdrachtregel (f"MAAK UW KEUZE AUB (tussen 0 en {rijteller} ) ")
        keuze = input()
        menu_keuze_controle(rijteller, keuze)
        if keuze == "0":
            break
        if keuze == "1":
            ft_film_toevoegen()
        if keuze == "2":
            ft_film_verwijderen_by_id()
        if keuze =="3":
            ft_film_verwijderen_by_MDB_id()
        if keuze =="4":
            ft_film_KNT_KT_wisselen()
        if keuze =="5":
            ft_alle_films_tonen()
        if keuze =="6":
            ft_film_zoeken_met_zoekterm()
