from models.film import Film
from models.vertoning import Vertoning
from models.ticket import Ticket
from DATA.datamanager import Datamanager

dm = Datamanager()
film1=Film("In the Heights", 143, "KT", "tt1321510")
film2=Film("Peter Rabbit 2: The Runaway", 99, "KT", "tt8376234")
film3=Film("Censor", 84, "KNT", "tt10329614")
#
# tonen van FILM(S)
#

films = dm.alle_films()
for film in films :
    print (f"{film.id} {film.titel} en duurt {film.duurtijd} en is {'kinderen toegelaten' if film.knt == 'KT' else 'kinderen niet toegelaten.' }")
print ()
print (30*"id ")

film = dm.film_by_id(2)
if film :
    print (f"de film met ID {film.id} is {film.titel}")

print()
print (10*"zkterm ")

films = dm.film_by_zoekterm("sev")
if films :
    for film in films :
        print (f"{film.id} {film.titel} en duurt {film.duurtijd} en is {'kinderen toegelaten' if film.knt == 'KT' else 'kinderen niet toegelaten.' }")

else :
    print ("geen films")

print()
print (10*"voegtoe ")

#dm.film_toevoegen(film1)
#dm.film_toevoegen(film2)
#films = dm.alle_films()
#for film in films :
#    print (f"{film.id} {film.titel} en duurt {film.duurtijd} en is {'kinderen toegelaten' if film.knt == 'KT' else 'kinderen niet toegelaten.' }")
#print()
#print (10*"verwijder ")
#
#dm.film_verwijderen_by_id(2)
#films = dm.alle_films()
#for film in films :
#    print (f"{film.id} {film.titel} en duurt {film.duurtijd} en is {'kinderen toegelaten' if film.knt == 'KT' else 'kinderen niet toegelaten.' }")

vertoningen = dm.alle_vertoningen()
for vertoning in vertoningen :
    print (f"de vertoning van '{vertoning.film.titel.upper()}' is in zaal {vertoning.zaal} in {vertoning.drie_d} en duurt {vertoning.film.duurtijd}")

#vertoningen = dm.()
for vertoning in vertoningen :
    print (f"de vertoning van '{vertoning.film.titel.upper()}' is in zaal {vertoning.zaal} in {vertoning.drie_d} en duurt {vertoning.film.duurtijd}")