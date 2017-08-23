#import schedule
import time

def job():
#    print "P1 read started..." + time.strftime("%Y-%m-%d %H:%M:%S")
    execfile("read_p1_telegram.py")
    execfile("process_p1_telegram.py") 
    execfile("sqlite_log.py")

while True:
    job()
    time.sleep(1)

