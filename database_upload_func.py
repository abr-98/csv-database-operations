#This is the main moddule of the program
#it defines a function that controls the full database uploading module
#it uploads the data for first time opening of a file
#it later on updates the data if csv document modified time stamp is changed

#!bin/python2.7
import MySQLdb, csv, sys
#the library for controlling the data used

import os
import os.path,time
from subprocess import call

import mysql.connector
import datetime
def database_upload(count,time):

#connecting database

    conn=mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="excel_project"
    )
    mycursor = mydb.cursor()
    #print(conn)
    now=datetime.datetime.now().date().strftime ("%Y-%m-%d")

    #saving the current date in format

    if count == '0':        #new Entry

        #calling the python3 file launcher module

        exitcode= call("python3 file_launcher.py", shell=True)
        text_file = open("Output.txt", "r")
        file_name=text_file.read()
        text_file.close()

        #time_now=datetime.datetime.now().time()
        #print(file_name)

        #checking Whether the input is of proper format

        if not file_name.endswith('.csv'):
            if not file_name.endswith('.txt'):
                print("Please enter correct file type")
                sys.exit()
        with open(file_name) as csv_file:

#here we read the data from csv and enter into database as row

            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                line_count+=1
                if line_count>=1:
                    #mycursor.execute("INSERT INTO STOCK_DETAILS(Date_update) VALUES (%s)"% now)        #entering the date in the database
                    #val=(now)
                    if row[4]=='sold':

                        ret=float(row[8])-float(row[5])
                    else:
                        ret=float(row[10])-float(row[5])

                    str(ret)

                    #mycursor.execute(sql,val)
                    conn.commit()
                    mycursor.execute('INSERT INTO STOCK_DETAILS(Date_update,Scrip,sector,ACTION,status,EntryPrice,EntryDate,StopLoss,ExitPrice,ExitDate,LTP,LastTradingDay,Profit) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'% (now,row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],ret))

                    #val = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
                    conn.commit()

                    #mycursor.execute("INSERT INTO STOCK_DETAILS(Profit) VALUES (%s)"% ret)
                    #val=(ret)
                    #mycursor.execute(sql,val)
                    #conn.commit()

    else:                   #the file is in a synchronization call
        text_file = open("Output.txt", "r")
        fileName=text_file.read()
        text_file.close()
        modify_time=os.path.getmtime(fileName)
        if modify_time!= time:
            #checking whether the time stamp had changed

            mycursor.execute("TRUNCATE TABLE STOCK_DETAILS")
            time_keep_file = open("time.txt", "w")
            time_keep_file.write("%s" % modify_time)
            time_keep_file.close()

            conn.commit()
            with open(fileName) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                if '\0' in open(fileName).read():
                    print "you have null bytes in your input file.Exiting..."
                    sys.exit()
                else:

                    for row in csv_reader:

#updatinh the updated value after updating database
                        line_count+=1
                        if line_count>=1:
                            if row[4]=='sold':

                                ret=float(row[8])-float(row[5])
                            else:
                                ret=float(row[10])-float(row[5])

                            str(ret)

                            #mycursor.execute(sql,val)
                            conn.commit()
                            mycursor.execute('INSERT INTO STOCK_DETAILS(Date_update,Scrip,sector,ACTION,status,EntryPrice,EntryDate,StopLoss,ExitPrice,ExitDate,LTP,LastTradingDay,Profit) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'% (now,row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],ret))

                            #val = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
                            conn.commit()
    conn.close()
