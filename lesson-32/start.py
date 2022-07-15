import smtplib

my_email = ""
password = ""


with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="",
        msg="Subject:hello\n\nThis is a body of email"
    )

import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
print(day_of_week)
print(year)

date_of_birth = dt.datetime(year=1991, month=9, day=19)
print(date_of_birth)
