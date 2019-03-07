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

def install_script():
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

def automatic():
    os.system("clear")
    print(colored("[+] ","green")+colored("Welcome To Automatic Wifi Hack","blue"))
    wifi = input(colored("Name Of Wifi To Hack(SSID): ","yellow"))
    print(colored("[+] ","green")+colored("You Want To Hack","blue")+colored("{}".format(wifi),"yellow"))
    print(colored("[INFO] ","yellow")+colored("Now Starting Enabling Mode","blue"))
    

#all functions here

#call function
root_check()
#call function