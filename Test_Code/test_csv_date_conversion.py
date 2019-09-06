import csv
import datetime
from datetime import timedelta

with open ('C:\\Users\\kwhol\\my_python_code\\python.csv','rt') as csvfile:
    readablefile = csv.reader(csvfile)
    #writablefile = csv.writer(csvfile)
    for row in readablefile:
        ##date_format = datetime.datetime.strptime(row[1], '%m/%d/%y')
        date_format = datetime.datetime.strptime(row[1], '%m/%d/%y %H:%M')
        print("\n"+ "this is the ticket time")
        print(date_format)
        print("\n"+"this is the breach time")
        print (date_format + timedelta(hours=8))
        #print("\n"+"this is the breach time")
        #print(date_format)
        #writablefile.writerow(date_format)