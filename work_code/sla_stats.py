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
p1_sla_miss = 1
p2_sla_met = 0
p2_sla_miss = 1
p3_sla_met = 0
p3_sla_miss = 1
p4_sla_met = 0
p4_sla_miss = 1

p1_totals = 0
p2_totals = 0
p3_totals = 0
p4_totals = 0


opened_yesterday = 0
resolved_yesterday = 0
ticket_list = []


snow_file_path = "K:\\snow_file.csv"
#snow_file1_path = "K:\\snow_file1_new.csv"
 
#dump_file_path = "K:\\dump_file.csv"
#daily_stats_file_path = "K:\\daily_stats.csv"
#totals_file_path = "K:\\totals_file.csv"
sla_file_path = "K:\\sla_file.csv"

val = int(input("Enter your value: "))
#print(type(val))
if val <=0 or val > 12:
  print("invalid entry, The value must be between 1-12")
  sys.exit()
else:
  #print(type(val))
  val = str(val)
  #print(type(val))
  
#print(val)


def Ticket_SLA():
  print("calling ticket SLA")
   

 

Ticket_SLA()
print("ticket SLA")

with open (snow_file_path,'r') as snow_file:
    #with open (sla_file_path,'w', newline='') as sla_file:
        readablefile = csv.reader(snow_file)
        #writablefile = csv.writer(sla_file) 
        ##snow_file1.write("ticket, hpsm_ticket,P_Type, breach_time, assigned to, impact, priority, created on, description"+"\n")
        for row in readablefile:
            print("\n")
            break
        for row in readablefile:
          ##
          for row in readablefile:
            created = str(row[12])
            #print(created)
            x = created.split("/")
            #print("this is the split", x)
            index = x[0]
            #print(type(index))
            #print("The Value - ", index)
            if index == val:
              print("")
              ##print("it worked")
            else:
              ##print (" it did not work")
              break
          ##
            date_format = datetime.strptime(row[12], '%m/%d/%Y %H:%M')
            if row[6] == "2 - Medium" and row[7] == "2 - High" or row[6] == "2 - Medium" and row[7] == "4 - Low":
              P2= P2 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              breach_time = (str(date_format + timedelta(hours=8))) 
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%#d/%Y %H:%M") 
              if resolved < new_breach_time:
                p2_sla_met = p2_sla_met +1
                ##print(ticket,"good med high med low")
              else:
                p2_sla_miss = p2_sla_miss +1
                ##print(ticket,"BAD med high med low")
                ##
            if row[6] == "2 - Medium" and row[7] == "3 - Moderate":
              P2= P2 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              breach_time = (str(date_format + timedelta(hours=8))) 
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%#d/%Y %H:%M") 
              if resolved < new_breach_time:
                p2_sla_met = p2_sla_met +1
                ##print(ticket,"good med and mod")
              else:
                p2_sla_miss = p2_sla_miss +1
                ##print(ticket,"BAD med and mod")
                ##
            elif row[6] == "1 - High" and row[7] == "2 - High" or row[6] == "1 - High" and row[7] == "3 - Moderate":
              P1= P1 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              breach_time = (str(date_format + timedelta(hours=8)))
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%#d/%Y %H:%M")
              if resolved < new_breach_time:
                p1_sla_met = p1_sla_met +1
                ##print("here")
              else:
                p1_sla_miss = p1_sla_miss +1
                ##print(ticket, created, resolved, new_breach_time)
                #print(ticket, created, resolved, new_breach_time)
            elif row[6] == "3 - Low" and row[7] == "3 - Moderate" or row[6] == "3 - Low" and row[7] == "4 - Low":
              P3= P3 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              breach_time = (str(date_format + timedelta(hours=24)))
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%#d/%Y %H:%M")
              if resolved < new_breach_time:
                p3_sla_met = p3_sla_met +1
              else:
                p3_sla_miss = p3_sla_miss +1
            elif row[6] == "3 - Low" and row[7] == "5 - Very Low" and row[8]:
              P4= P4 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              breach_time = (str(date_format + timedelta(hours=120)))
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%m/%d/%Y %H:%M")
              if resolved < new_breach_time:
                p4_sla_met = p4_sla_met +1
              else:
                p4_sla_miss = p4_sla_miss +1
            else:
              p1_totals = (p1_sla_met + p1_sla_miss)
              p2_totals = (p2_sla_met + p2_sla_miss)
              p3_totals = (p3_sla_met + p3_sla_miss)
              p4_totals = (p4_sla_met + p4_sla_miss)

P1_Percent_SLA = '{0:.2f}'.format((p1_sla_met/p1_totals * 100))
P2_Percent_SLA = '{0:.2f}'.format((p2_sla_met/p2_totals * 100))
P3_Percent_SLA = '{0:.2f}'.format((p3_sla_met/p3_totals * 100))
P4_Percent_SLA = '{0:.2f}'.format((p4_sla_met/p4_totals * 100))

#P1_Percent_SLA = '{0:.2f}'.format((p1_sla_met/p1_totals * 100))
#P2_Percent_SLA = '{0:.2f}'.format((p2_sla_met/p2_totals * 100))
#P3_Percent_SLA = '{0:.2f}'.format((p3_sla_met/p3_totals * 100))
#P4_Percent_SLA = '{0:.2f}'.format((p4_sla_met/p4_totals * 100))

with open (sla_file_path,'a', newline='') as sla_file:
  writablefile = csv.writer(sla_file) 
  now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  #print(now)
  lst=(now,P1_Percent_SLA,P2_Percent_SLA,P3_Percent_SLA,P4_Percent_SLA,val )
  #print(lst)
  writablefile.writerow(lst)
  sla_file.close()

print("P1 Tickets - ",p1_totals)
print("P2 Tickets - ",p2_totals)
print("P3 Tickets - ",p3_totals)
print("P4 Tickets - ",p4_totals)


print("The Percentage Of P1 Tickets That Met The SLA", P1_Percent_SLA)
print("The Percentage Of P2 Tickets That Met The SLA",P2_Percent_SLA)
print("The Percentage Of P3 Tickets That Met The SLA",P3_Percent_SLA)
print("The Percentage Of P4 Tickets That Met The SLA",P4_Percent_SLA)