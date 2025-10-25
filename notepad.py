import os # For checking file existence (optional, but good practice)

# Global variable to store the notepad's content
notepad_content = ""

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Simple Python Console Notepad ---")
    print("1. Write/Edit Text")
    print("2. View Text")
    print("3. Save to File")
    print("4. Load from File")
    print("5. Clear Notepad")
    print("6. Exit")
    print("-------------------------------------")

def write_edit_text():
    """Allows the user to input multiline text into the notepad."""
    global notepad_content
    print("Enter your text (type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    notepad_content = "\n".join(lines)
    print("Text updated.")

def view_text():
    """Displays the current content of the notepad."""
    if not notepad_content: # Check if the content is empty
        print("Notepad is empty.")
    else:
        print("\n--- Current Notepad Content ---")
        print(notepad_content)
        print("-------------------------------")

def save_to_file():
    """Saves the current notepad content to a user-specified file."""
    filename = input("Enter filename to save (e.g., mynotes.txt): ")
    try:
        with open(filename, 'w') as file: # Open file in write mode ('w')
            file.write(notepad_content)
        print(f"Content saved to '{filename}'.")
    except IOError: # Catch potential errors during file operations
        print(f"Error: Could not save to file '{filename}'.")

def load_from_file():
    """Loads content from a user-specified file into the notepad."""
    global notepad_content
    filename = input("Enter filename to load from (e.g., mynotes.txt): ")
    if not os.path.exists(filename): # Check if file exists before trying to open
        print(f"Error: File '{filename}' not found.")
        return
    try:
        with open(filename, 'r') as file: # Open file in read mode ('r')
            notepad_content = file.read()
        print(f"Content loaded from '{filename}'.")
    except IOError:
        print(f"Error: Could not load from file '{filename}'.")

def clear_notepad():
    """Clears all content from the notepad."""
    global notepad_content
    notepad_content = ""
    print("Notepad content cleared.")

def main():
    """Main function to run the notepad application."""
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError: # Handle non-integer input
            print("Invalid input. Please enter a number between 1 and 6.")
            continue # Continue to the next loop iteration

        if choice == 1:
            write_edit_text()
        elif choice == 2:
            view_text()
        elif choice == 3:
            save_to_file()
        elif choice == 4:
            load_from_file()
        elif choice == 5:
            clear_notepad()
        elif choice == 6:
            print("Exiting Notepad. Goodbye!")
            break # Exit the loop
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main() # Run the main application function when the script is executed
