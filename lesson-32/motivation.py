import random


my_email = ""
password = ""



with open("quotes.txt") as data:
    list_motivation = data.readlines()
    print(random.choice(list_motivation))

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 4:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=random.choice(list_motivation)
        )
