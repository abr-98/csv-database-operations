#!usr/bin/python2.7
#This is the main moddule of the program
#it defines a function that controls the full database uploading module
#it uploads the data for first time opening of a file
#it later on updates the data if csv document modified time stamp is changed

##UPDATE-> Columns are not fixed any table can be enetered with the fields in 'total' list
#the table must have the table headers
import MySQLdb, csv, sys
#the library for controlling the data used
sys.path.insert(0,'/')
import os
#os.system('attrib +H *.txt /S')
#os.system('attrib +H *.pyc /S')
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
    print(conn)
    now=datetime.datetime.now().date().strftime ("%d/%m/20%y")
    print(now)
    items=[]
    values=['','','','','','','','','','','']
    total=['Stock','Sector','Action','Status','Entry','DateOfEntry','S/L','Exit','DateOfExit','LastTradingDay','P/L']
    #saving the current date in format

    if count == '0':        #new Entry

        #calling the python3 file launcher module

        #exitcode= call("python3 file_launcher.py", shell=True)
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


#updatinh the updated value after updating database
                if line_count==0:
                    items=row
                    #print (row)
                line_count+=1
                if line_count==1:
                    break
            #print (items)
            #print (total)
            line_count=0
            for row in csv_reader:
#updatinh the updated value after updating database

                line_count+=1
                if line_count>=1:

                    for i in total:
                        #print i
                        for j in items:
                            #print(j)
                            if i==j:
                                #print(total.index(i))
                                values[total.index(i)]=row[items.index(j)]
                                break
                            else:
                                values[total.index(i)]='N/A'    #the values not in the table will be given 'N/A'

                    #mycursor.execute(sql,val)
                    #print(values[4])
                    LTP=float(values[4])+float(values[10])      #LTP=EntryPrice+Profit


                    str(LTP)
                    if values[2]=='Sold':
                        values[total.index(DateOfExit)]=now         #if sold Exit=LTP
                        values[total.index(Exit)]=LTP               #DateOfExit= present DATE
                        #str(EntryDate)
                    if values[2]=='Bought':
                        #print(now)
                        #print('a')
                        mycursor.execute('INSERT INTO STOCK_DETAILSS(Date_update,Scrip,sector,ACTION,status,EntryPrice,EntryDate,StopLoss,ExitPrice,ExitDate,LTP,LastTradingDay,Profit) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'% (now,values[0],values[1],values[2],values[3],values[4],now,values[6],values[7],values[8],LTP,values[9],values[10]))
                        #If bought EntryDate  is the present date
                        #val = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
                        conn.commit()


                    else:

                    #
                        #print(values[5])
                        mycursor.execute('INSERT INTO STOCK_DETAILSS(Date_update,Scrip,sector,ACTION,status,EntryPrice,EntryDate,StopLoss,ExitPrice,ExitDate,LTP,LastTradingDay,Profit) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'% (now,values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],LTP,values[9],values[10]))
                        #else collect from table
                    #val = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
                        conn.commit()

    else:                   #the file is in a synchronization call
        text_file = open("Output.txt", "r")
        fileName=text_file.read()
        text_file.close()
        if not fileName.endswith('.csv'):
            if not fileName.endswith('.txt'):
                print("Please enter correct file type")
                sys.exit()
        modify_time=os.path.getmtime(fileName)

        if modify_time!= time:
            #checking whether the time stamp had changed

            mycursor.execute('DELETE FROM STOCK_DETAILSS where Date_update ="%s"' % now)
            conn.commit()
            time_keep_file = open("time.txt", "w")
            time_keep_file.write("%s" % modify_time)
            time_keep_file.close()


            with open(fileName) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                if '\0' in open(fileName).read():
                    print "you have null bytes in your input file.Exiting..."
                    sys.exit()
                else:

                    for row in csv_reader:
                        if line_count==0:
                            items=row
                            #print (row)
                        line_count+=1
                        if line_count==1:
                            break
                    #print (items)
                    #print (total)
                    line_count=0
                    for row in csv_reader:
#updatinh the updated value after updating database

                        line_count+=1
                        if line_count>=1:

                            for i in total:
                                #print i
                                for j in items:
                                    #print(j)
                                    if i==j:
                                        #print(total.index(i))
                                        values[total.index(i)]=row[items.index(j)]
                                        break
                                    else:
                                        values[total.index(i)]='N/A'

                            #mycursor.execute(sql,val)
                            #print(values[4])
                            LTP=float(values[4])+float(values[10])


                            str(LTP)
                            if values[2]=='Bought':
                                #print(now)
                                #print('a')
                                mycursor.execute('INSERT INTO STOCK_DETAILSS(Date_update,Scrip,sector,ACTION,status,EntryPrice,EntryDate,StopLoss,ExitPrice,ExitDate,LTP,LastTradingDay,Profit) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'% (now,values[0],values[1],values[2],values[3],values[4],now,values[6],values[7],values[8],LTP,values[9],values[10]))

                                #val = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
                                conn.commit()


                            else:

                            #    EntryDate=values[5]

                            #str(EntryDate)
                                #print(values[5])
                                mycursor.execute('INSERT INTO STOCK_DETAILSS(Date_update,Scrip,sector,ACTION,status,EntryPrice,EntryDate,StopLoss,ExitPrice,ExitDate,LTP,LastTradingDay,Profit) VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'% (now,values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],LTP,values[9],values[10]))

                            #val = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
                                conn.commit()

    conn.close()
#def main():
##    print ("hi")
#if __name__ == '__main__':
#    main()
