from os import system
from menu import menu_keuze_controle, menu_opbouw
from prettytable import PrettyTable
from ansimarkup import ansiprint as print
import requests
from models.film import Film
from DATA.datamanager import Datamanager
from time import sleep
import json

MDB_id = ""
dm = Datamanager()

endpoint1 = "https://api.themoviedb.org/3/movie/"
endpoint2 ="?api_key=63ab94123b97a859ecdc1e3ebdd2af14&language=nl&region=BE"
rijteller =0 

while True :

    TO_DO_list= ["Film toevoegen", "Film Verwijderen", "Vertoning Toevoegen", "Vertoning Verwijderen"]
    system ('cls')    
    x, rijteller = menu_opbouw (TO_DO_list)
    print (x)
    print (f"<blue>MAAK UW KEUZE AUB (tussen 0 en {rijteller} ) </blue>", end = "")
    keuze = input()
    menu_keuze_controle(rijteller, keuze)
    if keuze == "0":
        break
    if keuze == "1":
        system ("cls")
        print()
        print()
        print()
        print ("<blue> Geef het Movie Data Base id aub ? </blue>", end ="")
        MDB_id=input ()
        response= requests.get(endpoint1+MDB_id+endpoint2)
        movie_dict=response.json()
        #print (json.dumps(movie_dict, indent=2))

        film = Film (movie_dict["title"], movie_dict["runtime"], "KNT" if movie_dict["adult"] == True else "KT", MDB_id) 
        print (film)
        print ("deze wordt toegevoegd. druk op een toets")
        input()
#        print (movie_dict["adult"])
#print (movie_dict["title"])
#print (movie_dict["overview"])
#print (movie_dict["id"])
#print (movie_dict["runtime"])
        dm.film_toevoegen(film)
        films=dm.alle_films()
        for film in films :
            print (film)





        


