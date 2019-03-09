#!/usr/bin/python3

#This script is made to hack wpa/wpa2 wifi network automatically or manually if prefered

#Author: ReVibe


#all imports here
import os                       #manage terminal commands
from termcolor import colored   #prints colored text
import time                     #pause script
import getpass                  #get username
#all imports here

#all functions here
def root_check():  
    os.system("clear")                            #need root access for some functions to run properly
    user = getpass.getuser()
    print(colored("[INFO] ","yellow")+colored("Current User Is {}","green").format(user))
    if user != 'root':
        print(colored("[INFO] ","yellow")+colored("We Need root Access To Run Some Of The Functions","blue"))
        print(colored("[INFO] ","yellow")+colored("Please Run As Root","red"))
        quit()
    else:
        check_install()

def check_install():                              #check if lazyfi already installed
    directory = os.path.isdir("/bin/Lazyfi")
    if directory:
        os.system("clear")
        banner()
    else:
        os.system("clear")
        banner_install()    

def banner():                                     #start screen styles
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
        print(colored("[1] Automatic                    *","blue"))
        print(colored("[2] Manual                       *","blue"))
        print(colored("[3] Cleanup                      *","blue"))
        print(colored("[4] Uninstall                    *","blue"))
        print(colored("[5] Exit                         *","blue"))
        print(colored("**********************************","blue"))
        opt = input(colored(">> ","blue"))
        if opt == '1':
            automatic()
        elif opt == '2':
            print("manual")
        elif opt == '3':
            print("clean")
        elif opt == '4':
            quit()
        elif opt == '5':
            uninstall()
        else:
            print("not valid")

def banner_install():                             #start installing script 
        print(colored("**********************************","blue"))
        print(colored("*   _                     __ _   *","blue"))
        print(colored("*  | |    __ _ _____   _ / _(_)  *","blue"))
        print(colored("*  | |   / _` |_  / | | | |_| |  *","blue"))
        print(colored("*  | |__| (_| |/ /| |_| |  _| |  *","blue"))
        print(colored("*  |_____\__,_/___|\__, |_| |_|  *","blue"))
        print(colored("*                  |___/         *","blue"))
        print(colored("*                        v 2.0   *","blue"))
        print(colored("**********************************","blue"))
        print(colored("[1] Install                      *","blue"))
        print(colored("[2] Exit                         *","blue"))
        print(colored("**********************************","blue"))
        opt = input(colored(">> ","blue"))
        if opt == '1':
            install_script()
        elif opt == '2':
            os.system("clear")
            quit()
        else:
            os.system("clear")
            print(colored("[INFO] ","yellow")+colored("Please Type A Valid Option","red"))
            banner_install()

def install_script():                             #install the script if not installed
    os.system("clear")
    print(colored("[PROCESS] ","green")+colored("Making lazyfi Script","blue"))
    os.system("echo '#!/bin/bash' >> lazyfi")
    time.sleep(1)
    os.system("echo 'sudo python3 /bin/Lazyfi/Lazyfi.py' >> lazyfi")
    time.sleep(1)
    print(colored("[PROCESS] ","green")+colored("Making /bin/Lazyfi Folder","blue"))
    os.system("mkdir /bin/Lazyfi")
    time.sleep(1)
    print(colored("[PROCESS] ","green")+colored("Coping All Files To /bin/Lazyfi","blue"))
    os.system("cp Lazyfi.py /bin/Lazyfi")
    time.sleep(1)
    os.system("mv lazyfi /bin/Lazyfi")
    time.sleep(1)
    print(colored("[PROCESS] ","green")+colored("Fixing Permissions...","blue"))
    os.system("chmod +x /bin/Lazyfi/lazyfi")
    time.sleep(1)
    print(colored("[PROCESS] ","green")+colored("Adding Script To PATH","blue"))
    os.system("export PATH=$PATH:/bin/Lazyfi")
    time.sleep(1)
    os.system("echo 'export PATH=$PATH:/bin/Lazyfi' >> ~/.bashrc")
    time.sleep(1)
    #for users other than root
    os.system("locate .bashrc | grep home > bashrc.txt")
    location = open("bashrc.txt","+r")
    dirs = location.readline()
    os.system("echo 'export PATH=$PATH:/bin/Lazyfi' >> {}".format(dirs.rstrip()))
    time.sleep(1)
    os.system("rm bashrc.txt")
    print(colored("[PROCESS] ","green")+colored("All Done. Good To Go","blue"))
    time.sleep(2)
    banner()

