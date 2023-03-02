import random, pandas
# numbers = [1, 2, 3]
# new_list = [n+1 for n in numbers]
# print(new_list)
#
# new_list2 = [n*2 for n in range(1,5)]
# print(new_list2)
#
# name = "Nikos"
# letter_list = [letter for letter in name]
# print(letter_list)
#
# names = ["Nikos", "Maria", "Vaso", "Giota", "Stef"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
#
# long_names = [name.upper() for name in names if len(name) > 4]
# print(long_names)
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n*n for n in numbers]
# print(squared_numbers)
# even_numbers = [n for n in numbers if n%2 ==0]
# print(even_numbers)

# with open("file1.txt") as file1:
#     file_1 = file1.readlines()
#     #print(file_1)
#
# with open("file2.txt") as file2:
#     file_2 = file2.readlines()
#     #print(file_2)
#
# duplicate_list = [int(num) for num in file_1 if num in file_2]
# print(duplicate_list)

# names = ["Nikos", "Maria", "Vaso", "Giota", "Stef"]
# students_score = {student:random.randint(1, 100) for student in names}
# print(students_score)
# passed_students = {student:score for (student, score) in students_score.items() if score >= 60 }
# print(passed_students)

# sentence = "Which team is considered the Best team in the WORLD"
# result = {word:len(word) for word in sentence.split()}
# print(result)

# weather = {
# #     "Monday": 12,
# #     "Tuesday": 14,
# #     "Wednesday": 15,
# #     "Thursday": 14,
# #     "Friday": 21,
# #     "Saturday": 22,
# #     "Sunday": 24,
# # }
# #
# # weather_F = {day:temp_c*9/5 +32 for (day, temp_c) in weather.items()}
# # print(weather_F)

student_dict = {
    "student": ["Nikos", "Maria", "Giota"],
    "score": [56, 76, 98]
}

# Looping through a Dictionary
for (key,value) in student_dict.items():
    print(key, value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Looping through a DataFrame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Nikos":
        print(row.score)
