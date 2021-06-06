from datetime import datetime
from models.vertoning import Vertoning
from models.film import Film

class Ticket :
    def __init__(self, datum, prijs_volw, prijs_kind, aant_volw, aant_kind, vertoning, id=None) :
        self._datum = datum
        self.prijs_volw = prijs_volw
        self.prijs_kind = prijs_kind
        self.aant_volw = aant_volw
        self.aant_kind = aant_kind
        self.vertoning = vertoning
        self.id=id

    @property
    def datum (self) :
        return self._datum

    # Nagaan of de string "YYYY-MM-DD" een datum is
    @datum.setter
    def datum(self, datum):
        dagformaat = "%Y-%m-%d"
        try :
            datetime.strptime(datum,dagformaat)
            self._datum=datum    
        except ValueError :
           print ("geen correcte datum") 
           return
            
    @property
    def aant_volw (self):
        return self._aant_volw
        
    @aant_volw.setter
    def aant_volw(self,aant_volw):
        if type(aant_volw)==int :
            self._aant_volw=aant_volw
        else :
            raise ValueError    

    @property
    def aant_kind (self):
        return self._aant_kind
        
    @aant_kind.setter
    def aant_kind(self,aant_kind):
        if type(aant_kind)==int :
            self._aant_kind=aant_kind
        else :
            raise ValueError
            
            
    @property
    def vertoning (self) :
        return self._vertoning

    #bij een ticket hoort een vertoning van de klasse vertoning
    @vertoning.setter
    def vertoning(self, vertoning):
        if isinstance(vertoning, Vertoning) :
            self._vertoning = vertoning
        else :
            raise ValueError


    #prijs per ticket
    @property
    def prijs_ticket (self):
        return self.prijs_volw*self.aant_volw+self.prijs_kind*self._aant_kind


    def __str__(self):
        return f" ticket gekocht op {self.datum} \n VOLWASENEN {self.aant_volw:>3d} à {self.prijs_volw:>5.2f}€ = {self.prijs_volw*self.aant_volw:>5.2f}€ \n KINDEREN   {self.aant_kind:>3d} à {self.prijs_kind:>5.2f}€ = {self.prijs_kind*self.aant_kind:>5.2f}€\n TOTAAL                    {self.prijs_ticket:>5.2f}€\n {self.vertoning.film}\n zaal {self.vertoning.zaal} om {self.vertoning.uur}h"



    @classmethod
    def from_dict(cls, dict):
        datum = dict["datum"]
        prijs_volw = dict["prijs_volw"]
        prijs_kind = dict["prijs_kind"]
        aant_volw = dict["aant_volw"]
        aant_kind = dict["aant_kind"]
        vertoning = Vertoning(dict["zaal"], dict["uur"], dict["drie_d"], dict["vertoning_actief"], Film(dict["titel"], dict["duur"], dict["knt"], dict["MDB_id"] ))
        id=dict["id"]
        return cls(datum, prijs_volw, prijs_kind, aant_volw, aant_kind, vertoning, id)


