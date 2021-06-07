from prettytable import PrettyTable
from ansimarkup import ansiprint as print
from os import system
from time import sleep




def menu_opbouw ( kolom_head ,lijst) :
    x=PrettyTable()
    x.field_names=(kolom_head)
    rijteller=0
    for rij in lijst :
        rijteller+=1
        x.add_row ([rijteller, rij])
        
    x.add_row([0, "   AFSLUITEN   "])
    
    return x, rijteller



def menu_keuze_controle (rijteller, keuze):

    try :
        get=int (keuze)
        if get < 0 or get >rijteller :
            print ("<RED>CORRECTE KEUZE AUB</RED>")
            sleep (0.5)  
    except ValueError :
        print ("<RED>CORRECTE KEUZE AUB</RED>")
        sleep (0.5) 
    return keuze


def controle_jn(jn):
    if jn.upper() == "J" or jn.upper() == "N" :
        return jn.upper()
    else :
        print ("<RED> CORRECTE KEUZE AUB j/n</RED>")
        sleep (1)
        return None

def controle_int(int_getal):
#    if int_getal == int :
#        return True
#    else :
#        print ("<RED>CORRECTE KEUZE AUB j/n</RED>")
#        sleep (1)
#        return 
    try :
        getal = int(int_getal)
        return int_getal
    except ValueError :
        print ("<RED> CORRECTE INTEGER AUB </RED>")
        sleep (1)
        return None


    