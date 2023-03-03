import smtplib
import datetime as dt
import random

my_email = "pythonemailtest08@gmail.com"
password = "hliefomgxgnalpzw"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Making our Email encrypted - Not readable from other users
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="pythonemailtest09@gmail.com",
                            msg=f"Subject:Friday Motivation\n\n{quote}")