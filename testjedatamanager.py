from models.film import Film
from models.vertoning import Vertoning
from models.ticket import Ticket
from DATA.datamanager import Datamanager

dm = Datamanager()
#film1=Film("In the Heights", 143, "KT", "tt1321510")
#film2=Film("Peter Rabbit 2: The Runaway", 99, "KT", "tt8376234")
#film3=Film("Censor", 84, "KNT", "tt10329614")
filmzoek1 = dm.film_by_id(5)
filmzoek2 = dm.film_by_id(9)
filmzoek3 = dm.film_by_id(3)
vertoning1 = Vertoning(2,1500,"3D","AC",filmzoek1)
vertoning2 = Vertoning(3,1500,"2D","AC",filmzoek2)
vertoning3 = Vertoning(1,2000,"3D","NC",filmzoek3)


teller=0
##
## tonen van FILM(S)
##
#
#films = dm.alle_films()
#for film in films :
#    print (f"{film.id} {film.titel} en duurt {film.duurtijd} en is {'kinderen toegelaten' if film.knt == 'KT' else 'kinderen niet toegelaten.' }")
#print ()
#print (30*"id ")
#
#film = dm.film_by_id(2)
#if film :
#    print (f"de film met ID {film.id} is {film.titel}")
#
#print()
#print (10*"zkterm ")
#
#films = dm.film_by_zoekterm("sev")
#if films :
#    for film in films :
#        print (f"{film.id} {film.titel} en duurt {film.duurtijd} en is {'kinderen toegelaten' if film.knt == 'KT' else 'kinderen niet toegelaten.' }")
#
#else :
#    print ("geen films")
#
#print()
#print (10*"voegtoe ")
#
#dm.film_toevoegen(film1)
#dm.film_toevoegen(film2)
#dm.film_toevoegen(film3)
##films = dm.alle_films()
##for film in films :
##    print (f"{film.id} {film.titel} en duurt {film.duurtijd} en is {'kinderen toegelaten' if film.knt == 'KT' else 'kinderen niet toegelaten.' }")
##print()
##print (10*"verwijder ")
##
##dm.film_verwijderen_by_id(2)
##films = dm.alle_films()
##for film in films :
##    print (f"{film.id} {film.titel} en duurt {film.duurtijd} en is {'kinderen toegelaten' if film.knt == 'KT' else 'kinderen niet toegelaten.' }")
#print ()
#print ("alle vertoningen"*10)
#print ()
#vertoningen = dm.alle_vertoningen()
#for vertoning in vertoningen :
#    print (f"de vertoning van '{vertoning.film.titel.upper()}' is in zaal {vertoning.zaal} in {vertoning.drie_d} en duurt {vertoning.film.duurtijd}")
#
##vertoningen =[]
#print ()
#print ("AC vertoningen"*10)
#print ()
#
#vertoningen = dm.alle_actieve_vertoningen()
#for vertoning in vertoningen :
#    print (f"ACTIEF '{vertoning.film.titel.upper()}' is in zaal {vertoning.zaal} in {vertoning.drie_d} en duurt {vertoning.film.duurtijd} {vertoning.vertoning_actief}")
#
#
#print ()
#print ("NA vertoningen"*10)
#print ()
#
#vertoningen = dm.alle_niet_actieve_vertoningen()
#for vertoning in vertoningen :
#    print (f"NIET ACTIEF '{vertoning.film.titel.upper()}' is in zaal {vertoning.zaal} in {vertoning.drie_d} en duurt {vertoning.film.duurtijd} {vertoning.vertoning_actief}")
#
#print ()
#print (" 2d vertoningen"*10)
#print ()
#
#vertoningen = dm.alle_2D_vertoningen()
#for vertoning in vertoningen :
#    print (f"2D '{vertoning.film.titel.upper()}' is in zaal {vertoning.zaal} in {vertoning.drie_d} en duurt {vertoning.film.duurtijd} {vertoning.vertoning_actief}")
#
#print ()
#print (" 3d vertoningen"*10)
#print ()
#
#vertoningen = dm.alle_3D_vertoningen()
#for vertoning in vertoningen :
#    print (f"3D '{vertoning.film.titel.upper()}' is in zaal {vertoning.zaal} in {vertoning.drie_d} en duurt {vertoning.film.duurtijd} {vertoning.vertoning_actief}")
#
#print ()
#print (" vertoningen per zaal"*10)
#print ()
#
#vertoningen = dm.alle_vertoningen_by_zaal(2)
#for vertoning in vertoningen :
#    print (f"3D '{vertoning.film.titel.upper()}' is in zaal {vertoning.zaal} in {vertoning.drie_d} en duurt {vertoning.film.duurtijd} {vertoning.vertoning_actief}")
#
#print ()
#print (" zet AC"*10)
#print ()
#
#dm.set_vertoning_actief_by_id(2)

#dm.film_toevoegen(film1)
#dm.film_toevoegen(film2)
#dm.film_toevoegen(film3)


#dm.set_vertoning_non_actief_by_id(7)

#dm.vertoning_verwijderen_by_id(8)

#dm.vertoning_toevoegen(vertoning3)

#dm.vertoning_verwijderen_by_id(2)

#tickets= dm.alle_tickets()
#for ticket in tickets :
##    print (f"{ticket.datum}, {ticket.vertoning.film.titel}, {ticket.vertoning.zaal}")
#    print (ticket)

#tickets = dm.tickets_tss_data("2021-05-01", "2021-05-31")
#for ticket in tickets :
#    print (f"{ticket.datum}, {ticket.vertoning.film.titel}, {ticket.vertoning.zaal}")
##    print (ticket)

#tickets = dm.tickets_by_film_id(5)
#for ticket in tickets :
#    print (f"{ticket.datum}, {ticket.vertoning.film.titel}, {ticket.vertoning.zaal}")
##    print (ticket)
