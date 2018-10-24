from xlrd import open_workbook
import csv
import os
import webbrowser

file=raw_input("enter the name of the file you want to  open")
wb=open_workbook(file)
fileDir, fileName = os.path.split(file)
nameOnly = os.path.splitext(fileName)
newName = nameOnly[0] + ".csv"
outCSV = os.path.join(fileDir, newName)
your_csv=open(outCSV,'wb')
webbrowser.open(file)
print outCSV
for i in range(0,wb.nsheets):
    sheet=wb.sheet_by_index(i)
    print sheet.name
    wr = csv.writer(your_csv, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sheet.nrows):
       wr.writerow(sheet.row_values(rownum))
your_csv.close()
webbrowser.open(outCSV)
