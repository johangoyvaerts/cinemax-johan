from models.film import Film

#CINEMAX heeft 6 zalen
ZALEN = [1, 2, 3, 4, 5, 6]
SETTING = ["2D","3D"]
VERT_ACT = ["AC", "NA"]


class Vertoningen:
    def __init__(self, zaal, uur, drie_d, vertoning_actief, film_id) :
        self._zaal = zaal
        self._uur = uur 
        self._drie_d= drie_d
        self._vertoning_actief= vertoning_actief
        self.film_id=film_id
    
    @property
    def zaal (self) :
        return self._zaal

    #zaal moet in de CINEMAX zijn!!
    @zaal.setter
    def zaal(self, zaal):
        if zaal in ZALEN :
            self._zaal = zaal
        else :
            raise ValueError

    @property
    def uur (self) :
        return self._uur

    #uur moet tussen 0.00h en 24.00h liggen en 
    # uur moet op vol of 30min zijn!!
    @uur.setter
    def uur(self, uur):
        minuten = uur%100
        if (uur < 2400 or uur>0) and (minuten==30 or minuten==0):
            self._uur = uur
        else :
            raise ValueError

    @property
    def drie_d (self) :
        return self._drie_d

    #drie_d moet 3D of 2D zijn
    @drie_d.setter
    def drie_d(self, drie_d):
        if drie_d.upper() in SETTING :
            self._drie_d = drie_d.upper()
        else :
            raise ValueError




    @property
    def vertoning_actief (self) :
        return self._vertoning_actief

    # vertoning moet actief "AC" of niet-actief "NC" zijn
    # zo kan men zien of de vertoning gepland is of niet.
    # Een vertoning verwijderen zou ook de linnk met de film doen verdwijnen
    #   
    @vertoning_actief.setter
    def vertoning_actief(self, vertoning_actief):
        if vertoning_actief.upper() in VERT_ACT :
            self._vertoning_actief = vertoning_actief.upper()
        else :
            raise ValueError
"""   
    @property
    def uur (self):
        return self._uur

    @uur.setter
    pass
"""


