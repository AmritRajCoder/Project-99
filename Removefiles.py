import os
import time
import shutil
path = input("Enter address of folder to be cleaned: ")
days = int(input("Enter days:"))
min_time = days*24*60*60

if os.path.exists(path):
   lst =os.listdir(path)
   for item in lst:
      item_path = os.path.join(path, item)
      ctime = os.stat(item_path).st_ctime
      if (time.time()-ctime)>min_time:
         if "." in item:
            os.remove(item_path)
         else:
            shutil.rmtree(item_path)
else:
   print("Directory not found!")

