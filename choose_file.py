#!usr/bin/python2.7
# this code chooses multiple files from user through file explorer and writes the unque
#portion of the name of the file in a text file in a new line in each line
import sys
import string

sys.path.insert(0,'/') #for writing in a textfile from php

import tkinter,time,os.path
import tkinter.filedialog
import time
import datetime

root=tkinter.Tk()       # launching file explorer
root.withdraw()

text_file=open("myfolder.txt","r")  # reading the directory
directory_set=text_file.read()

text_file.close()
filenames=tkinter.filedialog.askopenfilenames(parent=root,initialdir=directory_set,title='Please select the required files(without date extensions)')
lst=list(filenames)     #splitting the files selected and saving them in a list

text_file=open("myfolder.txt","r")
directory_set=text_file.read()

text_file.close()
textfile=open("file_collection.txt","w")    #to Write in the text file
textfile.close()
now=datetime.datetime.now().date().strftime ("%Y%m%d") #form ->directory/'uniquename''date'.csv
date_extension=str(now)
length_folder=len(directory_set)
length_date_handle=len(date_extension)
length_date_handle=length_date_handle+4
extension=".csv"
for  i in lst:
    index_folder=i.find(directory_set)
    index_date=i.find(date_extension)
    str=i[index_folder+length_folder:index_date]        #writing the unique part in a text file
    str=str+date_extension+extension
    textfile=open("file_collection.txt","a")
    textfile.write("%s\n" % str)
    textfile.close()
