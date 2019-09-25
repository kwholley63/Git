import csv
import time
import datetime
from datetime import date, timedelta
today = time.strftime("%m/%d/%Y")
#print(today)
#exit(0)
counter = 0 
with open ('H:\\python code\\hpsm_file2.csv','rt') as hpsm_file:
    readablefile = csv.reader(hpsm_file)
    for row in readablefile:                                                                     # This loop is to skip over the header record
            print("\n")
            break;
    for row in readablefile:
        check = str(row[2])
        check_date = (check[0:9])
        yesterday = (date.today() + timedelta(-1))
        new_date = yesterday.strftime('X%m/X%d/%Y').replace('X0','X').replace('X','')
        #
        #print(new_date)
        #
        check_date = (check[0:9])
        print("The file date is>>",check_date) 
        print("\n the date of yesterday was >>", new_date)
        if new_date == check_date:
            #print("TRUE")
            counter = counter +1
            print(counter)
        else:
            #print(False) 
            #print(check_date)  
        #exit(0)
        #print("\n")
            print("The total tickets opened yesterday is >> ",counter)
