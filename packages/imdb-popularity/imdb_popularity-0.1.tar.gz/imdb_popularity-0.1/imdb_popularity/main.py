import os
import csv
import sys
import subprocess
#####
#

def install(package):
    '''
    Installs a given Python Package
    '''
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def find(m_id):
    '''
    Finds rating, region and genre of an id
    '''
    # we get a list of parameters from imdb database
    dp = ia.get_movie(m_id)
    # we get rating, region and genre from this list
    rating = dp.get('rating')
    region = dp.get('country')
    genre = dp.get('genres')

    output = (region, rating, genre)
    return output


def main(num):
    '''
    All magic happens here
    '''
    # Getting data and creating dictionaries
    sorter(num)
    # Finding information
    d_sum = best_sum(country_dict)
    d_pop = popularity(country_count)
    d_middle = best_genre_middle(country_dict, country_count)
    # Finalizing information
    saving(d_sum, d_pop, d_middle)


def sorter(n):
    '''
    '''
    # We disable certain genres:
    # Short, Family, Game-show, Music, News, Reality TV, Sport, Talk-Show
    forbiden = ("Short", "Family", "Game-Show", "Music", "News",
                "Reality-TV", "Sport", "Talk-Show")

    print("This process needs internet connection")
    for num in range(1, n+1):
        length = len(str(num))
        # Create a proper id
        m_id = '0'*(7-length) + str(num)
        length = len(str(num))
        # Get film info
        film_info = find(m_id)
        # Get genres
        genres = film_info[2]
        # Get rating
        rating = film_info[1]
        # Get country
        try:
            country = ''.join(film_info[0])
        except:
            country = film_info[0]
        if rating is None:
            continue
        else:
            for genre in genres:
                # We check if genre is not disabled
                if genre in forbiden:
                    pass
                else:
                    # Check if the given country exists in the dictionary
                    if not country_dict.get(country):
                        country_dict[country] = {genre : rating}
                        country_count[country] = {genre : 1}
                    else:
                        # Country exists, then
                        # Check if given genre exists
                        if not country_dict[country].get(genre):
                            country_dict[country][genre] = rating
                            country_count[country][genre] = 1
                        else:
                            country_dict[country][genre] += rating
                            country_count[country][genre] += 1
        print("===Progress " + str(int(num/n*100)) + "%===")
    print("===DONE!===")

def best_sum(dictionary):
    '''
    '''
    # Gets the best film genres by sum of points
    best = {}
    for country in dictionary:
        rating = 0
        for genre in dictionary[country]:
            if float(dictionary[country][genre]) > rating:
                rating = dictionary[country][genre]
                best[country] = (genre, rating)
    return best


def popularity(dictionary):
    '''
    '''
    # Gets the most popular film genre of every country
    best = {}
    for country in dictionary:
        amount = 0
        for genre in dictionary[country]:
            if float(dictionary[country][genre]) > amount:
                amount = dictionary[country][genre]
                best[country] = (genre, amount)
    return best


def best_genre_middle(dictionary1, dictionary2):
    '''
    '''
    # Gets the best genre by middle of points
    best = {}
    for country in dictionary1:
        points = 0
        for genre in dictionary1[country]:
            if float(dictionary1[country][genre]) / float(dictionary2[country][genre]) > points:
                points = float(dictionary1[country][genre]) / float(dictionary2[country][genre])
                best[country] = (genre, points)
    return best


def saving(d_sum, d_pop, d_middle):
    '''
    '''
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(__location__, "output.txt"), "w+")
    f.write("===============================================================================================================================================\n")
    f.write("Best film genres by sum of ratings\n")
    for country in d_sum:
        f.write(str(country) + " : " + str(d_sum[country][1]) + "\nGenre : " + str(d_sum[country][0]) + "\n\n")

    f.write("===============================================================================================================================================\n")
    f.write("Most popular film genres\n")
    for country in d_pop:
            f.write(str(country) + " : " + str(d_pop[country][0]) + "\nAmount : " + str(d_pop[country][1]) + "\n\n")

    f.write("===============================================================================================================================================\n")
    f.write("Best film genres by average rating\n")
    for country in d_middle:
            f.write(str(country) + " : " + str(d_middle[country][1]) + "\nGenre : " + str(d_middle[country][0]) + "\n\n")

    f.close()

if __name__ == "__main__":
    # If the package isn`t already installed the installation will begin
    try:
        import imdb
    except:
        install('IMDBpy')
        import imdb

    ia = imdb.IMDb()

    # We use two dict to store data globaly
    # We use this dict to store the sum of ratings by genres
    country_dict = {}


    # This dict looks like this:
    # {country1:
    #   {genre1:rating,
    #   genre2:rating}
    # ,
    # country2:
    #   {genre1:rating,
    #   genre2:rating}
    # }

    # We use this dict to store the amount of titles by genres
    country_count = {}

    # The dict looks like this:
    # {country1:
    #   {genre1:count,
    #   genre2:count}
    # ,
    # country2:
    #   {genre1:rating,
    #   genre2:rating}
    # }
    n = int(input("Imput number of movies: "))
    main(n)