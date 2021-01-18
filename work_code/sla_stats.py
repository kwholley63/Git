import csv
import datetime
import operator
from datetime import date, timedelta
#from datetime import datetime, timedelta
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
p1_sla_met = 1
p1_sla_miss = 1
p2_sla_met = 1
p2_sla_miss = 1
p3_sla_met = 1
p3_sla_miss = 1
p4_sla_met = 1
p4_sla_miss = 1

p1_totals = 1
p2_totals = 1
p3_totals = 1
p4_totals = 1


opened_yesterday = 0
resolved_yesterday = 0
ticket_list = []

"""

If the field resolved= str(row[17]) is blank I populate it "1/01/2050 2:58"
This is to prevent the date calculation from failing on a blank field. This 
will marginally inflate the met SLA statistics at the start of the month


We have commented out any P1 calculation. These are not real P1 ticket but more elevated
P2 tickets. They were called P1 in thr original HPSM > SNOW mapping of tickets.
The code will be adjusted to change these to P2

"""

snow_file_path = "K:\\snow_file.csv"
#snow_file1_path = "K:\\snow_file1_new.csv"
 
#dump_file_path = "K:\\dump_file.csv"
#daily_stats_file_path = "K:\\daily_stats.csv"
#totals_file_path = "K:\\totals_file.csv"
sla_file_path = "K:\\sla_file.csv"
sla_file_details_path = "K:\\sla_file_details.csv"

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
######

def cleanup():
  print("Cleaup old Files")
  if os.path.isfile(sla_file_details_path):
    os.remove(sla_file_details_path)
  else:
    print("file not found. Extract needs to be completed", dump_file_path)
    sys.exit(1)
cleanup()

######

def Ticket_SLA():
  print("calling ticket SLA")
   

 

Ticket_SLA()
print("ticket SLA")

