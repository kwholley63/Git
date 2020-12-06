import csv
import datetime
import operator
from datetime import date, timedelta
from datetime import datetime
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
critical = 0
p2_ack_total = 0
p3_ack_total = 0
p4_ack_total = 0
ack_totals = 0
ack_percent = 0
counter = 0
p1_sla_met = 0
p1_sla_miss = 0
p2_sla_met = 0
p2_sla_miss = 0
p3_sla_met = 0
p3_sla_miss = 0
p4_sla_met = 0
p4_sla_miss = 0

p1_totals = 0
p2_totals = 0
p3_totals = 0
p4_totals = 0


opened_yesterday = 0
resolved_yesterday = 0
ticket_list = []


snow_file_path = "K:\\snow_file.csv"
snow_file1_path = "K:\\snow_file1_new.csv"
 
dump_file_path = "K:\\dump_file.csv"
daily_stats_file_path = "K:\\daily_stats.csv"
totals_file_path = "K:\\totals_file.csv"



def Ticket_SLA():
  print("calling ticket SLA")

 

Ticket_SLA()
print("ticket SLA")

with open (snow_file_path,'r') as snow_file:
    with open (snow_file1_path,'w', newline='') as snow_file1:
        readablefile = csv.reader(snow_file)
        ##writablefile = csv.writer(snow_file1) 
        ##snow_file1.write("ticket, hpsm_ticket,P_Type, breach_time, assigned to, impact, priority, created on, description"+"\n")
        for row in readablefile:
            print("\n")
            break
        for row in readablefile:
            date_format = datetime.strptime(row[12], '%m/%d/%Y %H:%M')
            if row[6] == "2 - Medium" and row[7] == "3 - Moderate" or row[6] == "2 - Medium" and row[7] == "4 - Low":
              P2= P2 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              ##print(row[12], row[17], "created and resolved times")
              ##description = str(row[3])
              breach_time = (str(date_format + timedelta(hours=8))) 
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%#d/%Y %H:%M") 
              ##print(new_breach_time)
              #breach_time.strftime('%m/%d/%Y %H:%M')
              if resolved < new_breach_time:
                ##print (row[12], row[17], new_breach_time, "..........................................created, resolved, breached, GOOD")
                ##print ("The ticket is", ticket)
                ##print (" The Created time is" , created)
                ##print (" The resolved time is" ,resolved)
                ##print ("The breached time is" , breach_time)
                ##print (" The new Breach time is", new_breach_time)
                p2_sla_met = p2_sla_met +1
                print("SLA MET", p2_sla_met, ticket)
                print (row[12], row[17], new_breach_time, "..........................................created, resolved, breached, GOOD")
                #break
              else:
                p2_sla_miss = p2_sla_miss +1
                print("SLA MISS", p2_sla_miss, ticket)
                print (row[12], row[17], new_breach_time, "created, resolved, breached, BAD")
              ##lst=(ticket, hpsm_ticket, "P2", breach_time, assigned, impact, priority, created, description )
              ##writablefile.writerow(lst)
            elif row[6] == "1 - High" and row[7] == "3 - Moderate" or row[6] == "2 - Medium" and row[7] == "2 - High":
              P1= P1 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              ##print(row[12], row[17], "created and resolved times")
              #description = str(row[3])
              breach_time = (str(date_format + timedelta(hours=8)))
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%#d/%Y %H:%M")
              ##print(new_breach_time)
              #breach_time.strftime('%m/%d/%Y %H:%M')
              if resolved < new_breach_time:
                ##print (row[12], row[17], new_breach_time, "..........................................created, resolved, breached, GOOD")
                ##print ("The ticket is", ticket)
                ##print (" The Created time is" , created)
                ##print (" The resolved time is" ,resolved)
                ##print ("The breached time is" , breach_time)
                ##print (" The new Breach time is", new_breach_time)
                p1_sla_met = p1_sla_met +1
                ##print(p1_sla_met)
                #break
              else:
                p1_sla_miss = p1_sla_miss +1
                ##print(p1_sla_miss)
                ##print (row[12], row[17], breach_time, "created, resolved, breached, BAD")
              #lst=(ticket, hpsm_ticket, "P1", breach_time, assigned, impact, priority, created, description )
              #writablefile.writerow(lst)
            elif row[6] == "3 - Low" and row[7] == "3 - Moderate" or row[6] == "3 - Low" and row[7] == "4 - Low":
              P3= P3 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              ##print(row[12], row[17], "created and resolved times")
              #description = str(row[3])
              breach_time = (str(date_format + timedelta(hours=24)))
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%#d/%Y %H:%M")
              ##print(new_breach_time)
              #breach_time.strftime('%m/%d/%Y %H:%M')
              if resolved < new_breach_time:
                ##print (row[12], row[17], new_breach_time, "..........................................created, resolved, breached, GOOD")
                ##print ("The ticket is", ticket)
                ##print (" The Created time is" , created)
                ##print (" The resolved time is" ,resolved)
                ##print ("The breached time is" , breach_time)
                ##print (" The new Breach time is", new_breach_time)
                p3_sla_met = p3_sla_met +1
                ##print(p3_sla_met)
                #break
              else:
                p3_sla_miss = p3_sla_miss +1
                ##print(p3_sla_miss)
                ##print (row[12], row[17], breach_time, "created, resolved, breached, BAD")
              #lst=(ticket, hpsm_ticket, "P3", breach_time, assigned, impact, priority, created, description )
              #writablefile.writerow(lst)
            elif row[6] == "3 - Low" and row[7] == "5 - Very Low" and row[8]:
              P4= P4 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              #description = str(row[3])
              breach_time = (str(date_format + timedelta(hours=120)))
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%m/%d/%Y %H:%M")
              ##print(new_breach_time)
              #breach_time.strftime('%m/%d/%Y %H:%M')
              if resolved < new_breach_time:
                ##print (row[12], row[17], new_breach_time, "..........................................created, resolved, breached, GOOD")
                ##print ("The ticket is", ticket)
                ##print (" The Created time is" , created)
                ##print (" The resolved time is" ,resolved)
                ##print ("The breached time is" , breach_time)
                ##print (" The new Breach time is", new_breach_time)
                p4_sla_met = p4_sla_met +1
                ##print(p4_sla_met)
                #break
              else:
                p4_sla_miss = p4_sla_miss +1
                ##print(p4_sla_miss)
                ##print (row[12], row[17], breach_time, "created, resolved, breached, BAD")
              #lst=(ticket, hpsm_ticket, "P4", breach_time, assigned, impact, priority, created, description )
              #writablefile.writerow(lst)
            else:
              ##print(" ---- Processing, Kevin is thinking of you...  ---- ")
        #print(" The totals are P1 P2 P3 and P4 = ", P1, P2, P3, P4)
        #exec(open("./stats.py").read())
              p1_totals = p1_sla_met + p1_sla_miss
              p2_totals = p2_sla_met + p2_sla_miss
              p3_totals = p3_sla_met + p3_sla_miss
              p4_totals = p4_sla_met + p4_sla_miss
              #print(p4_totals)

P1_Percent_SLA = '{0:.2f}'.format((p1_sla_met/p1_totals * 100))
P2_Percent_SLA = '{0:.2f}'.format((p2_sla_met/p2_totals * 100))
P3_Percent_SLA = '{0:.2f}'.format((p3_sla_met/p3_totals * 100))
P4_Percent_SLA = '{0:.2f}'.format((p4_sla_met/p4_totals * 100))

print("The Percentage Of P1 Tickets That Met The SLA", P1_Percent_SLA)
print("The Percentage Of P2 Tickets That Met The SLA",P2_Percent_SLA)
print("The Percentage Of P3 Tickets That Met The SLA",P3_Percent_SLA)
print("The Percentage Of P4 Tickets That Met The SLA",P4_Percent_SLA)

print(p1_sla_met, p1_sla_miss,"p1 met and p1 miss")
print(p2_sla_met, p2_sla_miss,"p2 met and p2 miss")
print(p3_sla_met, p3_sla_miss,"p3 met and p3 miss")
print(p4_sla_met, p4_sla_miss,"p4 met and p4 miss")
        
#print("Hello")
"""
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

"""
