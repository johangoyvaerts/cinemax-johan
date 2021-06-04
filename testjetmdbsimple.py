#import tmdbsimple as tmdb,requests
import requests
import json

endpoint1 = "https://api.themoviedb.org/3/movie/"
endpoint2 ="?api_key=63ab94123b97a859ecdc1e3ebdd2af14&language=nl&region=BE"
#endpoint = "https://api.themoviedb.org/3/search/movie?api_key=63ab94123b97a859ecdc1e3ebdd2af14&query=seven"
#tmdb.API_KEY = '63ab94123b97a859ecdc1e3ebdd2af14'
#
#tmdb.REQUESTS_SESSION = requests.session()
#movie = tmdb.Movies(343611)
#response = movie.info()
#print (response)
#print (response["title"])
#
#print (response["adult"])
#print (response["imdb_id"])
#print (response["overview"])
MDB_id="399566"
response= requests.get(endpoint1+MDB_id+endpoint2)
movie_dict=response.json()

print (json.dumps(movie_dict, indent=2))
print (movie_dict["adult"])
print (movie_dict["title"])
print (movie_dict["overview"])
print (movie_dict["id"])
print (movie_dict["runtime"])

