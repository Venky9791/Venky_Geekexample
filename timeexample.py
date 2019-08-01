import time
from time import perf_counter as mytimer
import random
import tkinter

print (tkinter.TkVersion)
print (tkinter.TclVersion)
mainwindow = tkinter.Tk()
mainwindow.title = "My First Example GUI"
mainwindow.geometry('640*640+8+400')
mainwindow.mainloop()
# input("Press enter to Start the timeer")
# waittime= random.randint(1,6)
# time.sleep(waittime)
# starttime = mytimer()
# endtime= input ("Press Enter to Stop the timer")
# endtime=mytimer()
#
#
# print("Started at"+time.strftime("%X",time.localtime(starttime)))
# print("Ended  at"+time.strftime("%X",time.localtime(endtime)))
# print ("Your Reaction time is {} seconds" .format(endtime-starttime))
