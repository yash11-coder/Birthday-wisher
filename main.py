import smtplib, pandas, random, re
import datetime as dt

email = 'test@mail.com'  #Type your mail Id
password = 'password'    #Type your password here

letters = {0:'letter_1.txt', 1:'letter_2.txt', 2:'letter_3.txt'}
p = random.randint(0,2)

now = dt.datetime.now()
d = pandas.read_csv("birthdays.csv").to_dict()

for i in range(0,2):
    if d['month'][i] == now.month and d['day'][i] == now.day:
        with smtplib.SMTP("smtp.gmail.com") as connection:    # here in the brackets you need to add smtp address of your mail if it is gmail it will have one address and if it yahoo it will have another
            connection.starttls()
            connection.login(email, password)

            with open(f"letter_templates/{letters[p]}", mode="r+") as f:
                wishes = re.sub('\[NAME]', d['name'][i], f.read())

            connection.sendmail(from_addr=email,  to_addrs=d['email'][i], msg=f"Subject:Wishes\n\n{wishes}")





