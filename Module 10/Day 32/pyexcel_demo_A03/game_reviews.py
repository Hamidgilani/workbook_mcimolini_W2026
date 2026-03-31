import pyexcel as pex # as keyword allows us to shorten or change the names of our imports.

def create_game_reviews_excel_file(reviews, output_file):
    pex.save_as(array=reviews, dest_file_name=output_file)

def add_recommendation_column(input_file, output_file):
    # load the input file
    sheet = pex.get_sheet(file_name=input_file)

    # add the column
    recommendations = ["Recommendation"]

    # get all of the rows from my sheet
    rows = sheet.to_array()

    # itterate through the rows
    for row_index, row_values in enumerate(rows[1:]): # 1: skips the first row (our header row)
        score = row_values[2] # 2 is the index of score in our row

        if score >= 90:
            recommendations.append("Highly Recommended")
        elif score >= 80:
            recommendations.append("Recommended")
        elif score >= 70:
            recommendations.append("Average")
        else:
            recommendations.append("Not Recommended")
    
    # adds our list to the end of the columns currently in the file
    sheet.column += recommendations

    # save and update
    sheet.save_as(output_file)

def main():
    GAME_REVIEWS_FILE_NAME = "game_reviews.xlsx"
    RECOMMENDED_GAME_REVIEWS_FILE_NAME = "recommended_game_reviews.xlsx"
    # the data we're going to write to the excel file
    GAME_REVIEWS = [
        ["Title", "Platform", "Score"],
        ["Elden Ring", "PC", 95],
        ["Stardew Valley", "Switch", 89],
        ["Cyberpunk 2077", "PS5", 82],
        ["No Man's Sky", "PC", 90],
        ["Gollum", "PS5", 43],
    ]

    create_game_reviews_excel_file(GAME_REVIEWS, GAME_REVIEWS_FILE_NAME)
    print(f"Created {GAME_REVIEWS_FILE_NAME} with game reviews.")

    add_recommendation_column(GAME_REVIEWS_FILE_NAME, RECOMMENDED_GAME_REVIEWS_FILE_NAME)
    print(f"Created {RECOMMENDED_GAME_REVIEWS_FILE_NAME} with recommendations.")


if __name__ == "__main__":
    main()