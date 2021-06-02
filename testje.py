from models.vertoningen import Vertoningen
from models.film import Film

nieuwe_film=Film("grease", 100, "F","tt4656546")


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

nieuwe_vertoning = Vertoningen(2,1300,"2D","AC",3)

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