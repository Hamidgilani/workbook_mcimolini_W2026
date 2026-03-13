import csv

from pprint import pprint

def read_nhl_teams(file_path):
    # This is going to read all of our teams data
    all_teams = []

    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

            for team in reader:
                all_teams.append(team)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    
    return all_teams

def sort_teams_by_stat(teams, column, reverse=True, top_n=5):

    # special function aka helper function
    def get_score(entry):
        return entry[column]
    
    # key will be the column we're sorting by
    # sorted_teams = sorted(teams, key=get_score, reverse=reverse) # defaults to sorting biggest to smallest now
    # we can replace the function above with a lambda function. Basically a short lived simple function.
    sorted_teams = sorted(teams, key = lambda entry: entry[column], reverse=reverse) # defaults to sorting biggest to smallest now

    data = []
    for team in sorted_teams:
        data.append({
            "Team": team["team"],
            column: team[column]
        })

    return data[:top_n] # will return the first top_n items (0 to top_n - 1)

def main():
    file_path = "data/nhl_teams_data_2024_2025_A03.csv"
    teams = read_nhl_teams(file_path)
    #COLUMN = "xGoalsFor" # all caps variable names means it's a "static" variable ie. we shouldn't change it

    columns = list(teams[0].keys())
    print ("Available statistics to sort by:")
    for index, column in enumerate(columns):
        print(f"{index + 1}. {column}")

    choice = int(input("Enter the column number to sort by:")) - 1 # subtracting 1 as our print is 1 based instead of 0 based
    COLUMN = columns[choice]

    top_teams = sort_teams_by_stat(teams, COLUMN)
    # print(f"NHL Teams from {file_path}:\n")
    # pprint(teams) # this just formats and prints our dictionary

    print(f"Top 5 NHL Teams by {COLUMN}:\n")
    for index, team in enumerate(top_teams):
        print(f"{index + 1}. {team['team']} - {team[COLUMN]}")

if __name__ == "__main__":
    main()