with open (snow_file_path,'r') as snow_file:
    with open (sla_file_details_path,'a', newline='') as sla_file_details:
        readablefile = csv.reader(snow_file)
        writablefile = csv.writer(sla_file_details) 
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
            
            #print("here")
            if row[6] == "2 - Medium" and row[7] == "2 - High":
              P2= P2 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              #print(resolved)
              if resolved == "":
                resolved = "1/01/2050 2:58"
                #print("the resolve time was blank. it was set to >", resolved)
                #sys.exit()
              else:
                print("" )
              resolve_format = (str(resolved))
              #print(resolve_format)
              resolve_time = (str(resolve_format))
              #print(resolve_time)
              breach_time = (str(date_format + timedelta(hours=8)))
              #print("the orig resolve time is " ,ticket, resolve_time)
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%d/%Y %H:%M")
              resolve_time = datetime.strptime(resolve_time, '%m/%d/%Y %H:%M')
              new_resolve_time = datetime.strftime(resolve_time, '%#m/%d/%Y %H:%M')
              #print("the orig resolve time is " , resolve_time)
              #print("The new resolved time is", new_resolve_time)
              #print("the new breached time is", new_breach_time)
              #sys.exit()
              if new_resolve_time < new_breach_time:
                p2_sla_met = p2_sla_met +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P2 MADE SLA" )
                writablefile.writerow(lst)
                #print("SLA MADE", P2)
                #sys.exit()
              else:
                p2_sla_miss = p2_sla_miss +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P2 MISSED SLA" )
                writablefile.writerow(lst)
                #print("SLA MISSED", P2)

            elif row[6] == "2 - Medium" and row[7] == "4 - Low":
              P2= P2 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              #print(resolved)
              if resolved == "":
                resolved = "1/01/2050 2:58"
                #print("the resolve time was blank. it was set to >", resolved)
                #sys.exit()
              else:
                print("" )
              resolve_format = (str(resolved))
              #print(resolve_format)
              resolve_time = (str(resolve_format))
              #print(resolve_time)
              breach_time = (str(date_format + timedelta(hours=8)))
              #print("the orig resolve time is " ,ticket, resolve_time)
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%d/%Y %H:%M")
              resolve_time = datetime.strptime(resolve_time, '%m/%d/%Y %H:%M')
              new_resolve_time = datetime.strftime(resolve_time, '%#m/%d/%Y %H:%M')
              #print("The ticket is",ticket)
              #print("the orig resolve time is " , resolve_time)
              #print("The new resolved time is", new_resolve_time)
              #print("the new breached time is", new_breach_time)
              #sys.exit()
              if new_resolve_time < new_breach_time:
                p2_sla_met = p2_sla_met +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P2 MADE SLA" )
                writablefile.writerow(lst)
                #print("SLA MADE", P2)
                #sys.exit()
              else:
                p2_sla_miss = p2_sla_miss +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P2 MISSED SLA" )
                writablefile.writerow(lst)
                #print("SLA MISSED", P2)
               
            elif row[6] == "2 - Medium" and row[7] == "3 - Moderate":
              P2= P2 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              #print(resolved)
              if resolved == "":
                resolved = "1/01/2050 2:58"
                #print("the resolve time was blank. it was set to >", resolved)
                #sys.exit()
              else:
                print("" )
              resolve_format = (str(resolved))
              #print(resolve_format)
              resolve_time = (str(resolve_format))
              #print(resolve_time)
              breach_time = (str(date_format + timedelta(hours=8)))
              #print("the orig resolve time is " ,ticket, resolve_time)
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%d/%Y %H:%M")
              resolve_time = datetime.strptime(resolve_time, '%m/%d/%Y %H:%M')
              new_resolve_time = datetime.strftime(resolve_time, '%#m/%d/%Y %H:%M')
              #print("the orig resolve time is " , resolve_time)
              #print("The new resolved time is", new_resolve_time)
              #print("the new breached time is", new_breach_time)
              #sys.exit()
              if new_resolve_time < new_breach_time:
                p2_sla_met = p2_sla_met +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P2 MADE SLA" )
                writablefile.writerow(lst)
                #print("SLA MADE", P2)
                #sys.exit()
              else:
                p2_sla_miss = p2_sla_miss +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P2 MISSED SLA" )
                writablefile.writerow(lst)
                #print("SLA MISSED", P2)
                
               
            elif row[6] == "1 - High" and row[7] == "2 - High":
              P1= P1 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              #print(resolved)
              if resolved == "":
                resolved = "1/01/2050 2:58"
                #print("the resolve time was blank. it was set to >", resolved)
                #sys.exit()
              else:
                print("" )
              resolve_format = (str(resolved))
              #print(resolve_format)
              resolve_time = (str(resolve_format))
              #print(resolve_time)
              breach_time = (str(date_format + timedelta(hours=8)))
              #print("the orig resolve time is " ,ticket, resolve_time)
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%d/%Y %H:%M")
              resolve_time = datetime.strptime(resolve_time, '%m/%d/%Y %H:%M')
              new_resolve_time = datetime.strftime(resolve_time, '%#m/%d/%Y %H:%M')
              #print("the orig resolve time is " , resolve_time)
              #print("The new resolved time is", new_resolve_time)
              #print("the new breached time is", new_breach_time)
              #sys.exit()
              if new_resolve_time < new_breach_time:
                p1_sla_met = p1_sla_met +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P1 MADE SLA" )
                writablefile.writerow(lst)
                #print("SLA MADE", P1)
                #sys.exit()
              else:
                p1_sla_miss = p1_sla_miss +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P1 MISSED SLA" )
                writablefile.writerow(lst)
                #print("SLA MISSED", P1)
               
            elif row[6] == "1 - High" and row[7] == "3 - Moderate":
              P1= P1 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              #print(resolved)
              if resolved == "":
                resolved = "1/01/2050 2:58"
                #print("the resolve time was blank. it was set to >", resolved)
                #sys.exit()
              else:
                print("" )
              resolve_format = (str(resolved))
              #print(resolve_format)
              resolve_time = (str(resolve_format))
              #print(resolve_time)
              breach_time = (str(date_format + timedelta(hours=8)))
              #print("the orig resolve time is " ,ticket, resolve_time)
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%d/%Y %H:%M")
              resolve_time = datetime.strptime(resolve_time, '%m/%d/%Y %H:%M')
              new_resolve_time = datetime.strftime(resolve_time, '%#m/%d/%Y %H:%M')
              #print("the orig resolve time is " , resolve_time)
              #print("The new resolved time is", new_resolve_time)
              #print("the new breached time is", new_breach_time)
              #sys.exit()
              if new_resolve_time < new_breach_time:
                p1_sla_met = p1_sla_met +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P1 MADE SLA" )
                writablefile.writerow(lst)
                print("SLA MADE", P2)
                #sys.exit()
              else:
                p2_sla_miss = p2_sla_miss +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P1 MISSED SLA" )
                writablefile.writerow(lst)
                #print("SLA MISSED", P2)               
               
            elif row[6] == "3 - Low" and row[7] == "3 - Moderate":
              P3= P3 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              #print(resolved)
              if resolved == "":
                resolved = "1/01/2050 2:58"
                print("the resolve time was blank. it was set to >", resolved)
                #sys.exit()
              else:
                print("" )
              resolve_format = (str(resolved))
              #print(resolve_format)
              resolve_time = (str(resolve_format))
              #print(resolve_time)
              breach_time = (str(date_format + timedelta(hours=24)))
              #print("the orig resolve time is " ,ticket, resolve_time)
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%d/%Y %H:%M")
              resolve_time = datetime.strptime(resolve_time, '%m/%d/%Y %H:%M')
              new_resolve_time = datetime.strftime(resolve_time, '%#m/%d/%Y %H:%M')
              #print("the orig resolve time is " , resolve_time)
              #print("The new resolved time is", new_resolve_time)
              #print("the new breached time is", new_breach_time)
              #sys.exit()
              if new_resolve_time < new_breach_time:
                p3_sla_met = p3_sla_met +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P3 MADE SLA" )
                writablefile.writerow(lst)
                #print("SLA MADE", P3)
                #sys.exit()
              else:
                p3_sla_miss = p3_sla_miss +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P3 MISSED SLA" )
                writablefile.writerow(lst)
                #print("SLA MISSED", P3)
               
            elif row[6] == "3 - Low" and row[7] == "4 - Low":
              P3= P3 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              #print(resolved)
              if resolved == "":
                resolved = "1/01/2050 2:58"
                #print("the resolve time was blank. it was set to >", resolved)
                #sys.exit()
              else:
                print("" )
              resolve_format = (str(resolved))
              #print(resolve_format)
              resolve_time = (str(resolve_format))
              #print(resolve_time)
              breach_time = (str(date_format + timedelta(hours=24)))
              #print("the orig resolve time is " ,ticket, resolve_time)
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%d/%Y %H:%M")
              resolve_time = datetime.strptime(resolve_time, '%m/%d/%Y %H:%M')
              new_resolve_time = datetime.strftime(resolve_time, '%#m/%d/%Y %H:%M')
              #print("the orig resolve time is " , resolve_time)
              #print("The new resolved time is", new_resolve_time)
              #print("the new breached time is", new_breach_time)
              #sys.exit()
              if new_resolve_time < new_breach_time:
                p3_sla_met = p3_sla_met +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P3 MADE SLA" )
                writablefile.writerow(lst)
                #print("SLA MADE", P3)
                #sys.exit()
              else:
                p3_sla_miss = p3_sla_miss +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P3 MISSED SLA" )
                writablefile.writerow(lst)
                #print("SLA MISSED", P3)

            elif row[6] == "3 - Low" and row[7] == "5 - Very Low":
              P4= P4 +1
              ticket = str(row[0])
              hpsm_ticket = str(row[1])
              assigned = str(row[5])
              impact = str(row[6])
              priority = str(row[7])
              created = str(row[12])
              resolved= str(row[17])
              #print(resolved)
              if resolved == "":
                resolved = "1/01/2050 2:58"
                #print("the resolve time was blank. it was set to >", resolved)
                #sys.exit()
              else:
                print("" )
              resolve_format = (str(resolved))
              #print(resolve_format)
              resolve_time = (str(resolve_format))
              #print(resolve_time)
              breach_time = (str(date_format + timedelta(hours=120)))
              #print("the orig resolve time is " ,ticket, resolve_time)
              new_breach_time = datetime.strptime(breach_time, '%Y-%m-%d %H:%M:%S').strftime("%#m/%d/%Y %H:%M")
              resolve_time = datetime.strptime(resolve_time, '%m/%d/%Y %H:%M')
              new_resolve_time = datetime.strftime(resolve_time, '%#m/%d/%Y %H:%M')
              #print("the orig resolve time is " , resolve_time)
              #print("The new resolved time is", new_resolve_time)
              #print("the new breached time is", new_breach_time)
              #sys.exit()
              if new_resolve_time < new_breach_time:
                p4_sla_met = p4_sla_met +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P4 MADE SLA" )
                writablefile.writerow(lst)
                #print("SLA MADE", P3)
                #sys.exit()
              else:
                p4_sla_miss = p4_sla_miss +1
                lst=(ticket,assigned,impact,priority,created,resolve_time,new_breach_time,"P4 MISSED SLA" )
                writablefile.writerow(lst)
                #print("SLA MISSED", P3)

