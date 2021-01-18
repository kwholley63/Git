from datetime import datetime
import csv
import os
import sys

task_file_path = "K:\\task_file.csv"
task_data_path = "K:\\task_data.csv"

def cleanup():
  print("Cleaup old Files")
  if os.path.isfile(task_data_path):
    os.remove(task_data_path)
  
cleanup()


with open (task_file_path,'r') as task_file:
    with open (task_data_path,'a', newline='') as task_data:
        readablefile = csv.reader(task_file)
        writablefile = csv.writer(task_data) 
        task_data.write("number, inc_num, state, assigned, closed_by, created_time, closed_time, Time To Complete"+"\n") 
        for row in readablefile:
            print("\n")
            break
        for row in readablefile:
          ##
          for row in readablefile:
            number = str(row[0])
            state = str(row[2])
            assigned = str(row[4])
            inc_num = str(row[5])
            closed_time = str(row[7])
            closed_by = str(row[8])
            created_time = str(row[9])
            
            """
            x = created.split("/")
            index = x[0]
            date_format = datetime.strptime(row[12], '%m/%d/%Y %H:%M')

            datetime.datetime.strptime("21/12/2008", "%d/%m/%Y").strftime("%Y-%m-%d")
            """
            
            time = created_time
            time1 = closed_time
            time_start  = datetime.strptime(time, '%m/%d/%Y %H:%M')
            time_end =  datetime.strptime(time1, '%m/%d/%Y %H:%M')
            diff = (time_end - time_start)
            print(time_end - time_start)
            print(created_time ,  closed_time , diff)

            lst=(number, inc_num, state, assigned, closed_by, created_time, closed_time, diff)
            writablefile.writerow(lst)
            
            #print(number, state, assigned, inc_num, closed_by , created_time, closed_time,  )
#added 1/18/2021
