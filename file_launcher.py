import tkinter
from tkinter.filedialog import askopenfilename

root=tkinter.Tk()
root.withdraw()
filename=askopenfilename()
text_file = open("Output.txt", "w")
text_file.write("%s" % filename)
text_file.close()
