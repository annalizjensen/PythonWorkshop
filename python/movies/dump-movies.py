# dump-movies.py

# read the movies.csv file and dump it out nicely
# formatted

f = open("movies.csv")
lines = f.readlines()
lines = lines[1:]

def get_columns(line):
    # return the title, year and budget columns
    # from the input line
    line = line[:-2] # remove trailine \r\n from line
    if line[0] == '"':
        _, title, rest = line.split('"')
        _, year, _, budget, _, _ = rest.split(',')
    else:
        columns = line.split(",")
        title, year, _, budget, _, _ = columns
    return title, year, budget

for i, line in enumerate(lines):
    title, year, budget = get_columns(line)
    print i, title, year, budget
