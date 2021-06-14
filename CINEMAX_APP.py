from os import system
from prettytable import PrettyTable
from ansimarkup import ansiprint as print
from utils.menu_en_contole import menu_keuze_controle, menu_opbouw, print_opdrachtregel, print_titel
from admin.filmthings import ft_film_bewerken
from admin.vertoningthings import ft_vertoning_bewerken
from admin.ticketthings import ft_ticket_bewerken

MDB_id = ""
#dm = Datamanager()


rijteller =0 

while True :
    

    TO_DO_list= ["Film bewerken",  "Vertoningen bewerken", "Tickets bewerken"]
    TO_DO_list_header = ["keuze", "WAT WIL JE DOEN"]
    afsluiten="AFSLUITEN"
    system ('cls') 
    print_titel("HOOFDMENU") 
    x, rijteller = menu_opbouw (TO_DO_list_header, TO_DO_list, afsluiten)
    print (x)
    print_opdrachtregel(f"MAAK UW KEUZE AUB (tussen 0 en {rijteller} ) ")
    keuze = input()
    menu_keuze_controle(rijteller, keuze)
    if keuze == "0":
        break
    if keuze == "1":
        ft_film_bewerken()
    if keuze == "2":
        ft_vertoning_bewerken()

    if keuze =="3":
        ft_ticket_bewerken()

    #3313033333131333330322236302333333333