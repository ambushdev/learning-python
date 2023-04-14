# ABYSS 1.0 // ambushdev // ambush#0777
# CMD GUI TEST PROGRAM
# RUN IN CMD USING "py ABYSS 1.0 CMD GUI TEST.py"

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import requests
import json

options = ["1", "2"]

colorama_init()

# FBI WANTED API
def wantedapi():
  try:
    count = 0
    descriptions = input("descriptions? Y/N: ").upper()
    
    if "Y" in descriptions:
      print("ok")
    elif "N" in descriptions:
      print("ok")
    else:
      wantedapi()
    
    num = int(input("results: "))
    
    url = f"https://api.fbi.gov/wanted/v1/list"

    data = requests.get(url).json()
    
    for count in range(num):
      print("\n")
      print(data['items'][count]['title'])
      print("\n")
      print(data['items'][count]['url'])
      print("\n")
      if descriptions == "Y":
        print(data['items'][count]['details'])
      count = count + 1
    else:
      menu()
  except:
    print("ERROR: couldnt produce results. returning to menu...\n")
    menu()
    

# ADVANCED CALCULATOR
def advancedcalculator():
  try:
    operators = ["+", "-", "*", "/", "%", "**"]

    print(f"\nUse following operators: {operators}")

    calc = input("Calculate: ").split()

    if calc[1] in operators:
      
      op = {
      
      '+': lambda x,y: x + y, 
      '-': lambda x,y: x - y, 
      '*': lambda x,y: x * y, 
      '/': lambda x,y: x / y,
      '%': lambda x,y: x % y,
      '**': lambda x,y: x ** y

      
      }

      res = op[calc[1]](int(calc[0]),int(calc[2]))
      print(f"{calc[0]} {calc[1]} {calc[2]} = {res}\n")
      menu()

    else:
      print(f"Use following operators: {operators}")
      menu()
  except:
    advancedcalculator()

# ASCII TITLE DISPLAY
def title():
  print(f"""{Fore.MAGENTA}# ABYSS 1.0 // ambushdev // ambush#0777
 {Fore.BLUE}                                             .        .
                  .                           ;W       ;W
               .. Ef.        f.     ;WE.     f#E      f#E
              ;W, E#Wi       E#,   i#G     .E#f     .E#f  
             j##, E#K#D:     E#t  f#f     iWW;     iWW;  
  {Fore.LIGHTBLUE_EX}          G###, E#  E#f.   E#t G#i     L##Lffi  L##Lffi
          :E####, E#WEE##Wt  E#jEW,     tLLG##L  tLLG##L 
         ;W#DG##, E##Ei;;;;. E##E.        ,W#i     ,W#i  
        j###DW##, E#DWWt     E#G         j#E.     j#E.   
  {Fore.CYAN}     G##i,,G##, E#. .#K;   E#t       .D#j     .D#j     
     :K#K:   L##, E#Dfff##E, E#t      ,WK,     ,WK,      
    ;##D.    L##, jLLLLLLLLL;EE.      EG.      EG.       
    ,,,      .,,             t        ,        ,{Style.RESET_ALL}\n""")   

# MENU WITH OPTIONS
try:
  def menu():
    print(f"""{Fore.LIGHTBLUE_EX}  
    ##MENU:###################################################
    #                                                        #
    # 1. ADVANCED CALCULATOR            2. FBI WANTED API    #
    #                                                        #
    #########################################TYPE X TO QUIT.##{Style.RESET_ALL}\n""")
    selection = input(f"{Fore.CYAN}ABYSS > ").upper()
    if "X" in selection:
      quit
    elif "1" in selection:
      advancedcalculator()
    elif "2" in selection:
      wantedapi()
    else:
      menu()
except:
  print("ERROR")


title()
menu()



    
  





