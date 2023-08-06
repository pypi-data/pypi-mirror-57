import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
import gzip
from io import BytesIO, StringIO
import ssl
import os.path


def display_intro():
    """
    Research Introduction.
    :return: None
    """
    print("This is a research by Dmytro Lopushanskyy called " +\
          "\"The Most Popular Genres Among Top Movies Sorted by Years\"")


def get_criteria(recursion_depth=0):
    """
    Getting analysis criteria from user.
    :return: (int, int, float, int)
    """
    defaults = input("\nDo you want to use the default movies criteria? (yes/no) ")
    if defaults.lower() == 'yes':
        print("Using default criteria:\nyear_from = 1990\nyear_to = 2020\nrating = 8.0\nvotes = 1000")
        return 1990, 2020, 8.0, 1000
    elif defaults.lower() == 'no':
        year_from = input("Enter FROM year: ")
        year_to = input("Enter TO year: ")
        rating = input("Enter minimum movie rating: ")
        votes = input("Enter minimum number of votes: ")
        try:
            return int(year_from), int(year_to), float(rating), int(votes)
        except ValueError:
            pass

    print('\nWrong data entered!')
    if recursion_depth < 1000:
        return get_criteria(recursion_depth+1)
    else:  # if user entered wrong data 1000 times use defaults
        print("\nUsing default criteria:\nyear_from = 1990\nyear_to = 2020\nrating = 8.0\nvotes = 1000")
        return 1990, 2020, 8.0, 1000


def download(url):
    # Download database
    out_file_path = url.split("/")[-1][:-3]
    print('Downloading Database From: {}'.format(url))
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    compressed_file = BytesIO(response.read())
    decompressed_file = gzip.GzipFile(fileobj=compressed_file)

    # Extract database
    with open(out_file_path, 'w') as outfile:
        outfile.write(decompressed_file.read().decode('utf-8', errors="ignore"))

    return outfile.name


def get_movies_by_rating(rating, votes):
    """
    The function for reading the file 'title.ratings.tsv' and
    returning a list of movies with the number of votes and rating
    bigger than given rating and votes.
    :param rating: float
    :param votes: int
    :return: list
    """
    movies_titles_list = []
    if not os.path.isfile('title.ratings.tsv'):
        # File doesn't exist in the directory
        download("https://datasets.imdbws.com/title.ratings.tsv.gz")

    with open("title.ratings.tsv", encoding='utf-8', errors='ignore') as file:
        for line in file:
            line = line.strip().split()
            if line[0] != 'tconst':
                try:
                    if float(line[1]) > rating and int(line[2]) > votes:
                        movies_titles_list.append(line[0])
                except:
                    pass
    movie_titles_set = set(movies_titles_list)
    print("....." + str(len(movie_titles_set)) + ' movies by rating and votes selected.....\n')
    return movie_titles_set


def get_movies(year_from, year_to, movie_titles_set):
    """
    The function for reading the file 'title.basics.tsv' and
    returning a list of movies that math all of the given criteria.
    :param year_from: int
    :param year_to: int
    :param movie_titles_set: list
    :return: list
    """
    final_films_list = []
    film_length = 0

    if not os.path.isfile('title.basics.tsv'):
        # File doesn't exist in the directory
        download("https://datasets.imdbws.com/title.basics.tsv.gz")

    with open("title.basics.tsv", encoding='utf-8', errors='ignore') as file:
        for line in file:
            try:
                line = line.strip().split()
                if line[1] == 'movie':
                    if year_from <= int(line[-4]) <= year_to:
                        if line[0] in movie_titles_set:
                            movie_titles_set.remove(line[0])  # to prevent from duplicates
                            final_films_list.append((line[0], int(line[-4]), line[-1], ' '.join(line[2:-6])))
                            film_length = len(final_films_list)
                            if film_length % 50 == 0:
                                print("....." + str(film_length) + ' movies in given time period selected.....')
            except:
                pass
    print("....." + str(film_length) + ' movies in given time period selected.....')
    return final_films_list


