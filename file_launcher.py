#tkinter is python app development library(standard)
#it is available only for and above python 3.4  Version
from subprocess import call
import os
import sys
#.filedialog used to open the document dialogbox and openfile ocopies its address from user path



#creating the textfile for filename
#text_file = open("Output.txt", "w")
#text_file.close()
exitcode= call("python2 file_updater.py", shell=True)

#runs the file_updater code to save the current date fileName
#this filename contains that name which is uses to compare
text_file2 = open("output.txt", "r")
filename=text_file2.read()
text_file2.close()

if not os.path.isfile(filename):        #checking the presence
    print ("file not present")
    sys.exit()


#determining the last updated time of the file opened

time=os.path.getmtime(filename)

#keeping the trackrecord of the file update time

time_keep_file = open("time.txt", "w")
time_keep_file.write("%s" % time)
time_keep_file.close()



text_file2 = open("Output.txt", "r")
file_name=text_file2.read()
text_file2.close()
#print(filename)
print(file_name)
if filename == file_name:
    #print("gjgk")
    count=1
else:
    #print("sgjgsajd")
    count=0

#determining whether the file is opened for 1st time or it was previously used

count_keep_file = open("count.txt", "w")
count_keep_file.write("%s" % count)
count_keep_file.close()


text_file = open("Output.txt", "w")
text_file.write("%s" % filename)
text_file.close()
