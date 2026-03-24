import csv # module for handling csv data

def read_nhl_teams(file_path):
    all_teams = []

    try:
        with open(file_path, "r") as file:
           reader = csv.DictReader(file)

           for team in reader:
               all_teams.append(team) 

    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")

    return all_teams

def sort_teams_by_stat(teams, column, reverse=True, top_n=5):
    # helper function aka special functions (in python)
    def get_score(entry):
        return entry[column]
    
    sorted_teams = sorted(teams, key=get_score, reverse=reverse) # get_score to determine which column to sort by

    return sorted_teams[:top_n] # returns the teams from 0 to top_n - 1

def main():
    file_path = "data/nhl_teams_data_2024_2025.csv"

    teams = read_nhl_teams(file_path)

    # Get the column names from the first item in teams (header row)
    columns = list(teams[0].keys())

    print("Available stats to sort by:")
    for index, column in enumerate(columns, 1):
        print(f"{index}. {column}")

    choice = int(input("Enter the number of the stat to sort by: ")) - 1 # resets the index to 0 base
    COLUMN = columns[choice] # no longer static, so name should be changed to column
    
    #COLUMN = "xGoalsFor" # a variable in all caps is called a static variable ie. we shouldn't change it

    top_teams = sort_teams_by_stat(teams, COLUMN)

    print(f"Top 5 NHL Teams by {COLUMN}:\n")

    for index, team in enumerate(top_teams, 1): # putting a 1 here lets my printed index start at 1
        print(f"{index}. {team["team"]} - {team[COLUMN]}")

if __name__ == "__main__":
    main()