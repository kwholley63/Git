import csv
import datetime
import binascii
from datetime import timedelta
import sys ,operator
import collections
#
# Have to still format the number column work on this fix. For now format the number cells when done running the tool
#
P2 = 0
P3 = 0
P4 = 0
breach = 0
warning = 0
premier_count = 0
hold_count = 0
resolved = 0
closed = 0
transferred = 0
Acknowledged = 0
D1MSTTECHOPS = 0
D1MSTTECHOPSAUTO = 0
jpmc = 0
ticket_list = []
#
with open ('H:\\python code\\hpsm_file.csv','rt') as hpsm_file:                                    # Have to format the ticket column to be a number
    with open ('H:\\python code\\hpsm_file1.csv','w') as hpsm_file1:                         
        readablefile = csv.reader(hpsm_file)
        writablefile = csv.writer(hpsm_file1)
        hpsm_file1.write("ticket,severity,open_time,breach_time,breach_state,premier,assignee_name,assigned_to,status,alert_name,queue_name"+"\n")
        for row in readablefile:                                                                     # This loop is to skip over the header record
            print("\n")
            break;
        for row in readablefile:
            date_format = datetime.datetime.strptime(row[2], '%m/%d/%Y %H:%M')
            if row[8] == "P2" and row[3] != "Resolved":
                P2 = P2 +1
                assignee_name = str(row[9])
                ticket = int(row[0])
                severity = str(row[8])
                open_time = str(row[2])
                breach_state = str(row[7])
                description = str(row[5])
                queue_name = str(row[6])
                alert_name = str(row[5])
                if queue_name == str(row[6]) == "D1MSTTECHOPS":
                    D1MSTTECHOPS = D1MSTTECHOPS +1
                else:
                    D1MSTTECHOPSAUTO = D1MSTTECHOPSAUTO +1
                if description.find("PREMIER") == -1:
                    premier = " "
                else:
                    premier = "TRUE"
                    #print(queue_name)
                    premier_count = premier_count +1
                if description.find("hold") == -1:
                    hold = " "
                else:
                    #
                    if queue_name == "D1MSTTECHOPSAUTO":
                        hold = " "
                    else:
                        hold = "TRUE"
                        hold_count = hold_count +1
                        ticket_list.append(row[0])
                    #
                if breach_state == "Breached":
                    breach = breach +1
                if breach_state == "Warning":
                    warning = warning +1  
                breach_time = (str(date_format + timedelta(hours=8)))
                tkt=(ticket)
                name = description.find("Splunk Alert:30159_Alert_SM2_OPSMON_High_Priority_Alerts") #== -1
                if name != -1:
                    alert_name = (description[name:100])
                    lst=(ticket, severity, open_time, breach_time, breach_state, premier, assignee_name,queue_name,alert_name )
                    writablefile.writerow(lst)
                else:
                    lst=(ticket, severity, open_time, breach_time, breach_state, premier, assignee_name,queue_name )
                    writablefile.writerow(lst)
            elif row[8] == "P3" and row[3] != "Resolved":
                P3 = P3 +1
                assignee_name = str(row[9])
                ticket = int(row[0])
                severity = str(row[8])
                open_time = str(row[2])
                breach_state = str(row[7])
                description = str(row[5])
                queue_name = str(row[6])
                alert_name = str(row[5])
                if queue_name == str(row[6]) == "D1MSTTECHOPS":
                    D1MSTTECHOPS = D1MSTTECHOPS +1
                else:
                    D1MSTTECHOPSAUTO = D1MSTTECHOPSAUTO +1
                if description.find("PREMIER") == -1:
                    premier = " "
                else:
                    premier = "TRUE"
                    #print(queue_name)
                    premier_count = premier_count +1
                if description.find("hold") == -1:
                    hold = " "
                else:
                    #
                    if queue_name == "D1MSTTECHOPSAUTO":
                        hold = " "
                    else:
                        hold = "TRUE"
                        hold_count = hold_count +1
                        ticket_list.append(row[0])
                #
                if breach_state == "Breached":
                    breach = breach +1
                if breach_state == "Warning":
                    warning = warning +1
                breach_time = (str(date_format + timedelta(hours=24)))
                tkt=(ticket)
                name = description.find("Splunk Alert:30159_Alert_SM2_OPSMON_High_Priority_Alerts") #== -1
                if name != -1:
                    alert_name = (description[name:100])
                    lst=(ticket, severity, open_time, breach_time, breach_state, premier, assignee_name,queue_name,alert_name )
                    writablefile.writerow(lst)
                else:
                    lst=(ticket, severity, open_time, breach_time, breach_state, premier, assignee_name,queue_name)
                    writablefile.writerow(lst)
            elif row[8] == "P4" and row[3] != "Resolved":
                P4 = P4 +1
                assignee_name = str(row[9])
                ticket = int(row[0])
                severity = str(row[8])
                open_time = str(row[2])
                breach_state = str(row[7])
                description = str(row[5])
                queue_name = str(row[6])
                alert_name = str(row[5])
                if queue_name == str(row[6]) == "D1MSTTECHOPS":
                    D1MSTTECHOPS = D1MSTTECHOPS +1
                else:
                    D1MSTTECHOPSAUTO = D1MSTTECHOPSAUTO +1
                if description.find("PREMIER") == -1:
                    premier = " "
                else:
                    premier = "TRUE"
                    #print(queue_name)
                    premier_count = premier_count +1
                if description.find("hold") == -1:
                    hold = " "
                else:
                    #
                    if queue_name == "D1MSTTECHOPSAUTO":
                        hold = " "
                    else:
                        hold = "TRUE"
                        hold_count = hold_count +1
                        ticket_list.append(row[0])
                    #
                if breach_state == "Breached":
                    breach = breach +1
                if breach_state == "Warning":
                    warning = warning +1
                breach_time = (str(date_format + timedelta(hours=120)))
                tkt=(ticket)
                name = description.find("Splunk Alert:30159_Alert_SM2_OPSMON_High_Priority_Alerts") #== -1
                if name != -1:
                    alert_name = (description[name:100])
                    lst=(ticket, severity, open_time, breach_time, breach_state, premier, assignee_name,queue_name,alert_name)
                    writablefile.writerow(lst)
                else:
                    lst=(ticket, severity, open_time, breach_time, breach_state, premier, assignee_name,queue_name)
                    writablefile.writerow(lst)
                ##writablefile.writerow(lst)
            ##
            ##if row[3] == "Resolved":
            ##    resolved = resolved +1
            ##elif row[3] == "Closed":
            ##    closed = closed +1
            ##elif row[3] == "Acknowledged":
            ##    Acknowledged = Acknowledged +1
            #elif row[3] =="Transferred":
            ##    Transferred = Transferred +1
            ##else:
            ##    transferred = transferred +1
            #     print(row[3])
            ##