def optimize_raw_values(raw_values):
    """
    Optimizing criteria from the user to get better visualisation.
    :param raw_values: dict
    :return: dict
    """
    new_dict = {}
    if len(raw_values.keys()) > 10:
        group_number = len(raw_values.keys()) // 5
        i = 0
        years_list = sorted(list(raw_values.keys()))
        for i in range(0, len(years_list)//group_number):
            if i == len(years_list)//group_number - 1:
                end_index = -1
            else:
                end_index = group_number * i + group_number - 1

            if years_list[2*i] != years_list[end_index]:
                dict_key = str(years_list[group_number*i]) + '-' + str(years_list[end_index])
                new_dict[dict_key] = {}
                for year in range(years_list[group_number*i], years_list[end_index]):
                    try:
                        for genre_in_year in raw_values[year].keys():
                            if genre_in_year in new_dict[dict_key].keys():
                                new_dict[dict_key][genre_in_year] += raw_values[year][genre_in_year]
                            else:
                                new_dict[dict_key][genre_in_year] = raw_values[year][genre_in_year]
                    except KeyError:
                        pass
            else:
                dict_key = str(sorted(list(raw_values.keys()))[group_number*i])
                new_dict[dict_key] = {}
                for genre_in_year in raw_values[years_list[group_number*i]].keys():
                    if genre_in_year in new_dict[dict_key].keys():
                        new_dict[dict_key][genre_in_year] += raw_values[years_list[group_number*i]][genre_in_year]
                    else:
                        new_dict[dict_key][genre_in_year] = raw_values[years_list[group_number*i]][genre_in_year]
            # print(new_dict)
    else:
        new_dict = raw_values
    return new_dict


def analyze_films(final_movies_list):
    """
    Analyzing given list of movies and preparing the data
    about the most popular genres for visualisation.
    :param final_movies_list: list
    :return: dict
    """
    print("\n.....Analyzing genres of " + str(len(final_movies_list)) + " movies.....\n")

    genre_dict = {}
    for movie in final_movies_list:
        genres = [x.lower() for x in movie[2].split(',')]
        if '\\n' in genres:
            genres.remove('\\n')
        if movie[1] not in genre_dict.keys():
            genre_dict[movie[1]] = {}
        for genre in genres:
            if genre in genre_dict[movie[1]].keys():
                genre_dict[movie[1]][genre] += 1
            else:
                genre_dict[movie[1]][genre] = 1

    print("Raw values: " + str(genre_dict) + "\n")

    genre_dict = optimize_raw_values(genre_dict)

    years = []
    most_popular_genres = {}

    # loop for getting the most popular genres in each year range
    for year in genre_dict:
        years.append(year)
        total_films = []
        for films_number in genre_dict[year].values():
            total_films.append(films_number)
        total_films.sort(reverse=True)
        # print(total_films, genre_dict[year])

        for genre in genre_dict[year]:
            if genre_dict[year][genre] in total_films[0:3]:
                most_popular_genres[genre] = []

    # loop for getting data for each selected genre from previous loop
    for year in genre_dict:
        for genre in most_popular_genres:
            total_films_number = 0
            for films_number in genre_dict[year].values():
                total_films_number += films_number

            if genre in genre_dict[year].keys():
                most_popular_genres[genre].append(int((genre_dict[year][genre]*100)/total_films_number))
            else:
                most_popular_genres[genre].append(0)

    years = [str(year) for year in sorted(years)]

    # print(years)
    # print(most_popular_genres)
    return years, most_popular_genres


def display_results(genres_dict, years):
    """
    Display results in form of visualized data
    :param genres_dict: dict
    :param years: list
    :return: dict
    """
    print("The statistic visualisation window has been opened!\n")
    df = pd.DataFrame(genres_dict, index=years)
    ax = df.plot.bar(rot=0)
    plt.show()


def main():
    """
    Main function that coordinates the research data analysis
    :return: None
    """
    display_intro()
    year_from, year_to, rating, votes = get_criteria()

    print('\nSearching for films by given criteria')
    print('This process might take a couple of minutes.\n')

    film_titles_list = get_movies_by_rating(rating, votes)
    final_movies_list = get_movies(year_from, year_to, film_titles_list)

    years, genres_dict = analyze_films(final_movies_list)

    display_results(genres_dict, years)

    print("Thank you for taking the time to view this research!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\nError: " + str(e))
        print("Please try entering different values!\nif you've discovered a bug, text to Dmytro")
        print("Thank you for taking the time to view this research!")
