#Data was taken from https://datasets.imdbws.com/
#to get result use files from archives title.ratings.tsv.gz title.crew.tsv.gz title.basics.tsv.gz name.basics.tsv.gz
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    Function prints the list of 100 worst films and their directors, list and graph of genres of these films
    and list and graph of age of directors.
    """
    num_films = 100
    rating_df = pd.read_csv("title.ratings.tsv", sep = '\t')
    directors_df = pd.read_csv("title.crew.tsv", sep = '\t')
    titles_df = pd.read_csv("title.basics.tsv", sep = '\t', dtype={"startYear": object, "endYear": object})
    names_df = pd.read_csv("name.basics.tsv", sep = '\t')

    set_tconst_directors1 = set(directors_df['tconst'])
    set_tconst_titles1 = set(titles_df['tconst'])
    set_tconst_rating = set(rating_df['tconst'])

    directors_df = directors_df[directors_df['directors'].str.find('\\N') == -1]
    titles_df = titles_df[titles_df['genres'].str.find('\\N') == -1]

    set_tconst_directors2 = set(directors_df['tconst'])
    set_tconst_titles2 = set(titles_df['tconst'])

    extra_index1 = set_tconst_directors1 - set_tconst_directors2
    extra_index2 = set_tconst_titles1 - set_tconst_titles2
    extra_index = extra_index1 | extra_index2
    extra_index = extra_index.intersection(set_tconst_rating)
    extra_index = list(extra_index)

    rating_df = rating_df.set_index(['tconst'])
    rating_df = rating_df.drop(extra_index)

    films_min_rating = rating_df.sort_values(['averageRating', 'numVotes'], ascending=[True, False])
    lst_keys = films_min_rating.index.tolist()[0:num_films]
    lst_ratings = films_min_rating['averageRating'].iloc[0:num_films].tolist()

    rating_dct = dict()
    for i in range(num_films):
        key = lst_keys[i]
        value = lst_ratings[i]
        rating_dct[key] = value

    titles_df = titles_df.set_index(['tconst'])
    title_dct = dict()
    lst_titles = []
    for i in range(num_films):
        key = lst_keys[i]
        title_dct[key] = titles_df.loc[lst_keys[i], 'originalTitle']
        lst_titles.append(titles_df.loc[lst_keys[i], 'originalTitle'])

    directors_df = directors_df.set_index(['tconst'])
    directors_dct = dict()
    for i in range(num_films):
        key = lst_keys[i]
        value = directors_df.loc[lst_keys[i], 'directors']
        if value.count('nm') != 1:
            value = value.split(',')
        directors_dct[key] = value

    names_df = names_df.set_index(['nconst'])
    names_dct = dict()
    lst_directors = []
    lst_births = []
    for key in lst_keys:
        if type(directors_dct[key]) != list:
            idx = directors_dct[key]
            names_dct[key] = names_df.loc[idx, 'primaryName']
            lst_directors.append(names_df.loc[idx, 'primaryName'])
            lst_births.append(names_df.loc[idx, 'birthYear'])
        else:
            lst_names = directors_dct[key]
            lst_temp = []
            names_dct[key] = []
            for i in range(len(lst_names)):
                names_dct[key].append(names_df.loc[lst_names[i], 'primaryName'])
                lst_temp.append(names_df.loc[lst_names[i], 'birthYear'])
            names_dct[key] = ', '.join(names_dct[key])
            lst_directors.append(names_dct[key])
            lst_births.append(lst_temp)

    genres_dct = dict()
    lst_genres = []
    for i in range(num_films):
        key_dct = lst_titles[i]
        genres_dct[key_dct] = titles_df.loc[lst_keys[i], 'genres']
        lst_genres.append(titles_df.loc[lst_keys[i], 'genres'])

    lst_start = []
    for i in range(num_films):
        lst_start.append(titles_df.loc[lst_keys[i], 'startYear'])

    lst_age = []
    for i in range(num_films):
        if type(lst_births[i]) == str:
            if lst_births[i].isdigit():
                lst_age.append(int(lst_start[i]) - int(lst_births[i]))
            else:
                lst_age.append('No information')
        else:
            lst_age.append([])
            for element in lst_births[i]:
                if element.isdigit():
                    lst_age[i].append(str(int(lst_start[i]) - int(element)))
                else:
                    lst_age[i].append('No information')
            lst_age[i] = ', '.join(lst_age[i])
    result_dct = dict()
    result_dct['Title'] = list(title_dct.values())
    result_dct['Director'] = list(names_dct.values())
    result_dct['Rating'] = lst_ratings

    result_df = pd.DataFrame(result_dct)
    result_df.index += 1
    print("The list of worst movies and their directors".center(150))
    print(result_df.to_string())

    lst_genres_graph = []
    for element in lst_genres:
        if element.count(',') > 0:
            element = element.split(',')
            for i in range(len(element)):
                lst_genres_graph.append(element[i])
        else:
            lst_genres_graph.append(element)

    lst_times = [1 for i in range(len(lst_genres_graph))]
    genres_graph_df = pd.DataFrame(list(zip(lst_genres_graph, lst_times)), columns =['Genres', 'Number of movies'.center(10)])
    new = pd.pivot_table(genres_graph_df, index = ["Genres"], aggfunc=np.sum)
    print("Genres of worst movies".center(120))
    print(new)
    lst_y = new['Number of movies'].tolist()
    lst_x = new.index.tolist()
    plt.rcParams['figure.figsize'] = (20,6)
    plt.plot(lst_x, lst_y)
    plt.xlabel('Genre')
    plt.ylabel('Number of films')
    plt.title('Genres of the worst films')
    plt.show()

    lst_ages_graph = []
    for element in lst_age:
        if type(element) == str:
            element = element.split(',')
            for i in range(len(element)):
                if element[i].count('No information') != 1:
                    lst_ages_graph.append(int(element[i]))
        else:
            if element != 'No information':
                lst_ages_graph.append(element)

    lst_times = [1 for i in range(len(lst_ages_graph))]
    ages_graph_df = pd.DataFrame(list(zip(lst_ages_graph, lst_times)), columns =['Age', 'Number of directors'.center(10)])
    new = pd.pivot_table(ages_graph_df, index = ['Age'], aggfunc=np.sum)
    print("How old were directors, when they filmed worst movies".center(120))
    print(new)

    plt.rcParams['figure.figsize'] = (10, 3)
    plt.scatter(new.index, new['Number of directors'])
    plt.xlabel('Age')
    plt.ylabel('Number of directors')
    plt.title('How old were directors when they made worst films')
    plt.show()

main()
