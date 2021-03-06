try:
    import Tkinter as tk
except:
    import tkinter as tk
from os import times
import re
import logging
from datetime import datetime


version = '1.3 [BETA 3]'

path = '/Users/vincenzodeluca/Library/Application Support/minecraft/logs/latest.log' # please edit /Users/vincenzodeluca/Library/...
#and replace vincenzodeluca whit your user, info: https://github.com/Vincenzo160/project-landscape/wiki/Setting-the-path

print ("Version: " + version)
print ("Project landscape")
print ("/!\ ATTENTION /!\ ")
print ("If your client don't save the log in the minecraft folder this program won't function")

root = tk.Tk()
root.geometry("500x500")
root.title('Project Landscape')
root.resizable(False, False)
root.iconbitmap()

def close_window():
    root.destroy()

def slog():
    logging.basicConfig(filename="GEXP.log", level=logging.INFO)
    print("")
    print("Saving..")
    now = datetime.now()
    current_time = now.strftime("%Y %M %D %H:%M:%S")
    print(current_time)
    logging.info(current_time)
    sum = 0
    for s in matching_lines:
        m = re.search("earned (\\d+) GEXP", s)
        sum = sum + int(m.group(1))
        logging.info(m.group(1))
    logging.info("Total GEXP Earned = {}".format(sum))
    print("GEXP.log Saved Succesfully in your user root")    

pattern = 'You earned'
matching_lines = [line for line in open(path).readlines() if pattern in line] 
sum = 0
for s in matching_lines:
    m = re.search("earned (\\d+) GEXP", s)
    sum = sum + int(m.group(1))
    print(m.group(1))
total = ("Total GEXP Earned = {}".format(sum))
total = tk.Label(text="Total GEXP Earned: {}".format(sum), width=50, height=5)
list = tk.Label(text="Last amount of GEXP: " + m.group(1), width=50, height=5)


version = tk.Label(text="Landscape Version: " + version)
changept = tk.Button(text = "Quit", command = close_window)
saveto = tk.Button(text = "Save To File", command = slog)

version.pack()
list.pack()
total.pack()


#fetchr = tk.Button(text = "Refresh", command = fetch)
#fetchr.pack()

button = tk.Button(text = "Quit", command = exit)
button.pack(side=tk.BOTTOM)
saveto.pack(side=tk.BOTTOM)

root.mainloop()

