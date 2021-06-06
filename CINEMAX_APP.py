from os import system
from ticketthings import ft_tickets_bewerken
from vertoningthings import ft_vertoning_bewerken
from menu_en_controle import menu_keuze_controle, menu_opbouw
from prettytable import PrettyTable
from ansimarkup import ansiprint as print
#import requests
from models.film import Film
from DATA.datamanager import Datamanager
from time import sleep
import json
from filmthings import ft_film_bewerken

MDB_id = ""
dm = Datamanager()

#endpoint1 = "https://api.themoviedb.org/3/movie/"
#endpoint2 ="?api_key=63ab94123b97a859ecdc1e3ebdd2af14&language=nl&region=BE"
rijteller =0 

while True :
    

    TO_DO_list= ["Film bewerken",  "Vertoningen bewerken", "Tickets bewerken"]
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
        ft_film_bewerken()
    if keuze == "2":
        ft_vertoning_bewerken()

    if keuze =="3":
        ft_tickets_bewerken()

    