#p1_totals = (p1_sla_met + p1_sla_miss)
p2_totals = (p2_sla_met + p2_sla_miss)
p3_totals = (p3_sla_met + p3_sla_miss)
p4_totals = (p4_sla_met + p4_sla_miss)

#print("p1 sla met" , p1_sla_met)
#print("p1 sla miss", p1_sla_miss)
print("p2 sla met",  p2_sla_met)
print("p2 sla miss", p2_sla_miss)
print("p3 sla met", p3_sla_met)
print("p3 sla miss", p3_sla_miss)
print("p4 sla met" , p4_sla_met)
print("p4 sla miss", p4_sla_miss)

#P1_Percent_SLA = '{0:.2f}'.format((p1_sla_met/p1_totals * 100))
P2_Percent_SLA = '{0:.2f}'.format((p2_sla_met/p2_totals * 100))
P3_Percent_SLA = '{0:.2f}'.format((p3_sla_met/p3_totals * 100))
P4_Percent_SLA = '{0:.2f}'.format((p4_sla_met/p4_totals * 100))

 
 
with open (sla_file_path,'a', newline='') as sla_file:
  writablefile = csv.writer(sla_file) 
  now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  #print(now)
  #lst=(now,P2_Percent_SLA,P3_Percent_SLA,val )
  lst=(now,P2_Percent_SLA,P3_Percent_SLA,P4_Percent_SLA,val )
  #print(lst)
  writablefile.writerow(lst)
  sla_file.close()

sla_file_details.close()
#print("P1 Tickets - ",p1_totals)
print("P2 Tickets - ",p2_totals)
print("P3 Tickets - ",p3_totals)
print("P4 Tickets - ",p4_totals)


#print("The Percentage Of P1 Tickets That Met The SLA", P1_Percent_SLA)
print("The Percentage Of P2 Tickets That Met The SLA",P2_Percent_SLA)
print("The Percentage Of P3 Tickets That Met The SLA",P3_Percent_SLA)
print("The Percentage Of P4 Tickets That Met The SLA",P4_Percent_SLA)
#added 1/18/2021
