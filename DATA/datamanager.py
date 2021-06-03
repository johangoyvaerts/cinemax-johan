from models.film import Film
from models.vertoning import Vertoning
from models.ticket import Ticket
from DATA.database import dbconn

class Datamanager :

    #
    # FILMS
    #


    # TONEN

    def alle_films(self):
        with dbconn() as cur :
            sql = "SELECT * FROM films"
            cur.execute (sql)
            rijen = cur.fetchall()
            films = [Film.from_dict(rij) for rij in rijen]
            return films

    def film_by_id(self, id):
        with dbconn() as cur :
            sql = "SELECT * FROM films WHERE id = ?"
            cur.execute (sql, [id])
            rij = cur.fetchone()
            if rij :
                film = Film.from_dict(rij)
                return film
            else :
                return None

    def film_by_zoekterm(self, zoekterm):
        with dbconn() as cur :
            zkterm =f"%{zoekterm}%"
            sql = "SELECT * FROM films WHERE titel LIKE ?"
            cur.execute (sql, [zkterm])
            rijen = cur.fetchall()
            if rijen :
                films = [Film.from_dict(rij) for rij in rijen]
                return films
            else :
                return None

    # toevoegen FILM

    def film_toevoegen (self, film):
        with dbconn() as cur :
            sql = "INSERT INTO films (titel, duur, knt, MDB_id) VALUES (?,?,?,?)"
            cur.execute(sql,[film.titel, film.duur, film.knt, film.MDB_id])

    # verwijderen FILM

    def film_verwijderen_by_id (self,id):
        with dbconn() as cur :
            if id :
                sql = "DELETE FROM films WHERE id = ?"
                cur.execute(sql,[id])
            else :
                raise ValueError


    #
    # VERTONINGEN
    #

    # TONEN

    def alle_vertoningen(self):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id"
            cur.execute (sql)
            rijen = cur.fetchall()
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen

    def alle_actieve_vertoningen(self):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id  WHERE vertoningen.vertoning_actief = 'AC'"
            cur.execute (sql)
            rijen = cur.fetchall()
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen

    def alle_niet_actieve_vertoningen(self):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id  WHERE vertoningen.vertoning_actief = 'NA'"
            cur.execute (sql)
            rijen = cur.fetchall()
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen


    def alle_2D_vertoningen(self):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id  WHERE vertoningen.drie_d = '2D'"
            cur.execute (sql)
            rijen = cur.fetchall()
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen


    def alle_3D_vertoningen(self):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id  WHERE vertoningen.drie_d = '3D'"
            cur.execute (sql)
            rijen = cur.fetchall()
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen

    
    def alle_vertoningen_by_zaal(self,zaal):
        with dbconn() as cur :
            sql = "SELECT vertoningen.*, films.* FROM vertoningen INNER JOIN films ON vertoningen.films_id = films.id  WHERE vertoningen.zaal = ?"
            cur.execute (sql, [zaal])
            rijen = cur.fetchall()
            vertoningen = [Vertoning.from_dict(rij) for rij in rijen]
            return vertoningen


    #
    #  VERTONINGEN bewerken
    #

    def vertoning_actief_by_id(self,id):
        with dbconn() as cur :
            sql = "UPDATE vertoningen SET vertoning_actief = 'AC' WHERE id = ?"
            cur.execute (sql, [id])

    def vertoning_non_actief_by_id(self,id):
        with dbconn() as cur :
            sql = "UPDATE vertoningen SET vertoning_actief = 'NA' WHERE id = ?"
            cur.execute (sql, [id])



    def vertoning_verwijderen_by_id (self,id):
        with dbconn() as cur :
            if id :
                sql = "DELETE FROM vertoningen WHERE id = ?"
                cur.execute(sql,[id])
            else :
                raise ValueError


    def vertoning_toevoegen (self, vertoning):
        with dbconn() as cur :
            sql = "INSERT INTO vertoningen (zaal, uur, drie_d, vertoning_actief, films_id) VALUES (?,?,?,?,?)"
            cur.execute(sql,[vertoning.zaal, vertoning.uur, vertoning.drie_d, vertoning.vertoning_actief, vertoning.film.id])

            



    