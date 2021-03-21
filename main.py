# import required modules
import smtplib
import datetime
import calendar
import os


def add_months(source_date, months):
    """A function that adds certain number of months to the source_date"""

    month = source_date.month - 1 + months
    year = source_date.year + month // 12
    month = month % 12 + 1
    day = min(source_date.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


start_day = datetime.date(2021, 3, 21)
current_day = datetime.date.today()

months4 = add_months(source_date=start_day, months=4)
months8 = add_months(source_date=start_day, months=8)
months12 = add_months(source_date=start_day, months=12)
months16 = add_months(source_date=start_day, months=16)
months20 = add_months(source_date=start_day, months=20)
months24 = add_months(source_date=start_day, months=24)
months28 = add_months(source_date=start_day, months=28)

# send a pay raise email every 4 months
if (current_day == months4) or (current_day == months8) or (current_day == months12) or (current_day == months16) \
        or (current_day == months20) or (current_day == months24) or (current_day == months28):

    with open(file="pay_raise.txt", encoding="utf-8") as letter:

        content = letter.read()

    my_email = os.environ["MY_EMAIL"]
    pass_word = os.environ["PASSWORD"]
    other_email = os.environ["BOSS_EMAIL"]
    text = f"Subject:Meeting Review\n\n{content}"

    # send an email requesting a pay raise to boss
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pass_word)
        connection.sendmail(from_addr=my_email, to_addrs=other_email,
                            msg=text.encode('ascii', 'ignore').decode('ascii'))
