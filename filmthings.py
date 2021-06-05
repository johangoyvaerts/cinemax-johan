#from NAVIGATIE import TO_DO_list
#from NAVIGATIE import MDB_id
from DATA.datamanager import Datamanager
from os import system
import requests
from models.film import Film
from ansimarkup import ansiprint as print
from time import sleep
from menu_en_controle import controle_jn, menu_opbouw, menu_keuze_controle
from prettytable import PrettyTable

# film toevoegen met de TMDB_id (te vinden op Themovierdb.org)

def ft_film_toevoegen():
    dm=Datamanager()
    jn=""
    endpoint1 = "https://api.themoviedb.org/3/movie/"
    endpoint2 ="?api_key=63ab94123b97a859ecdc1e3ebdd2af14&language=nl&region=BE"
    while True :
        system ("cls")
        print("       <b><GREEN>                               </GREEN></b>")
        print("       <b><GREEN>   FILM TOEGOEGEN MET TMDB ID  </GREEN></b>")
        print("       <b><GREEN>                               </GREEN></b>")
        print()
        print ("<blue> Geef het Movie Data Base id aub ? </blue> (eindig met ENTER) ", end ="")
        MDB_id=input ()
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
                
                print (f"Wenst u {film} toe te voegen. druk j/n ", end = "")
                jn=input()
                logic=controle_jn(jn)
                if logic :
                    break
                continue
            
            if jn.upper() == "J":
                print ("\n WORDT TOEGEVOEGD!!")
                dm.film_toevoegen(film)
                sleep (1.5)
            else :
                print (f"\n {film} werd <b><red>NIET</red></b> toegevoegd", end ="")
                sleep (2)
            
        else :
            print ("<red> film niet gevonden </red>")
            sleep (1.0)
    return



def ft_film_verwijderen():
    keuze = None
    dm=Datamanager()
    while True :
        List_header = ["keuze", "WAT WIL JE DOEN"]
        TO_DO_list = ["verwijder per id","Verwijder per TMDB_id"]
        system ('cls')    
        x, rijteller = menu_opbouw (List_header, TO_DO_list)
        print (x)
        print (f"<blue>MAAK UW KEUZE AUB (tussen 0 en {rijteller} ) </blue>", end = "")
        keuze = input()
        
        if keuze == "0" :
            break
        if keuze == "1" : #verwijderen by ID
            while True :
                x= PrettyTable()
                id_list=[]
                x.field_names=(["ID", "TITEL"])
                #print ("filmverwijder id")
                films=dm.alle_films()
                for film in films :
                    x.add_row([film.id, film.titel])
                    id_list.append(film.id)
                system("cls")
                print (x)
                #print (id_list)
                print ("<red>Welke film moet worden verwijderd ")
                print ("<red>Maak uw keuze (ID) </red> (endig met enter) ", end ="")
                keuze = input()
                if keuze == "":
                    break

                if int(keuze) in id_list :
                    film=dm.film_by_id(int(keuze))
                    while True :
                
                        print (f"Wenst u {film} toe te VERWIJDEREN. druk j/n ", end = "")
                        jn=input()
                        logic=controle_jn(jn)
                        if logic :
                            break
                        continue
            
                    if jn.upper() == "J":
                        print ("\n <red>WORDT VERWIJDERD!!</red>")
                        dm.film_verwijderen_by_id(int(keuze))
                        sleep (1.5)
                    else :
                        print (f"\n {film} werd <b><red>NIET</red></b> VERWIJDERD", end ="")
                        sleep (2)
                    
                    
                else :
                    print ("<red> film niet in lijst !!! </red>")
                    sleep (1.5)

                
        if keuze == "2" : #verwijderen by MDB_id
            while True :
                x= PrettyTable()
                MDB_id_list=[]
                x.field_names=(["ID", "TITEL"])
                #print ("filmverwijder TMDB id")
                films=dm.alle_films()
                for film in films :
                    x.add_row([film.MDB_id, film.titel])
                    MDB_id_list.append(film.MDB_id)
                system("cls")
                print (x)
                #print (id_list)
                print (MDB_id_list)
                print ("<red>Welke film moet worden verwijderd ")
                print ("<red>Maak uw keuze (TMDB id) </red> (endig met enter) ", end ="")

                keuze = input()
                if keuze == "":
                    break

                if keuze in MDB_id_list :
                    film=dm.film_by_MDB_id(keuze)
                    while True :
                
                        print (f"Wenst u {film} toe te VERWIJDEREN. druk j/n ", end = "")
                        jn=input()
                        logic=controle_jn(jn)
                        if logic :
                            break
                        continue
            
                    if jn.upper() == "J":
                        print ("\n <red>WORDT VERWIJDERD!!</red>")
                        dm.film_verwijderen_by_MDB_id(keuze)
                        sleep (1.5)
                    else :
                        print (f"\n {film} werd <b><red>NIET</red></b> VERWIJDERD", end ="")
                        sleep (2)
                    
                    
                else :
                    print ("<red> film niet in lijst !!! </red>")
                    sleep (1.5)

    return