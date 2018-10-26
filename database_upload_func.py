#!bin/python2.7
import MySQLdb, csv, sys
import os
import os.path,time
from subprocess import call

import mysql.connector
import datetime
def database_up(count,time):

    conn=mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="excel_project"
    )
    mycursor = mydb.cursor()
    #print(conn)
    if count==0:
        exitcode= call("python3 file_launcher.py", shell=True)
        text_file = open("Output.txt", "r")
        file_name=text_file.read()
        text_file.close()
        now=datetime.datetime.now().date().strftime ("%Y-%m-%d")
        #time_now=datetime.datetime.now().time()
        #print(file_name)
        

        if not file_name.endswith('.csv'):
            if not file_name.endswith('.txt'):
                print("Please enter correct file type")
                sys.exit()
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                line_count+=1
                if line_count>=1:
                    sql="INSERT INTO STOCK_DETAILS(Date_update) VALUES (%s)"
                    val=(now)
                    mycursor.execute(sql,val)
                    conn.commit()
                    sql="INSERT INTO STOCK_DETAILS(Scrip,sector,ACTION,status,EntryPrice,EntryDate,StopLoss,ExitPrice,ExitDate,LTP,LastTradingDay,Group) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (row[Scrip],row[sector],row[ACTION],row[status],row[EntryPrice],row[EntryDate],row[StopLoss],row[ExitPrice],row[ExitDate],row[LTP],row[LastTradingDay],row[Group])
                    mycursor.execute(sql,val)
                    conn.commit()
    else:
        modify_time=os.path.getmtime(file_name)
        if modify_time!=time:
            sql_del = "DELETE * FROM STOCK_DETAILS"
            mycursor.execute(sql_del)
            conn.commit()
            with open(file_name) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    line_count+=1
                    if line_count>=1:
                        sql="INSERT INTO STOCK_DETAILS VALUES(Scrip,sector,ACTION,status,EntryPrice,EntryDate,StopLoss,ExitPrice,ExitDate,LTP,LastTradingDay,Group) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        val = (row[Scrip],row[sector],row[ACTION],row[status],row[EntryPrice],row[EntryDate],row[StopLoss],row[ExitPrice],row[ExitDate],row[LTP],row[LastTradingDay],row[Group])
                        mycursor.execute(sql,val)
                        conn.commit()