#
# Sort the data and produce The final file
#
    data = csv.reader(open('H:\\python code\\hpsm_file1.csv'),delimiter=',')
    sortedlist = sorted(data, key=operator.itemgetter(3))                                   # 3 specifies according to fourth column we want to sort. Breach Time
                                                                                            # now write the sorte result into new CSV file
    with open("H:\\python code\\hpsm_file2.csv", "wb") as f:
        f.write("ticket,severity,open_time,breach_time,breach_state,premier,assignee_name,queue_name,alert_name,assigned_to,status"+"\n")       # Put the header records back in the final file
        fileWriter = csv.writer(f, delimiter=',')
        for row in sortedlist:
            fileWriter.writerow(row)
    hpsm_file.close()                                                                  # Close all our files 
    hpsm_file1.close()
    f.close()
#
#Update the daily stats file
#
with open ('H:\\python code\\daily_stats.csv','a') as stats_file:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total=P2+P3+P4
    stats_lst = (now,P2,P3,P4,total)
    writablefile = csv.writer(stats_file)
    writablefile.writerow(stats_lst)
    stats_file.close()
#
print("The total of open tickets is >> ",P2+P3+P4)
#print("\n")
print("The number of P2 tickets >> ",P2)
#print("\n")
print("The number of P3 tickets >> ",P3)
#print("\n")
print("The number of P4 tickets >> ",P4)
#print("\n")
print("The number of breached tickets >> ", breach)
#print("\n")
print("The number of warning tickets >> ", warning)
#print("\n")
#print("The number of resolved tickets >> ", resolved)
#print("\n")
#print("The number of closed tickets >> ", closed)
#print("\n")
#print("The number of transferred tickets >> ", transferred)
#print("\n")
print("The number of premier tickets is >> ", premier_count)
#print("\n")
print ("The number of tickets in D1MSTTECHOPS queue is >> ", D1MSTTECHOPS)
#print("\n")
print ("The number of tickets in D1MSTECHOPSAUTO queue is >> ", D1MSTTECHOPSAUTO)
#print("\n")
print ("The number of tickets with hold description, this is a potential ITSM & HPSM Conflict >> " ,hold_count)
print("\n")
print(ticket_list)
print("\n")
print("COMPLETE .... Your File is ready H:\\python code\\csv_test_file2.csv ")
print("COMPLETE .... Your Stats File is ready H:\\python code\\daily_stats.csv ")
