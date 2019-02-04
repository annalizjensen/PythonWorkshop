# avg-movies.py

# calculate the average budget of all movies
# in the movies.csv file


def decade(year):
    # for any integer year, return the first year of that decade
    return year / 10 * 10

def get_movies_as_list_of_strings():
    # Read the contents of the movies CSV file into a list of lines,
    # skipping the first line, as it is just a header. Returns the list of
    # lines.
    f = open("movies.csv")
    lines = f.readlines()
    lines = lines[1:]
    return lines


def convert_line_to_dict(line):
    # input is a string representing one line of text from the CSV movies file.
    # returns a dictionary of columns
    line = line[:-2]  # remove trailine \r\n from line
    if line[0] == '"':
        _, title, rest = line.split('"')
        _, year, length, budget, rating, votes = rest.split(',')
    else:
        columns = line.split(",")
        title, year, length, budget, rating, votes = columns
    return {'title': title, 'year': int(year), 'budget': budget,
            'length':length, 'rating':rating, 'votes':votes}


def calculate_budget_stats(movies):
    # input is a list of movies, where each movies is a
    # dictionary with keys title, year, budget
    # budget is either a number, or "NA" if unknown
    # calculates an average of all movies, and returns
    # the average, and the count, and max of the movies considered
    # return None for average if we count 0 items in the list
    count = 0
    total = 0
    mx = 0
    for movie in movies:
        budget = movie['budget']
        if budget != "NA":
            count = count + 1
            budget = int(budget)
            total = total + budget
            if budget > mx:
                mx = budget
    if count == 0:
        average = None
    else:
        average = total / count
    return count, average, mx

def calculate_average_rating(movies):
    # input is a list of movies, where each movies is a dictionary
    # calculates an average rating of all movies, and returns
    # the average, and the count of the movies considered
    count = 0
    total = 0
    for movie in movies:
        rating = movie['rating']
        count = count + 1
        total = total + float(rating)
    average = total / count
    return count, average

def convert_strings_list_to_movies_list(movie_lines):
    movies = []
    for line in movie_lines:
        movie = convert_line_to_dict(line)
        movies.append(movie)
    return movies

def group_movies_by_decade(movies):
    # given a list of movie dictionaries, return a dictionary that
    # groups movies by decade. The key is the integer decade, and
    # the value is a list of movies for that decade
    movies_by_decade = {}
    for m in movies:
        d = decade(m['year'])
        ls = movies_by_decade.get(d, [])
        ls.append(m)
        movies_by_decade[d] = ls
    return movies_by_decade

def main():
    # read in the movie file as a list of strings:
    movie_lines = get_movies_as_list_of_strings()

    # convert the list of strings to dictionary about each movie
    movies = convert_strings_list_to_movies_list(movie_lines)

    movies_by_decade = group_movies_by_decade(movies)
    # calculate the average budget of the list of movies

    for decade in sorted(movies_by_decade.keys()):
        ml = movies_by_decade[decade]
        cnt, avg, mx = calculate_budget_stats(ml)
        if cnt != 0:
            print "the average budget for the {} movies from the {}'s that report a budget is ${:1,}.".format(cnt, decade, avg)
            print "the mx budget for the {} movies from the {}'s that report a budget is ${:1,}.".format(cnt, decade, mx)

    cnt, avg, mx = calculate_budget_stats(movies)
    print "the average budget for the {} that report a budget is ${:1,}.".format(cnt, avg)
    print "the mx budget for the {} movies that report a budget is ${:1,}.".format(cnt, mx)


if __name__ == '__main__':
    main()
