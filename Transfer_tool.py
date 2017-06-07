# A code to transfer the files (including the subfolder files / subfolder directory ) from one directory (source) to the
# other directory (destination).
# Once initiated, this code would run on 1st of every month at 10:00 automatically in the background.

from datetime import datetime
from datetime import date
from threading import Timer
import os
import shutil
import re


src = "C:\\Users\Manjunatha\Desktop\src" # source path
dst = "E:\dst"                           # destination path

# To copy the files from the directory (source)and also the files from the sub directory into the destination directory.
# Only the files in the subfolder, not the subfolder.
def copytree1():
    for root, dirs, files in os.walk(src):
        for file in files:
            path_file = os.path.join(root,file)
            m = re.search("([0-9]{2}\-[0-9]{2}\-[0-9]{4})", path_file)
            if(m):
                if(m.group(0)>="09-02-2014" and m.group(0)<="31-31-2014"):
                    shutil.copy2(path_file,dst)

def transfertool():
    x=datetime.today()
    y=x.replace(month=x.month+1, day=1, hour=10, minute=0, second=0, microsecond=0) #1st of every month
    delta_t=y-x
    secs=delta_t.seconds+1
    t = Timer(secs, transfertool).start()
    
    copytree2() # one can also call another fuction "copytree1" according to the requirement

    print ("This code would run again on ",y)

# To copy the the files and also the folders from source directory into the destination directory.
def copytree2(symlinks=False, ignore=None):
    m = date(2014,2,10)
    print (m)
    n = date(2015,10,1)
    print (n)
    for item in os.listdir(src):
        source = os.path.join(src, item)
        destination = os.path.join(dst, item)
        idate = re.search("([0-9]{2}\-[0-9]{2}\-[0-9]{4})", source)            # Search for the datestring of the format DD.MM.YYYY in the 
        l = idate.group(0)
        print (l)
        import datetime
        dt = datetime.datetime.strptime(l, "%d-%m-%Y").date()
        print (dt)
        if(dt):       
            print (idate)
            if(dt >= m and dt <= n):
                if os.path.isdir(source):
                    try:
                        shutil.copytree(source, destination, symlinks, ignore)
                    except:
                        pass
                else:
                    shutil.copy2(source, destination)

    
transfertool()




