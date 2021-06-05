from DATA.datamanager import Datamanager
from os import system
import requests
from models.film import Film
from ansimarkup import ansiprint as print
from time import sleep




def ft_film_toevoegen():
    dm=Datamanager()
    endpoint1 = "https://api.themoviedb.org/3/movie/"
    endpoint2 ="?api_key=63ab94123b97a859ecdc1e3ebdd2af14&language=nl&region=BE"
    while True :
        system ("cls")
        print()
        print(" <b><GREEN>   FILM TOEGOEGEN MET TMDB ID  </GREEN></b>")
        print()
        print ("<blue> Geef het Movie Data Base id aub ? </blue> (eindig met ENTER) ", end ="")
        MDB_id=input ()
        if MDB_id == "":
            return
        response= requests.get(endpoint1+MDB_id+endpoint2)
        
        movie_dict=response.json()
        #print (json.dumps(movie_dict, indent=2))

        film = Film.from_movie_dict(movie_dict) 
        print (f"Wenst u {film} toe te voegen. druk j/n ", end = "")
        jn=input()
        if jn.upper() == "J":
            dm.film_toevoegen(film)
            print ("\n WORDT TOEGEVOEGD!!")
            sleep (1.5)
        else :
            print (f"\n {film} werd <b><red>NIET</red></b> toegevoegd", end ="")
            sleep (2)
        #films=dm.alle_films()
        #for film in films :
        #    print (film)
        #input()
    return



def ft_film_verwijderen():
    pass