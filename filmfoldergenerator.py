#slechts 1 maal uit te voeren om de posters aan te maken in png


from models.film import Film
from PIL import Image
import requests
from utils.menu_en_contole import get_api_key
from DATA.datamanager import Datamanager
import os

api_key = get_api_key()


dm = Datamanager()

endpoint1 = "https://api.themoviedb.org/3/movie/"
endpoint2 ="?api_key="+api_key

films= dm.alle_films()
for film in films :
    # vraag de film op
    response= requests.get(endpoint1+film.MDB_id+endpoint2)
    movie_dict=response.json()
    #vraag de poster op : JPG!!!
    foto=requests.get("https://image.tmdb.org/t/p/w200"+movie_dict["poster_path"])
    #schrijf het JPG bestand weg 
    with open(f"DATA/posters/{str(movie_dict['id'])}.jpg",'wb') as bestand :
        bestand.write(foto.content)
    # zet het JPG bestand om in een PNG bestand
    im1=Image.open(f"DATA/posters/{str(movie_dict['id'])}.jpg")
    im1.save(f"DATA//posters/{str(movie_dict['id'])}.png") 
    #verwijder JPG bestanden
    if os.path.exists(f"DATA/posters/{str(movie_dict['id'])}.jpg") :
        os.remove(f"DATA/posters/{str(movie_dict['id'])}.jpg")  
