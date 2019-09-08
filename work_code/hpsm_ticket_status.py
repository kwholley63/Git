import csv
import datetime
import binascii
from datetime import timedelta
import sys ,operator
import collections
#
# Have to still format the number column work on this fix. 
# For now format the number cells when done running the tool
# Have to remove resolved. work on this fix
#  
#
P2 = 0
P3 = 0
P4 = 0
breach = 0
warning = 0
premier_count = 0
resolved = 0
#
with open ('H:\\python code\\csv_test_file.csv','rt') as csvfile:                                    # Have to format the ticket column to be a number
    with open ('H:\\python code\\csv_test_file1.csv','w') as csv_test_file1:                         
        readablefile = csv.reader(csvfile)
        writablefile = csv.writer(csv_test_file1)
        csv_test_file1.write("ticket,severity,open_time,breach_time,breach_state,premier"+"\n")
        for row in readablefile:                                                                     # This loop is to skip over the header record
            print("\n")
            break;
        for row in readablefile:
            date_format = datetime.datetime.strptime(row[2], '%m/%d/%Y %H:%M')
            if row[8] == "P2" and row[3] != "Resolved":
                P2 = P2 +1
                ticket = int(row[0])
                severity = str(row[8])
                open_time = str(row[2])
                breach_state = str(row[9])
                description = str(row[5])
                if description.find("Premier") == -1:
                    premier = " "
                else: 
                    premier = "TRUE"
                    premier_count = premier_count +1
                if breach_state == "Breached":
                    breach = breach +1
                if breach_state == "Warning":
                    warning = warning +1  
                breach_time = (str(date_format + timedelta(hours=8)))
                tkt=(ticket)
                lst=(ticket, severity, open_time, breach_time, breach_state, premier)
                writablefile.writerow(lst)
            elif row[8] == "P3" and row[3] != "Resolved":
                P3 = P3 +1
                ticket = int(row[0])
                severity = str(row[8])
                open_time = str(row[2])
                breach_state = str(row[9])
                description = str(row[5])
                if description.find("Premier") == -1:
                    premier = " "
                else: 
                    premier = "TRUE"
                    premier_count = premier_count +1
                if breach_state == "Breached":
                    breach = breach +1
                if breach_state == "Warning":
                    warning = warning +1
                breach_time = (str(date_format + timedelta(hours=24)))
                lst=(ticket, severity, open_time, breach_time, breach_state, premier)
                writablefile.writerow(lst)
            elif row[8] == "P4" and row[3] != "Resolved":
                P4 = P4 +1
                ticket = int(row[0])
                severity = str(row[8])
                open_time = str(row[2])
                breach_state = str(row[9])
                description = str(row[5])
                if description.find("Premier") == -1:
                    premier = " "
                else: 
                    premier = "TRUE"
                    premier_count = premier_count +1
                if breach_state == "Breached":
                    breach = breach +1
                if breach_state == "Warning":
                    warning = warning +1
                breach_time = (str(date_format + timedelta(hours=120)))
                lst=(ticket, severity, open_time, breach_time, breach_state, premier)
                writablefile.writerow(lst)
            resolved = resolved +1
#
# Sort the data and produce The final file
#
    data = csv.reader(open('H:\\python code\\csv_test_file1.csv'),delimiter=',')
    sortedlist = sorted(data, key=operator.itemgetter(3))                                   # 3 specifies according to fourth column we want to sort. Breach Time
                                                                                            # now write the sorte result into new CSV file
    with open("H:\\python code\\csv_test_file2.csv", "wb") as f:
        f.write("ticket,severity,open_time,breach_time,breach_state,premier"+"\n")          # Put the header records back in the final file
        fileWriter = csv.writer(f, delimiter=',')
        for row in sortedlist:
            fileWriter.writerow(row)
    csv_test_file1.close()                                                                  # Close all our files 
    csvfile.close()
    f.close()
#
csv_test_file1.close()
print("The total of open tickets is",P2+P3+P4)
print("The number of P2 P3 and P4 tickets", P2,P3,P4)
print("The number of breached tickets is", breach)
print("The number of warning tickets is", warning)
print("The number of resolved tickets is", resolved)
print("The number of premier tickets is", premier_count)
print("COMPLETE .... Your File is ready H:\\python code\\csv_test_file2.csv ")
