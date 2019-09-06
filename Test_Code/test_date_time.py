from datetime import datetime
from datetime import timedelta
#Add 1 day.
print("\n"+"this is 1 day from now")
print (datetime.now() + timedelta(days=1))
#Subtract 60 seconds.
print("\n"+"this is 1 minute from now")
print (datetime.now() - timedelta(seconds=60))
#add 8 hours
print("\n"+"this is 8 hours from now")
print (datetime.now() + timedelta(hours=8))
#Add 2 years.
print("\n"+"this is 2 years from now")
print (datetime.now() + timedelta(days=730))
two = (datetime.now() + timedelta(days=730))
print("\n"+"testing a variable assignment")
print(two)