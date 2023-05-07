from datetime import datetime as dt

now = dt.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m-%d-%Y, %H:%M:%S")
print("tarih ve zaman:",date_time)
tarih=now.strftime("%d-%m-%Y")	
print("tarih:",tarih)