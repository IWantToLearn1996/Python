import smtplib

my_email = "pythonemailtest08@gmail.com"
password = "hliefomgxgnalpzw"
# password = "JustATestingEmail!1"

# Connection of the Email for gmail.com
with smtplib.SMTP("smtp.gmail.com") as connection:
    # Making our Email encrypted - Not readable from other users
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="pythonemailtest09@gmail.com",
                        msg="Subject:Trial\n\nThis is the Body of the Email.")
