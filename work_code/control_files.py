#History
import shutil
import datetime
import os
import getpass
#import re
#
# Check for access 
sid = input("\n\n enter your sid"+"\t")
#
# Test for valid sid against the app_control_file
#
if sid in open('C:\\Users\\kwhol\\my_python_code\\app_control_file.txt').read():
    print("\n\n\n"+"This is a valid sid"+"\n\n\n")
else:
    print("Invalid sid. Access denied")
    exit(1)
#
now = datetime.datetime.now()
timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
#
def twp():
    #
    # Trap the file name without the path to write to the audit log.
    #
    filename = "C:\\Users\\kwhol\\my_python_code\\twp_pid_ctrl"
    file = (filename[30:45])
    #
    # get the user name in a variable, it will be written to the audit log to track who is making changes to the files
    #
    user_name = (getpass.getuser())
    #
    # ask for the pid input and check for the proper length, must be 6 numbers
    # if input is blank or input <6  or >6 program exits
    # check for length of change # hold at 10
    # check for length of change description hold at 50
    #
    print("\n")
    change = input("enter the change number >>>"+"\t")
    print("\n")
    change_desc = input("enter a change description >>>"+"\t")
    print("\n")
    change_desc = change_desc[0:50]
    pid = input("enter the pid >>>"+"\t")
    #print(change)
    pid_len=len(pid)
    if pid_len < 6 or pid_len > 6:
        print("\n")
        print ("incorrect pid, length must be 6 digits"+"\n")
        print("\n")
        exit()
    print("\n")    
    #
    # Before we write a new record we backup and timestamp a copy of the file
    print("backing up the control file"+"\t"+filename+"\n")     
    #
    shutil.copyfile('C:\\Users\\kwhol\\my_python_code\\twp_pid_ctrl','C:\\Users\\kwhol\\my_python_code\\twp_pid_ctrl.' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.log')
    #
    #Open the files needed; twp_pid_ctrl and audit.log
    #
    file_twp=open("C:\\Users\\kwhol\\my_python_code\\twp_pid_ctrl", "a+")
    file_audit=open("C:\\Users\\kwhol\\my_python_code\\audit.log", "a+")
    #write to the files
    file_twp.write(pid+"\n")
    #
    #write to the audit file. Left justify and move 20 spaces for the next entry
    #
    file_audit.write("{: <20} {: <20} {: <20} {: <20} {: <20}".format(pid,change,user_name,file,change_desc+"\n"))    
    file_twp.close()
    file_audit.close()
#
# After we make our changes we copy the file to .staged This will be the version 
# for a production install. 
#
    shutil.copyfile('C:\\Users\\kwhol\\my_python_code\\twp_pid_ctrl','C:\\Users\\kwhol\\my_python_code\\twp_pid_ctrl.staged')
#
def reqsubs():
    filename = "C:\\Users\\kwhol\\my_python_code\\requiredSubs_list"
    file = (filename[30:47])
    print(file)
    user_name = (getpass.getuser())
#print ("you are in the required Subs function")
#exit(1)
#
# pid is 6 digits
# days = days of the week 1 = sunday, 2 = monday 3 = tuesday, 4 = wednesday, 5 = Thursday, 6 = Friday, 7 = saturday
# start time is time of day to start looking for submissions at HH:MM
# end time is the time of day to stop looking for submissions 
# module name is the system the submission is processed on, * for all
# submission type A = authorization , D = Deposit, * = Both
# min subs is the minimum number of submissions in a time period
# max subs is the maximum number of submissions in a time period
#
    print("\n")
    change = input("enter the change number >>>"+"\t")
    print("\n")
    change_desc = input("enter a change description >>>"+"\t")
    print("\n")
    change_desc = change_desc[0:50]
    pid = input("enter the pid >>>"+"\t")
    #print(change)
    pid_len=len(pid)
    if pid_len < 6 or pid_len > 6:
        print("\n")
        print ("incorrect pid, length must be 6 digits"+"\n")
        print("\n")
        exit()
        print("\n")    
#
    days = input("enter the days of the week (example 1=sunday, 2=monday, 3=wednesday enter each number for days to run) >>>"+"\t")
    start_time = input("\n"+"enter the start time to start looking for submissions as HH:MM >>>"+"\t")
    end_time = input("\n"+"enter the end time to stop looking for submissions as HH:MM >>>"+"\t")
    system_name = input("\n"+"enter the system name for the submission >>>"+"\t")
    sub_type = input("\n"+"enter the submission type, A=Auth, D=Deposit, *=Both >>>"+"\t")
    min_subs = input("\n"+"enter the minimum number of submissions for the time period >>>"+"\t>")
    max_subs = input("\n"+"enter the maximum number of submissions for the time period >>>"+"\t>")    
# define our data dictionary with key = value pairs
####
####
# Before we write a new record we backup and timestamp a copy of the file
    print("backing up the control file"+"\t"+filename+"\n")     
#
    shutil.copyfile('C:\\Users\\kwhol\\my_python_code\\twp_pid_ctrl','C:\\Users\\kwhol\\my_python_code\\requiredSubs_list.' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + '.log')
#
#Open the files needed; twp_pid_ctrl and audit.log
#
    file_subs=open("C:\\Users\\kwhol\\my_python_code\\requiredSubs_list", "a+")
    file_audit=open("C:\\Users\\kwhol\\my_python_code\\audit.log", "a+")
#write to the files
    file_subs.write(pid+"|"+days+"|"+start_time+"|"+end_time+"|"+system_name+"|"+sub_type+"|"+min_subs+"|"+max_subs+"\n")
#
#write to the audit file. Left justify and move 20 spaces for the next entry
#
    #file_audit.write("{: <20} {: <20} {: <20} {: <20} {: <20} {: <20} {: <20} {: <20}".format(pid,days,start_time,end_time,system_name,sub_type,min_subs,max_subs+"\n"))    
    file_audit.write("{: <20} {: <20} {: <20} {: <20} {: <20}".format(pid,change,user_name,file,change_desc+"\n"))
    file_subs.close()
    file_audit.close()
####
option = {'1' : 'twp_pid_ctrl', '2' : 'required submissions', '3' : 'required jobs', '4' : 'required files', '5' : 'update access file'}
for key,value in option.items():
    print(key, "=", value)
    print("\n")
#
#
resp=input("Select the control file to update >>>")
if resp == "1":
    #print("twp_pid_ctrl"+"\n")
    #call the twp function
    twp()
    #exit
elif resp == "2":
    print("required submissions")
    reqsubs()
    #exit
else:
    print("invalid entry")