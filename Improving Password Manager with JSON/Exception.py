# File Not Found
try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print("Key does NOT exist")
    print(f"the key {error_message} does NOT exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed")
    #raise TypeError("I made this Error")

height = float(input("Give Height: "))
weight = int(input("Give Weight: "))

if height > 3 or weight > 300:
    raise ValueError("Invalid number of Height or Weight!")

bmi = weight / height ** 2
print(bmi)