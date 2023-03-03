import smtplib
import datetime as dt
import random
import pandas

my_email = "pythonemailtest08@gmail.com"
password = "hliefomgxgnalpzw"

now = dt.datetime.now()
month = now.month
day = now.day

data = pandas.read_csv("birthdays.csv")
mum = data.name[0]
dad = data.name[1]

PLACEHOLDER = "[NAME]"
letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt" ]

def person(who):

    with open(random.choice(letter_list)) as letter_file:
        letter = letter_file.read()
        new_letter = letter.replace(PLACEHOLDER, who)
        print(new_letter)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Making our Email encrypted - Not readable from other users
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="pythonemailtest09@gmail.com",
                            msg=f"Subject:Happy Birthday\n\n{new_letter}")

if day == 4 and month == 3:
    person(mum)
elif day == 3 and month == 3:
    person(dad)
else:
    pass
