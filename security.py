from datetime import datetime as dt 
import time

redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]
hosts_path=r"C:\windows\system32\drivers\etc\hosts"  #this is path for windows host file 
today=dt.now()
date1=dt(dt.now().year,dt.now().month,dt.now().day,8)
date2=dt(dt.now().year,dt.now().month,dt.now().day,19)
while True:
    #print(type(today))
    if (date1<dt.now()<date2):
        print("working hours",dt.now())
        with open(hosts_path,"r+")as file:
            content=file.read()
            for website in website_list:
                if(website in content):
                    pass
                else:
                    file.write(redirect+" "+website+ "\n")
    else:
        # print("Fun hours",dt.now())
        with open(hosts_path,"r+")as file:
            content=file.read()
            for website in website_list:
                if(website in content):
                    file.truncate(3)
                    pass
    time.sleep(1)
    