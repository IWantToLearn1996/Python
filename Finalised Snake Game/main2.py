# Opening and Reading a File that it is in this directory and Close it in the end due to With-as.

# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)


# Opening, Deleting previous text and Writing a File with the new text that you provide and Close it in the end.

# with open("my_file.txt", mode= "w") as file:
#     file.write("Xyse")


# Opening, Appending/Writing a File with the new text that you provide and Close it in the end.

# with open("my_file.txt", mode= "a") as file:
#     file.write("Xyse")


# Creates a New File when it does not exist and Writes in it.

with open("new_file.txt", mode="w") as file:
    file.write("New Text.")


