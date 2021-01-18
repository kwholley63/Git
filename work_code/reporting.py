import csv
import datetime
import operator
from datetime import date, timedelta
import os
import sys
#
P1 = 0
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
loop_count = 0
critical = 0
p2_ack_total = 0
p3_ack_total = 0
p4_ack_total = 0
ack_totals = 0
ack_percent = 0
counter = 0
opened_yesterday = 0
resolved_yesterday = 0
ticket_list = []


snow_file_path = "K:\\snow_file.csv"
#snow_file2_path = "K:\\snow_file2_new.csv"
tickets_path = "K:\\tickets.csv"
 
dump_file_path = "K:\\dump_file.csv"
daily_stats_file_path = "K:\\daily_stats.csv"
totals_file_path = "K:\\total_file.csv"

def cleanup():
  print("Cleaup old Files")
  if os.path.isfile(snow_file_path):
    os.remove(snow_file_path)
  else:
    print(" ")
  if os.path.isfile(tickets_path):
    os.remove(tickets_path)
  else:
    print(" ")
  if os.path.isfile(dump_file_path):
    os.rename(dump_file_path, snow_file_path)
  else:
    print("file not found. Extract needs to be completed", dump_file_path)
    sys.exit(1)
cleanup()

def Ticket_data():
  print("calling ticket data")

def Ticket_stats():
  print("calling ticket stats")


Ticket_data()
print("ticket data")

with open (snow_file_path,'r') as snow_file:
    with open (tickets_path,'w', newline='') as tickets:
        readablefile = csv.reader(snow_file)
        writablefile = csv.writer(tickets) 
        tickets.write("ticket, hpsm_ticket,P_Type, breach_time, assigned to, impact, priority, created on, description, Priority, Status"+"\n")
        for row in readablefile:
            print("\n")
            break
        for row in readablefile:
            date_format = datetime.datetime.strptime(row[12], '%m/%d/%Y %H:%M')
            if row[6] == "2 - Medium" and row[7] == "3 - Moderate" and row[8] != "Resolved" or row[6] == "2 - Medium" and row[7] == "4 - Low" and row[8] != "Resolved":
              P2= P2 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              description = str(row[3])
              breach_time = (str(date_format + timedelta(hours=8)))
              lst=(ticket, hpsm_ticket, "P2", breach_time, assigned, impact, priority, created, description )
              writablefile.writerow(lst)
            elif row[6] == "1 - High" and row[7] == "3 - Moderate" and row[8] != "Resolved" or row[6] == "2 - Medium" and row[7] == "2 - High" and row[8] != "Resolved":
              P1= P1 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              description = str(row[3])
              breach_time = (str(date_format + timedelta(hours=8)))
              lst=(ticket, hpsm_ticket, "P1", breach_time, assigned, impact, priority, created, description )
              writablefile.writerow(lst)
            elif row[6] == "3 - Low" and row[7] == "3 - Moderate" and row[8] != "Resolved" or row[6] == "3 - Low" and row[7] == "4 - Low" and row[8] != "Resolved":
              P3= P3 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              description = str(row[3])
              breach_time = (str(date_format + timedelta(hours=24)))
              lst=(ticket, hpsm_ticket, "P3", breach_time, assigned, impact, priority, created, description )
              writablefile.writerow(lst)
            elif row[6] == "3 - Low" and row[7] == "5 - Very Low" and row[8] != "Resolved":
              P4= P4 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              description = str(row[3])
              breach_time = (str(date_format + timedelta(hours=120)))
              lst=(ticket, hpsm_ticket, "P4", breach_time, assigned, impact, priority, created, description )
              writablefile.writerow(lst)
            else:
              loop_count = loop_count +1
              #print(" ---- Processing, Kevin is thinking of you...  ---- ")
        print(" The totals are P1 P2 P3 and P4 = ", P1, P2, P3, P4)
        #exec(open("./stats.py").read())

Ticket_stats()
print("ticket stats")

with open (snow_file_path,'rt') as snow_file:
    readablefile = csv.reader(snow_file)
    for row in readablefile:                                                                      
        print("\n")
        break
    for row in readablefile:
        check_open_date = str(row[12])
        check_resolved_date = str(row[17])                                                                                                                              
        ticket = str(row[0])
        open_date=str(check_open_date)
        resolved_date = str(check_resolved_date)
        space_in_date=open_date.split(" ")
        space_in_resolved_date=resolved_date.split(" ")                                                
        date_length=len(space_in_date)
        resolved_date_length=len(space_in_resolved_date)                                              
        key=space_in_date[0]
        key_resolved=space_in_resolved_date[0]                                                        
        final_len=len(key)
        final_len_resolved=len(key_resolved)
        check_open_date = (check_open_date[0:final_len])
        check_resolved_date = (check_resolved_date[0:final_len_resolved])                               
        yesterday = (date.today() + timedelta(-1))                                                
        new_date = yesterday.strftime('X%m/X%d/%Y').replace('X0','X').replace('X','')             
        if new_date == check_open_date:
            opened_yesterday = opened_yesterday +1                                                                  
            open_time = str(row[12])
            if check_open_date == check_resolved_date :
              resolved_yesterday = resolved_yesterday +1
              percent_resolved = '{0:.2f}'.format((resolved_yesterday/opened_yesterday * 100))
            else:
              resolved_yesterday - resolved_yesterday
        else:
          opened_yesterday - opened_yesterday

with open (daily_stats_file_path, 'a') as stats_file:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    stats_lst = (now, opened_yesterday, resolved_yesterday, percent_resolved)
    writablefile = csv.writer(stats_file)
    writablefile.writerow(stats_lst)
    stats_file.close()
##
with open (totals_file_path, 'a') as totals_file:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    totals_lst = (now, P1, P2, P3, P4, opened_yesterday, resolved_yesterday, percent_resolved)
    writablefile = csv.writer(totals_file)
    writablefile.writerow(totals_lst)
    totals_file.close()
    
print(opened_yesterday, "Were opened Yesterday")
print(resolved_yesterday, "Were Resolved yesterday")
print(percent_resolved, "of the tickets opened yesterday were resolved yesterday")
#added 1/18/2021
