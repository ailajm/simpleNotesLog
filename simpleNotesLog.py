#Daily notes log

#!/usr/bin/env python

#imports time module and creates timestamp variable
import time;
ts = time.time()
rts = time.ctime(ts)

#Gets user input
noteEntry = input("Enter notes here:")

#Opens log file and writes user input to file
log = open("path-to-log-file>>", "a+")
log.write("\n")
log.write(noteEntry)
log.write("\n")
log.write(str(rts))
log.close()

#Prints updated log file for user to review
log = open("<<path-to-log-file>>", "r")
print(log.read())
log.close()

#Closes window
input("Type 'exit' and press enter to close: \n")
