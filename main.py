# developer: @aarinstech
# date: 21/07/2025
# Last updated: 21/07/2025
# version: 1.0

import pyautogui
import time
import random
import sys
import os
version = 1.0
name="Life Saver Bot by @aarinstech"

def clear():    
    if os.name == 'nt':
        sysos="cls"
    else:
        sysos="clear"
    os.system(sysos)
class cl:
    white = "\033[1;37m"
    grey = "\033[0;37m"
    purple = "\033[0;35m"
    red = "\033[1;31m"
    green = "\033[1;32m"
    yellow = "\033[1;33m"
    cyan = "\033[0;36m"
    cafe = "\033[0;33m"
    blue = "\033[1;34m"

white=cl.white
grey=cl.grey
purple=cl.purple
red=cl.red
green=cl.green
yellow=cl.yellow
cyan=cl.cyan
cafe=cl.cafe
blue=cl.blue

listcol = (white, grey, purple, red, green, yellow, cyan, cafe, blue)
color = random.choice(listcol)

with open("temp.txt", "r") as file:
    lines = file.read().splitlines()

x1 = int(lines[0])
y1 = int(lines[1])
x2 = int(lines[2])
y2 = int(lines[3])

headset_icon_pos = (x1, y1)
tea_break_pos = (x2, y2)

clear()
print(color+"\n")
print(color+"||=============||")
print(color+"|| Please Wait ||")
print(color+"||=============||")
print(color+"\n")
i=0
while i<5:
    sys.stdout.write(blue+'\rloading |')
    time.sleep(0.1)
    sys.stdout.write(red+'\rloading /')
    time.sleep(0.1)
    sys.stdout.write(yellow+'\rloading -')
    time.sleep(0.1)
    sys.stdout.write(green+'\rloading \\')
    time.sleep(0.1)
    i=i+1
clear()

print(random.choice(listcol)+
    '''

X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
|                           ,,'``````````````',,                            |
X                        ,'`                   `',                          X
|                      ,'                         ',                        |
X                    ,'          ;       ;          ',                      X
|       (           ;             ;     ;             ;     (               |
X        )         ;              ;     ;              ;     )              X
|       (         ;                ;   ;                ;   (               |
X        )    ;   ;    ,,'```',,,   ; ;   ,,,'```',,    ;   ;               X
|       (    ; ',;   '`          `',   ,'`          `'   ;,' ;              |
X        )  ; ;`,`',  _--~~~~--__   ' '   __--~~~~--_  ,'`,'; ;     )       X
|       (    ; `,' ; :  /       \~~-___-~~/       \  : ; ',' ;     (        |
X  )     )   )',  ;   -_\  o    /  '   '  \    o  /_-   ;  ,'       )   (   X
| (     (   (   `;      ~-____--~'       '~--____-~      ;'  )     (     )  |
X  )     )   )   ;            ,`;,,,   ,,,;',            ;  (       )   (   X
| (     (   (  .  ;        ,'`  (__ '_' __)  `',        ;  . )     (     )  |
X  )     \/ ,".). ';    ,'`        ~~ ~~        `',    ;  .(.", \/  )   (   X
| (   , ,'|// / (/ ,;  '        _--~~-~~--_        '  ;, \)    \|', ,    )  |
X ,)  , \/ \|  \\,/  ;;       ,; |_| | |_| ;,       ;;  \,//  |/ \/ ,   ,   X
|",   .| \_ |\/ |#\_/;       ;_| : `~'~' : |_;       ;\_/#| \/| _/ |.   ,"  |
X#(,'  )  \\\#\ \##/)#;     :  `\/       \/   :     ;#(\##/ /#///  (  ',)# ,X
|| ) | \ |/ /#/ |#( \; ;     :               ;     ; ;/ )#| \#\ \| / | ( |) |
X\ |.\\ |\_/#| /#),,`   ;     ;./\_     _/\.;     ;   `,,(#\ |#\_/| //.| / ,X
| \\_/# |#\##/,,'`       ;     ~~--|~|~|--~~     ;       `',,\##/#| #\_// \/|
X  ##/#  #,,'`            ;        ~~~~~        ;            `',,#  #\##  //X
|####@,,'`                 `',               ,'`                 `',,@####| |
X#,,'`                        `',         ,'`                        `',,###X
|'  spb                          ~~-----~~                               `' |
X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
              
        "The quieter you become,
         the more you are able to hear."

                       — KALI
'''
)
print(red+       r"     Follow Me On Instagram : @aarinstech                                             ")
print(purple+    r"     Follow Me On Twitter : @aarinstech                                               ") 
print(grey+      r"     Follow Me On Github : https://github.com/aarinstech                              ")
print(red+       r"     Subscribe To My Youtube Channel : aarinstech                                     ")
print(random.choice(listcol)+"     Version  ",version)

print("\n")
print("\n")
print("Welcome To",name)
print("\n")
print(red+"note: you can also use 0 for waiting time and break time")
waiting_time = int(input(white+"Enter the waiting/avail time (in seconds): "))
bt1 = int(input(white+"Enter the minimum break time (in seconds): "))
bt2 = int(input(white+"Enter the maximum break time (in seconds): "))
number_of_breaks = int(input(white+"Enter the number of breaks: "))

print(color+"\n\nYOU GOT 10 SECONDS TO SWITCH TO YOUR TARGET !!")
time.sleep(11)
if bt1==bt2:
    break_time = bt1
else:
    break_time = random.randrange(bt1, bt2)

i = 1
while i<=number_of_breaks:
    pyautogui.moveTo(headset_icon_pos[0], headset_icon_pos[1], duration=0.5)
    # pyautogui.moveTo(headset_icon_pos)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(tea_break_pos[0], tea_break_pos[1], duration=0.5)
    pyautogui.click()
    time.sleep(break_time)
    pyautogui.moveTo(headset_icon_pos)
    pyautogui.click()
    # time.sleep(break_time)
    pyautogui.moveTo(tea_break_pos)
    pyautogui.click()
    time.sleep(waiting_time)
    i += 1
    
print(color+"\n\nTASK COMPLETED !")