#full automatic mode
def automatic():                               #full automatic mode no interactions
    global inte
    os.system("clear")
    print(colored("[+] ","green")+colored("Welcome To Automatic Wifi Hack","blue"))
    wifi = input(colored("[+] ","green")+colored("Name Of Wifi To Hack(SSID): ","yellow"))
    print(colored("[+] ","green")+colored("You Want To Hack","blue")+colored("{}".format(wifi),"yellow"))
    print(colored("[INFO] ","yellow")+colored("Checking Interface","blue"))
    os.system("ifconfig | grep -wl | cut -d ':' -f 1 > interface.txt")
    interface = open("interface.txt","+r")
    inte = interface.readlines()
    if not inte:
        print(colored("[X] ","red")+colored("No Interface Found Please Insert Your Wifi Adeptar!","red"))
        quit()
    else:
        print(colored("[+] ","green")+colored("Your Network Interface Is: "+inte[0].rstrip(),"green"))
        time.sleep(2)
        check_mon()
    #print(colored("[INFO] ","yellow")+colored("Now Starting Enabling Mode","blue"))

def check_mon():                                      #check for monitor mode which is required
    os.system("clear")
    os.system("rm interface.txt")
    os.system("iwconfig 2> /dev/null | grep Mode: | awk '{ print $4 }' | cut -d ':' -f 2 > check_mon.txt")
    modename = open("check_mon.txt","+r")
    mode = modename.readlines()
    if mode[0].rstrip() != "Monitor":
            print(colored("[x] ","red")+colored("Your Current Mode Is: Managed","red"))
            time.sleep(2)
            os.system("rm check_mon.txt")
            monitor_enable()
    else:
            print(colored("[+] ","green")+colored("Your Current Mode Is: " +str(mode[0].rstrip()),"green"))
            time.sleep(2)
            os.system("rm check_mon.txt")
            search()

def monitor_enable():                                 #enables monitor mode if not enabled
    global inte
    os.system("pgrep NetworkManager > netm.txt")
    os.system("pgrep wpa_supplicant > wpa.txt")
    os.system("pgrep dhclient > dhc.txt")
    time.sleep(1)
    netman = open("netm.txt","+r")
    wpacli = open("wpa.txt","+r")
    dhcli = open("dhc.txt","+r")
    net = netman.readlines()
    wpa = wpacli.readlines()
    dh = dhcli.readlines()
    if not net: #kill NetworkManger
        pass
    else:
        os.system("kill {}".format(net[0].rstrip()))
    if not wpa: #kill wpa-supllicant
        pass
    else:
        os.system("kill {}".format(wpa[0].rstrip()))
    if not dh: #kill dhclient
        pass
    else:
        os.system("kill {}".format(dh[0].rstrip()))
    time.sleep(2)
    os.system("airmon-ng start {}".format(inte[0].rstrip()))
    time.sleep(1)
    os.system("rm netm.txt")
    os.system("rm wpa.txt")
    os.system("rm dhc.txt")
    time.sleep(2)
    check_mon()

def search():
    pass
#full automatic mode    

def uninstall():
    pass



#all functions here

#call function
root_check()
#call function




###steps
# check interface (done)
# check for monitor mode (done)
# activate it (done)
# search for wifi
# deauth
# capture cap
# crack cap
#  ###
