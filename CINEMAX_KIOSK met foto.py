#from tkinter.constants import DISABLED
import PySimpleGUI as gui
from PySimpleGUI.PySimpleGUI import Column
#from PySimpleGUI.PySimpleGUI import THEME_XPNATIVE, Text
import requests
from os import system
from prettytable import PrettyTable
from ansimarkup import ansiprint as print
from utils.menu_en_contole import bepaal_prijs

from models.ticket import Ticket
from DATA.datamanager import Datamanager
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")


# venster ressetten indien men een andere film of zaal kiest!!
def andere_vertoning():
    window["-PRIJS_VOLW-"].update(value="0€")
    window["-PRIJS_KIND-"].update(value="0€")
    window["-AANT_VOLW-"].update(value=0,disabled=True)
    window["-AANT_KIND-"].update(value=0,disabled=True)
    window["-TOT_PRIJS_VOLW-"].update(value="0€")
    window["-TOT_PRIJS_KIND-"].update(value="0€")
    window["-TOTAAL-"].update(value="0€")
    window["-KOPEN-"].update(disabled=True)
    return
    
def andere_zaal():
    pass

vandaag = datetime.now()
datum = vandaag.strftime("%Y-%m-%d")

prijs_volw = 0
prijs_kind = 0
tot_prijs_volw =0
tot_prijs_kind = 0
buttontext="KOPEN"


dm = Datamanager()
film_knt=""
film_id_list = []
vertoningen_list=[]
#maak een lijst van filmtitels om te tonen in de listbox
# alle actieve vertoningen!!
vertoningen = dm.alle_actieve_vertoningen()
for vertoning in vertoningen:
    if vertoning.film.id not in film_id_list :
        vertoningen_list.append(vertoning.film.titel) 
       
        film_id_list.append(vertoning.film.id)
vertoningen_list.sort()

# Documentatie: https://pysimplegui.readthedocs.io/en/latest/call%20reference/

# gui.theme_previewer()
gui.theme("LightBlue1")



layout_titel = [gui.Text("CINEMAX", font="Helvetica 32")]

layout_listbox = [
    gui.Column([
        [gui.Image(filename="DATA/posters/cinemax.png", key="-FOTO-" , size= (200,300), pad=(50,0))]
    ]),
    gui.Column([
        [gui.Text("Kies een film")],
        [gui.Listbox(values=vertoningen_list, size=(25, 15), key="-VERTONINGEN-", enable_events=True)]
    ]),
    gui.Column([
        [gui.Text("uren en zalen")],
        [gui.Listbox(values=[], size=(20, 5), key="-ZALEN-", enable_events=True)],
        [   
            gui.Text ("VOLW", size=(5,1)), 
            gui.Text (text="0€",size=(5,1),key="-PRIJS_VOLW-", enable_events=True),
            gui.Spin ([i for i in range(0,100)], initial_value=0, key="-AANT_VOLW-",size=(3,1), enable_events=True, disabled=True),
            gui.Text(text="0€", key="-TOT_PRIJS_VOLW-", size=(8,1), enable_events=True, justification="r")
            ],
        [   
            gui.Text ("Kind", size=(5,1)),
            gui.Text (text="0€",key="-PRIJS_KIND-",size=(5,1), enable_events=True),
            gui.Spin ([i for i in range(0,100)], initial_value=0, key="-AANT_KIND-", size=(3,1),enable_events=True, disabled=True),
            gui.Text (text="0€", key="-TOT_PRIJS_KIND-", size =(8,1), enable_events=True , justification="r")
            ],
        [   
            gui.Text ("TOTAAL", size=(15,1)),
            gui.Text (text="0€", key="-TOTAAL-", enable_events=True, size= (10,1), justification="r")

        ],
        [
            gui.Button (button_text=buttontext, enable_events=True,size=(25,3), key="-KOPEN-", disabled=True)
        ]
    ])
]

layout = [

    layout_titel,
    layout_listbox
]

