import time
from datetime import datetime as dt

# Target file
hosts_temp = "hosts"
# Target file's actual path
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
# Websites you want to block
website_block_list = ["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]

#Time Automation
while True:
    timeBottom = dt(dt.now().year,dt.now().month,dt.now().day,8)
    timeUpper = dt(dt.now().year,dt.now().month,dt.now().day,16)

    if timeBottom < timeUpper:
        print("Working hours...", timeUpper)

        #Opening File
        with open(hosts_temp,'r+') as file:
            content = file.read()
            
            #Checking if blocked websites list exists in the file or not
            for website in website_block_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website)
    else:
        with open(hosts_temp,'r+') as file:
            content = file.readlines()
            file.seek(0) 
            for line in content:
                if not any(website in line for website in website_block_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)