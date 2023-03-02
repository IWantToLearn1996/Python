PLACEHOLDER = "[name]"

with open("./Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    # Creates automatically a List
    names = names_file.readlines()
    print(names)

with open("./Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    # Creates automatically a List
    letters = letter_file.read()
    print(letters)
    for name in names:
        stripped_name = name.strip()
        new_letter = letters.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"./Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)