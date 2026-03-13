# Journal Application

def read_journal(file_path):
    # Always use 'with' when you call open() so that file cleanup happens!!!
    try:
        with open(file_path, "r") as file: # 'r' opens the file in read mode IF IT EXISTS
            entries = file.readlines() # lines plural as we want them all
    # Must have an appropriate return (list in this case) even when there are errors.
    except FileNotFoundError:
        return ["Error: The file does not exist. Please check the file path."]
    
    return entries

def write_entry(file_path, entry):
    # We still need to open the file to write to it
    # We will use 'a' to append to the end of the file
    try:
        with open(file_path, "a") as file: 
            file.write(f"{entry}\n")
        
        print("Entry written successfully.")
    except FileNotFoundError:
        print("Unable to write, file not found!")

def main():
    file_path = "journal_A03.txt"

    is_exiting = False

    while not is_exiting:
        action = input("Do you want to (r)ead or (w)rite to the Journal? (q to quit): ").strip().lower()

        match action:
            case 'r':                       
                entries = read_journal(file_path)

                print(f"Journal Entries of {file_path}:")
                for index, entry in enumerate(entries):
                    print(f"{index + 1}) {entry}")
            case 'w':
                new_entry = input("Enter your journal entry: ")
                write_entry(file_path, new_entry)
            case 'q':
                is_exiting = True
                print("Goodbye!")
            case _: # default case for invalid input
                print("I can't do that Dave...")

if __name__ == "__main__":
    main()