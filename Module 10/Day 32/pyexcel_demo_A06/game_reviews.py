import pyexcel as pex # as lets us rename our imports to anything we want. Kinda like a variable.

def create_reviews_file(reviews, output_file):
    pex.save_as(array=reviews, dest_file_name=output_file) # opens the file, writes all the lines to it, closes it. Check for errors throughout

def add_column_to_file(input_file, output_file):
    # load the existing file
    sheet = pex.get_sheet(file_name=input_file)
    
    recommendations = ["Recommendation"]

    rows = sheet.to_array() # turns our sheet of columns into a list of columns

    for index, row in enumerate(rows[1:]): # this loops through row starting at index 1

        match row[2]: # check and compare against the score present in each row
            case score if 90 <= score <= 100: # if the score for the row is 90-100
                recommendations.append("Highly Recommended")
            case score if 80 <= score <= 90: # if the score for the row is 80-90
                recommendations.append("Recommended")
            case score if 70 <= score <= 80: # if the score for the row is 70-80
                recommendations.append("Average")
            case _:
                recommendations.append("Not Recommended") # if score is anything else

    sheet.column += recommendations

    sheet.save_as(output_file)

def main():
    GAME_REVIEWS_FILE_NAME = "game_reviews.xlsx"
    RECOMMENDED_GAME_FILE_NAME = "recommended_game_reviews.xlsx"

    # the data we're going to write to the excel file
    GAME_REVIEWS = [
        ["Title", "Platform", "Score"],
        ["Elden Ring", "PC", 95],
        ["Stardew Valley", "Switch", 89],
        ["Cyberpunk 2077", "PS5", 82],
        ["No Man's Sky", "PC", 90],
        ["Gollum", "PS5", 43],
    ]

    create_reviews_file(GAME_REVIEWS, GAME_REVIEWS_FILE_NAME)
    print(f"Created {GAME_REVIEWS_FILE_NAME} with game reviews.")

    add_column_to_file(GAME_REVIEWS_FILE_NAME, RECOMMENDED_GAME_FILE_NAME)
    print(f"Created {RECOMMENDED_GAME_FILE_NAME} with game recommendations.")

if __name__ == "__main__":
    main()