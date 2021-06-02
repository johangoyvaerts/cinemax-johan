from models.tickets import Tickets
from models.vertoningen import Vertoningen
from models.film import Film
from datetime import datetime, date

nieuwe_film=Film("grease", 100, "KT","tt4656546")
film2=Film("grease 2", 135,"KT","tt654678")
film3=Film ("Seven", 127,"KNT","tt544587897")


print (nieuwe_film.duur)
nieuwe_film.duur=100
nieuwe_film.duur=150
nieuwe_film.duur=98
print (nieuwe_film.duur)
nieuwe_film.knt="kNt"
print (nieuwe_film.knt)
print (nieuwe_film)
print (nieuwe_film.duurtijd)

print (30*"-")

nieuwe_vertoning = Vertoningen(2,1300,"2D","AC",nieuwe_film)
vertoning2= Vertoningen(5,2000,"3d","AC",film2)
vertoning3= Vertoningen(2 ,2000,"2d","AC",film3)

ticket1 = Tickets("2021-04-20",10.5,8.5,1,2, vertoning3)
ticket2 = Tickets("2021-04-20",10.5,8.5,2,0,vertoning2)
ticket3 = Tickets("2021-04-20",10.5,8.5,2,0,vertoning2)
ticket4 = Tickets("2021-04-20",8,0,1,0, nieuwe_vertoning)
ticket5 = Tickets("2021-04-21",10.5,8.5,2,0,vertoning2)
ticket6 = Tickets("2021-04-22",10.5,8.5,2,0,vertoning3)
ticket7 = Tickets("2021-04-22",9.5,8.5,1,2, nieuwe_vertoning)
ticket8 = Tickets("2021-04-20",10.5,8.5,2,0,vertoning2)
ticket9 = Tickets("2021-04-20",10.5,8.5,2,0,vertoning2)

dagformaat = "%Y-%m-%d"

print (nieuwe_vertoning.zaal)
nieuwe_vertoning.zaal = 5
print (nieuwe_vertoning.zaal)
print (nieuwe_vertoning.uur)
nieuwe_vertoning.uur = 1400
print (nieuwe_vertoning.uur)
print (nieuwe_vertoning.drie_d)
nieuwe_vertoning.drie_d = "3D"
print (nieuwe_vertoning.drie_d)
print (nieuwe_vertoning.drie_d)
nieuwe_vertoning.drie_d = "2d"
print (nieuwe_vertoning.drie_d)
print (30*"-")
print (nieuwe_vertoning.vertoning_actief)
nieuwe_vertoning.vertoning_actief = "NA"
print (nieuwe_vertoning.vertoning_actief)
nieuwe_vertoning.vertoning_actief = "ac"
print (nieuwe_vertoning.vertoning_actief)
nieuwe_vertoning.vertoning_actief = "NA"
print (nieuwe_vertoning.vertoning_actief)
print (nieuwe_vertoning)
nieuwe_vertoning.film = film2
print (nieuwe_vertoning)
nieuwe_vertoning.vertoning_actief="ac"
print (nieuwe_vertoning)
print (vertoning2)
print (vertoning3)
print (30*"-", "TIKKETTEKES")
print (ticket2.datum)
ticket2.datum = "2021-08-30"
date1= ticket2.datum


print (ticket2.datum)

print (ticket1._aant_volw)

print (ticket5.prijs_ticket)

print (ticket1)

print ("**********************************************")
print (ticket2)


print ("**********************************************")
print (ticket4)
