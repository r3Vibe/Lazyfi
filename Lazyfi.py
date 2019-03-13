#!/bin/python3
#Lazyfi 2.0

#imports here
import time
import os
from termcolor import colored
import getpass
import netifaces
from subprocess import check_output
from threading import Thread

#check for root access
def check_root():
    os.system("clear")
    username = getpass.getuser()
    if username != 'root':
        print(colored("please run as root",'red'))
        quit()
    else:
        print(colored("script has root access","green"))
        time.sleep(2)
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
        pass
    elif response == '3':
        pass
    elif response == '4':
        os.system("clear")
        quit()
    else:
        print(colored("Please Give A Valid Input...","red"))
        time.sleep(2)
        banner()
################################################################################################################################
#                                                 FULL AUTOMATIC MODE                                                          #
################################################################################################################################
                                                                                                                               #     
#check if wlan0 available                                                                                                      #
def check_interface():                                                                                                         #
    global wifi
    global inte
    wifi = input(colored("Name OF WIFI To HACk: ","blue"))
    os.system("clear")                                                                                                         #
    interface = netifaces.interfaces()                                                                                         #
    inte = interface[2]
    if 'wlan0' or 'wlan0mon' in interface:                                                                                                   #
        print(colored("Wifi Adepter Found...","green"))                                                                        #
        time.sleep(2)
        print(colored("Your Interface is {}","green").format(inte))
        time.sleep(2)                                                                                                          #
        if inte == 'wlan0mon':
            print(colored("Monitor Mode IS Already ON","green")) 
            time.sleep(2)
            callem()
        else:
            start_mon()                                                                                                            #
    else:                                                                                                                      # 
        print(colored("No Wifi Adepter Found. Please Insert Your Adepter And Run Again!","red"))                               # 
        quit()                                                                                                                 # 
                                                                                                                               #                                                                                                                                                                                                                # 
#start monitor mode                                                                                                            #
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
        netman = '0'
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
        wpas = '0'
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
        dhcl = '0'
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
    chnage_interface = netifaces.interfaces()
    change_inte = chnage_interface[2]
    os.system("clear")
    print(colored("Now Searching For {}","yellow").format(wifi))
    time.sleep(2)
    os.system("xterm -bg black -fg brown -e 'airodump-ng {} -w nearby'".format(change_inte))
    get_wifi_details()

#stops monitoring
def stop_monitoring():
    print("active")
    pid = os.popen("pgrep -n xterm").read().rstrip()
    time.sleep(5)
    os.system("kill {}".format(pid))

#get bssid channel
def get_wifi_details():
    pass

################################################################################################################################
#                                                          END                                                                 # 
################################################################################################################################                                                                  


#call functions
check_root()