#tkinter is python app development library(standard)
#it is available only for and above python 3.4  Version

#.filedialog used to open the document dialogbox and openfile ocopies its address from user path

import tkinter,time,os.path
from tkinter.filedialog import askopenfilename

#root is a self allocated tkinter variable that gets the address from user

root=tkinter.Tk()
root.withdraw()


filename=askopenfilename()

#creating the textfile for filename
text_file = open("Output.txt", "w")
text_file.close()

#determining the last updated time of the file opened

time=os.path.getmtime(filename)

#keeping the trackrecord of the file update time

time_keep_file = open("time.txt", "w")
time_keep_file.write("%s" % time)
time_keep_file.close()



text_file = open("Output.txt", "r")
file_name=text_file.read()
text_file.close()
if filename==file_name:
    count+=1
else:
    count=0

#determining whether the file is opened for 1st time or it was previously used

count_keep_file = open("count.txt", "w")
count_keep_file.write("%s" % count)
count_keep_file.close()


text_file = open("Output.txt", "w")
text_file.write("%s" % filename)
text_file.close()
