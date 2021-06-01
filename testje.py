from models.film import Film

nieuwe_film=Film("grease", 100, "F","tt4656546")


print (nieuwe_film.duur)
nieuwe_film.duur=100
nieuwe_film.duur=150
nieuwe_film.duur=98
print (nieuwe_film.duur)
nieuwe_film.knt="f"
print (nieuwe_film.knt)
print (nieuwe_film)
print (nieuwe_film.duurtijd())