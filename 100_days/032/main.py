import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random

load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("PASSWORD")
to_email = os.getenv("TO_EMAIL")
todays_day_of_week = dt.datetime.now().weekday()

# ---------------------------- CHECK DAY OF WEEK ------------------------- #
if todays_day_of_week == 2:
    enable_sending = True
    with open("quotes.txt") as f:
        quotes = f.read().splitlines()
else:
    enable_sending = False

# ---------------------------- FUNCTIONS --------------------------------- #

def select_random_quotes():
    quote = random.choice(quotes)
    return quote

def send_email():
    global to_email
    if enable_sending:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject:Quote of the day!\n\nHello, dear {to_email}\n{select_random_quotes()}\nWish you a good day!"
            )
    print("Email sent!")

# ---------------------------- MAIN -------------------------------------- #
send_email()