#!usr/bin/python2.7
import time
import datetime
import os
import sys
sys.path.insert(0,'/')
#this module only frames the name of the file with extensions that will contain
#the updated details on each day
def file_update(file_set):
    print(file_set)
    text_file=open("myfolder.txt","r")
    directory_set=text_file.read()

    text_file.close()


    #now=datetime.datetime.now().date().strftime ("%Y%m%d")
    #date_extension=str(now)
    #extension=".csv"

    #gathering the date of the current day

    file_name=directory_set+file_set
    #print(file_name) framing the name
    print(file_name)
    text_file=open("output.txt","w")
    #saving the name
    text_file.write("%s" % file_name)
    text_file.close()
