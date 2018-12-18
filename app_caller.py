#!usr/bin/python2.7

#the main launching program it is the main code that
#calls the whole stock_app_launch until all the files are covered

from stock_app_launch import  stock_app_launch
import  string
textfile=open("file_collection.txt","r")
while True:
  file_set=textfile.readline()
  if(""==file_set):
      break
  i=file_set.index(".csv")
  file=file_set[:i+4]

  print file
  stock_app_launch(file)

textfile.close()
