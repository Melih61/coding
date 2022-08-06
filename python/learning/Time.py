import time

print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                       epoch = when your computer thinks time began (reference point)

print(time.time()) # return current seconds since epoch

print(time.ctime(time.time())) # Current time

time_object = time.localtime() # Local time
time_opject = time.gmtime() # Coordinated Universal Time (UTC)
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object) # Format local time
print(local_time)

# Get the time of a string like 20 April 2020 -> 20.04.2020
time_string = "20 April, 2020"
time_object = time.strptime(time_string, '%d %B, %Y')
print(time_object)

#   (year, month, day, hours, minutes, secs #day of the week, #day of the year, dst)
# Get seconds till time tuple
time_tuple = (2014,8,23,4,20,0,0,0,0)
time_string = time.mktime(time_tuple)
print(time_string)