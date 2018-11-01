import tkinter,time,os.path
import tkinter.filedialog


#root is a self allocated tkinter variable that gets the address from user
#this code will run only once and create the two files for two filenames
#it will run only once to set the directory containg the file

root=tkinter.Tk()
root.withdraw()

print("Select the destination directory")
print(" PS:go inside it then select open")

filename=tkinter.filedialog.askdirectory(parent=root,initialdir="/home",title='Please select a destination directory')
text_file=open("myfolder.txt","w")
text_file.write("%s" % filename)
text_file.close()

text_file2=open("Output.txt","w")# Output->previous filename
text_file2.close()

text_file2=open("count.txt","w")# Output->previous filename
text_file2.close()

text_file2=open("output.txt","w")#output->new filename
text_file2.close()
