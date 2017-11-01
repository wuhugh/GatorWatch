from bs4 import BeautifulSoup
import requests

class MovieListing:
    name = ""
    duration = ""
    times = []

    def __init__(self, name, duration, times):
        self.name = name
        self.duration = duration
        self.times = times

class Theater:
    name = ""
    address = ""
    movies = []

    def __init__(self, name, address, movies):
        self.name = name
        self.address = address
        self.movies = movies

# Find movies in the area - return an array of Theaters
def GetMovies():
    r = requests.get("https://www.moviefone.com/showtimes/gainesville-fl/32601/theaters/")
    soup = BeautifulSoup(r.text, "html.parser")

    results = soup.find("body", {"class": "showtimes-closest-page"})
    results = results.find("div", {"id": "mf-theater-showtimes-list"})

    results = results.findAll("div", {"class": "theater"})

    theaters = []

    for theater in results:
        theater_name = theater.find("a", {"class": "theater-name"}).text
        address = theater.find("p", {"class": "address"}).find("a").text

        movies = theater.findAll("div", {"class": "movie-data-wrap"})

        # print(theater_name)
        # print(address)

        movie_list = []

        for movie in movies:
            title = movie.find("div", {"class": "movietitle"}).text

            duration = movie.find("div", {"class": "movierating-runtime"}).text
            duration = duration.strip()
            duration = duration[:20]
            duration = duration.strip()

            showtimes = movie.find("div", {"class": "showtimes-list"}).findAll("span", {"class": "showtime-display"})

            MovieObj = MovieListing(title,duration,showtimes)
            movie_list.append(MovieObj)

            '''
            print(title)
            print(duration)
            for child in showtimes:
                print(child.text)
            print("---------")
            '''

        TheaterObj = Theater(theater_name, address, movie_list)
        theaters.append(TheaterObj)

    return theaters
    '''
    for theater in theaters:
        print(theater.name)
    '''