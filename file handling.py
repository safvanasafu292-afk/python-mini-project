def write_note():
    note = input("Write your note: ")

    with open("mynotes.txt", "a") as file:
        file.write(note + "\n")

    print("Note saved successfully!")


def read_notes():
    try:
        with open("mynotes.txt", "r") as file:
            notes = file.readlines()

            if not notes:
                print("No notes found.")
            else:
                print("\n--- Your Notes ---")
                for line in notes:
                    print(line.strip())

    except FileNotFoundError:
        print("No notes file found yet. Write a note first!")


def main():
    while True:
        print("\n===== Simple Note-Taking App =====")
        print("1. Write a new note")
        print("2. View all notes")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            write_note()

        elif choice == "2":
            read_notes()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


main()