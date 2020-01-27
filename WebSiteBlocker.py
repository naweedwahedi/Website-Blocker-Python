import time
from datetime import datetime as dt

# hosts_path = r"C:\Windows\System32\drivers\Demo\hosts" = path for windows user
hosts_path= "/etc/hosts"    # Host file location
redirect="127.0.0.1"    #local host IP address
website_list=["www.facebook.com",
              "facebook.com",               
              "dub119.mail.live.com",
              "www.dub119.mail.live.com"
             ]      # Block this websites

while True: # while loop to run the programm every 5 seconds
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,
    dt.now().month,dt.now().day,12):    # Condation to run the program from 8AM to 4PM
        print("Working hours...")
        with open(hosts_path,'r+') as file: # Open file to read and append
            content=file.read() # Load the text in a variable
            for website in website_list:    # iteriate trugh the list
                if website in content:
                    pass        # if blocked websites are in the file pass
                else:
                    file.write(redirect+" "+ website+"\n")  #if blocked websites are not in the file add them
    else:   # Second condation for outside of working hours
        with open(hosts_path,'r+') as file:
            content=file.readlines()    # Load the text in a variable as a list of strings
            file.seek(0)    # Bring the pointer to the index 0
            for line in content:
                if not any(website in line for website in website_list): # Compare the website_list with host file
                    file.write(line)
            file.truncate() # Remove the old copy of text from host file
        print("Fun hours...")
    time.sleep(5)
