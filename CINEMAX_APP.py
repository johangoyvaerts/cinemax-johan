from os import system
from prettytable import PrettyTable
from ansimarkup import ansiprint as print
from utils.menu_en_contole import menu_keuze_controle, menu_opbouw
from admin.filmthings import ft_film_bewerken
from admin.vertoningthings import ft_vertoning_bewerken
from admin.ticketthings import ft_tickets_bewerken

MDB_id = ""
#dm = Datamanager()


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

    