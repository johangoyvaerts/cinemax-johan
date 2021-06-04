from prettytable import PrettyTable
from ansimarkup import ansiprint as print
from os import system
from time import sleep




def menu_opbouw (lijst) :
    x=PrettyTable()
    x.field_names=(["keuze","Wat wil je doen"])
    rijteller=1
    for rij in lijst :
        x.add_row ([rijteller, rij])
        rijteller+=1
    x.add_row([0, "   AFSLUITEN   "])
    
    return x, rijteller-1



def menu_keuze_controle (rijteller, keuze):
#    if keuze<"0" or keuze > str(rijteller-1) :
#        print ("<RED>CORRECTE KEUZE AUB</RED>")
#        sleep (0.5)
#    else :
#        return keuze
    try :
        get=int (keuze)
        if get < 0 or get >rijteller :
            print ("<RED>CORRECTE KEUZE AUB</RED>")
            sleep (0.5)  
    except ValueError :
        print ("<RED>CORRECTE KEUZE AUB</RED>")
        sleep (0.5)
    #if get < 0 or get >rijteller :
    #    print ("<RED>CORRECTE KEUZE AUB</RED>")
    #    sleep (0.5)  
    return keuze