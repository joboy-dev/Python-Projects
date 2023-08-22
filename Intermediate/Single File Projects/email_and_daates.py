# import smtplib

# working with smtplib for email
# ------------------------------- #

# my_email = 'devjoboy@gmail.com'
# password = 'jdeasnpdzvzwjqqw'

# # create connection
# with smtplib.SMTP('smtp.gmail.com', 587) as connection:
#     # secure connection
#     connection.starttls() 
#     # login
#     connection.login(user=my_email, password=password)
#     # send mail
#     connection.sendmail(from_addr=my_email, to_addrs='devtesting941@gmail.com', msg='Subject: Hello\n\nHow are you doing today?')



# working with datetime for dates
# -------------------------------- #

import datetime as dt

# get current date and time
now = dt.datetime.now()
# print(now)
# print(now.time()

# creating a datetime of your own
dob = dt.datetime(year=2003, month=11, day=22)
print(dob.month)