window = gui.Window("Bibliotheek", layout, size=(1080, 480), font="Helvetica 16", element_justification="center")

while True:
    zaal_list=[]
    event, values = window.read()
    if event == gui.WIN_CLOSED:
        break
    if event == "-VERTONINGEN-": 
        andere_vertoning()
        totaal=0

        geselecteerde_film = values["-VERTONINGEN-"][0]


        # haal de geselecteerde film op en neem hiervan de id en de knt ...
        films = dm.film_by_zoekterm (geselecteerde_film)
        for film in films :
            film_id=film.id
            film_knt=film.knt

            #print (film.knt,type(film.knt))

        # haal van de geselecteerde film de actieve zaal en uur op
        zalen = dm.vertoning_actief_by_film_id(film_id)

        for zaal in zalen :
            zaal_list.append(f"zaal : {zaal.zaal}, uur : {zaal.uur} {'3D' if zaal.drie_d == '3D' else ''}")
        window["-ZALEN-"].update(values=zaal_list)
        window["-FOTO-"].update(filename= f"DATA/posters/{film.MDB_id}.png")
    if event=="-ZALEN-":
        andere_vertoning()
        totaal=0
        
        geselecteerde_vertoning=values["-ZALEN-"][0]
        geselecteerde_zaal=geselecteerde_vertoning[7:8]
        geselecteerd_uur=geselecteerde_vertoning[16:20]


        # haal de vertoning op de geselecteerd werd
        vertoning = dm.vertoning_by_film_id_zaal_uur(film_id,geselecteerde_zaal,geselecteerd_uur)

        prijs_volw, prijs_kind = bepaal_prijs(vertoning)

        window["-PRIJS_VOLW-"].update(value=str (prijs_volw)+"€")
        window["-AANT_VOLW-"].update(disabled=False)
        if film_knt == "KT":
            window["-PRIJS_KIND-"].update(visible=True, value=str (prijs_kind)+"€")
            window["-AANT_KIND-"].update(disabled=False)

    if event == "-AANT_KIND-":
        window["-KOPEN-"].update(disabled=False)
        if values["-AANT_KIND-"]==0 and values["-AANT_VOLW-"]==0 :
            window["-KOPEN-"].update(disabled=True)

        tot_prijs_kind = values["-AANT_KIND-"]*prijs_kind

        window["-TOT_PRIJS_KIND-"].update(value=str(tot_prijs_kind)+"€")
        totaal= tot_prijs_volw+tot_prijs_kind
        window["-TOTAAL-"].update(value=str(totaal)+"€")
       
    
    if event == "-AANT_VOLW-":
        window["-KOPEN-"].update(disabled=False)
        if values["-AANT_KIND-"]==0 and values["-AANT_VOLW-"]==0 :
            window["-KOPEN-"].update(disabled=True)

        tot_prijs_volw = values["-AANT_VOLW-"]*prijs_volw
        
        window["-TOT_PRIJS_VOLW-"].update(value=str(tot_prijs_volw)+"€")
        
        totaal= tot_prijs_volw+tot_prijs_kind
        window["-TOTAAL-"].update(value=str(totaal)+"€")
        

    if event == "-KOPEN-":
        aant_volw=values["-AANT_VOLW-"]
        aant_kind=values["-AANT_KIND-"]
        ticket=Ticket(datum,prijs_volw,prijs_kind,str(aant_volw),str(aant_kind),vertoning)

        verkoop=gui.popup_ok_cancel(ticket, title = 'KOPEN ?')
        
        if verkoop == "OK":
            gui.popup_auto_close(ticket, title = "BEDANKT", auto_close_duration=3, button_type=None)
            # ticket toevoegen aan database
            dm.ticket_toevoegen(ticket)
        else : 
            gui.popup_auto_close (ticket,title="NIET VERKOCHT", auto_close_duration=3, text_color="red")
        andere_vertoning()
        # maak de listbox zalen leeg!!
        window["-ZALEN-"].update(values=[])


window.close()

