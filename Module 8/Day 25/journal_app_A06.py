# Journal Application

def read_journal(file_path):
    try:
        # This will read the entries from our file
        with open(file_path, 'r') as file: # With closes our file when this code block ends. Keep it short. Closes the file even if there's an error.
            entries = file.readlines() # Gets all lines in the file
    except FileNotFoundError:
        # This is in [] as our function should return a list.
        return ["Error: The file does not exist. Please check the file path."]
    
    return entries

def write_journal(file_path, entry):
    # This will append the entry to our journal
    try:
        # 'a' opens our file in append mode
        with open(file_path, 'a') as file: # With closes our file when this code block ends. Keep it short. Closes the file even if there's an error.
            file.write(f"{entry}\n")
    except FileNotFoundError:
        # This is in [] as our function should return a list.
        return ["Error: The file does not exist. Please check the file path."] 

def main():
    file_path = "journal_A06.txt"
    
    # This will be our main loop for managing our journal
    while True:
        action = input("Do you want to (r)ead the journal or (w)rite a new entry? (q to quit)").strip().lower()

        match action:
            case "r":
                entries = read_journal(file_path)

                print(f"Journal Entries of {file_path}:\n")
                for index, entry in enumerate(entries):
                    print(f"{index + 1}: {entry}")
            case "w":
                new_entry = input("Enter your journal entry: ").strip()
                write_journal(file_path, new_entry)
                print("Entry added to the journal.")
            case "q":
                print("Goodbye!")
                break

if __name__ == "__main__":
    main()