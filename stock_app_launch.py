#this is a caller module for the original database_upload function parameterized call

#the count detects whether the file is opened for the first time or  its is just a synchronization call
#ie the called file is new

#the time detects  whether the last updated time for the .csv is  the same or it is later updated

#if the file is updated in the same date then database is updated if not left as it is
#compiler-python 2.7.15

#we use .txt files to just remember the values parmanentky through function calls

from database_upload_func  import database_upload
from subprocess import call
import os.path
import sys
exitcode= call("python3 file_launcher.py", shell=True)

#reading count to be passed in function

count_keep_file = open("count.txt", "r")
count=count_keep_file.read()
count_keep_file.close()
#print(count)
#reading filename to be opened to be passed  in function

text_file = open("Output.txt", "r")
file_name=text_file.read()
text_file.close()

#reading time updated to be passed in function
time_keep_file = open("time.txt", "r")

time=time_keep_file.read()
time_keep_file.close()
#print(time)
#to call database_upload original function

database_upload(count,time)
