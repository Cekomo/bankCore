"""
if there is no registery, line 34 gives an error
adjust currencyExchange method after currencies can store values
exception handlings are another main concept that I will consider for most methods
for now, I didn't add but we can get error message when any of related account is not present 
..by structuring if-else statement inside of each method if(...): if(isusd == True): ...  
system gives an error when nothing is typed into go:
checkBool() works fine but when tl comes, it also show money amount even if an account doesn't exist
"""

users = []
tl = 0
usd = 0
eur = 0
gold = 0

isusd = False
iseur = False
isgold = False

isname = True
issname = True
isid = True
ispassw = True
bool1 = False

print("Welcome to bankCore!\nPlase type regarding number for the next operation.\n")

def menu():
    print("\n1. Log in\n2. Create a new account\n9. Log out\n")
    go = int(input("Go: "))

    if(go == 1):
        print("\nPlease type your identity number and password.")
        login()
        menu()
    elif(go == 2):
        print("Please type related informations that is asked.\n")
        register()
        menu()
    elif(go == 9):
        print("Exiting the application.\n")
        exit()
    else:  
        print("Invalid input.\nPlease try again.")
        menu()
        
def login():
    id = input("Identity number: ") # unlike other programs, int is not bounded with approximately 2*10^10
    passw = input("Password: ")
    print("")

    if(users["id"] == id and users["password"] == passw): 
        print("Logged in.")
        print("Greetings dear {}, please type respective number to operate\n".format(users["name"]))
        interface()
    else:
        print("Identity number or password is incorrect.")


def register(): # whichever i type incorrect input, it asked when all are typed correct from the next again
    print("Please type your informations correctly that is asked. (Type \"9\" to go back)")
    
    print("Your name should have in between 3 - 13 characters. It can NOT have any digit or special character\n")
    name = input("Name: ")
    turnBack(name, menu)
    nameCorrection(isname, name, 3, 13, "Name")

    print("Your surname should have in between 2 - 15 characters. It can NOT have any digit or special character\n")
    sname = input("Surname: ")
    turnBack(sname, menu)
    nameCorrection(issname, sname, 2, 15, "Surname")
      
    print("Your identity number should only have 11 digits\n")
    id = input("Identity number: ") # that was int
    turnBack(id, menu)
    idCorrection(isid, id)
    
    print("Your password should be in between 8 - 15 characters. Only letters and digits are allowed\n")
    passw = input("Password: ")
    turnBack(passw, menu)
    passwCorrection(ispassw, passw) # when I type wrong input and type for correct, it prints ln 83 for two times
    
    if(isname == True and issname == True and isid == True and ispassw == True):
        print("Your account is created")
        createUser(name, sname, id, passw) # i think it does not save the inputs
    else: 
        register()

def createUser(name, sname, id, upassw):
    global users 
    users = {"name": name.capitalize(), "surname": sname.capitalize(), "id": id, "password": upassw}
    return users

def printUser(): 
    print("\nInformations of the user are listed.")
    print("Name: {}\nSurname: {}\nIdentity number: {}\nPassword: {}\n".format(users["name"], users["surname"], users["id"], users["password"]))
    # it overwrite if another user is typed 

def interface():
    print("1. Show registry informations\n2. Display existing currency accounts\n3. Create new currency account\n4. Transfer currency\n5. Exchange Currency\n9. Return main menu\n")
    go = int(input("Go: "))

    if(go == 1):
        printUser()

    elif(go == 2):
        print("1. TRY account\n2. USD Account\n3. EUR Account\n4. Gold Account\n")
        go = int(input("Go: "))
        if(go == 1):
            tryAccount()
        elif(go == 2):
            if(isusd == True):
                usdAccount()
            else:
                print("You do NOT have US Dollar account to operate it.\n")
                interface()
        elif(go == 3):
            if(iseur == True):
                eurAccount()
            else:
                print("You do NOT have Euro account to operate it.\n")
                interface()
        elif(go == 4):
            if(isgold == True):    
                goldAccount()
            else:
                print("You do NOT have Gold account to operate it.\n")
                interface()
        else:
            interface()

    elif(go == 3): 
        createCurrency()

    elif(go == 4):
        # this part will be applied after storage of multiple accounts into dictionary located in another file
        pass

    elif(go == 5):
        currencyExchange()

    elif(go == 9):
        menu() 

    else:
        interface()
    
    interface() # after deposit and withdrawing, it doesn't return interface so this is added. check it

def tryAccount():
    global tl
    print(f"\n1. Display currency amount\n2. Deposit TRY\n3. Withdraw TRY\n9. Return main account\n")
    go = int(input("Go: "))

    if(go == 1):
        print("\nDear {}, you have {} tl in your Turkish Lira account.".format(users["name"], str(tl))) 

    elif(go == 2):
        
        print("\nPlease type the amount that you would like to deposit.\n")
        addtl = float(input("TRY: "))
        tl += addtl
        print(f"TRY balance is updated as {tl} tl\n.")       

    elif(go == 3): 
        print("\nPlease type the amount that you would like to withdraw.")
        taketl = float(input("TRY: "))
        tl -= taketl 
        
        if(tl >= 0):
            print(f"TRY balance is updated as {tl} tl.\n")
           
        else:
            tl += taketl 
            print(f"\nYou have insufficient currency to withdraw {taketl} tl.\nNo currency is withdrawn.\n")

    elif(go == 9):
        interface()

    tryAccount() 

def usdAccount():
    global usd
    print(f"\n1. Display currency amount\n2. Deposit USD\n3. Withdraw USD\n9. Return main account\n")
    go = int(input("Go: "))

    if(go == 1):
        print("\nDear {}, you have {} dollar(s) in your US Dollar account.\n".format(users["name"], str(usd))) 

    elif(go == 2):
        print("\nPlease type the amount that you would like to deposit.\n")
        addusd = float(input("USD: "))
        usd += addusd
        print(f"USD balance is updated as {usd} dollars\n.")       

    elif(go == 3): 
        print("\nPlease type the amount that you would like to withdraw.")
        takeusd = float(input("USD: "))
        usd -= takeusd 
        
        if(usd >= 0):
            print(f"USD balance is updated as {usd} dollars.\n")
           
        else:
            usd += takeusd 
            print(f"\nYou have insufficient currency to withdraw {takeusd} dollars.\nNo currency is withdrawn.\n")

    elif(go == 9):
        interface()

    usdAccount() 

def eurAccount():
    global eur
    print(f"\n1. Display currency amount\n2. Deposit EUR\n3. Withdraw EUR\n9. Return main account\n")
    go = int(input("Go: "))

    if(go == 1):
        print("\nDear {}, you have {} euro in your Euro account.\n".format(users["name"], str(eur))) 

    elif(go == 2):
        print("\nPlease type the amount that you would like to deposit.\n")
        addeur = float(input("EUR: "))
        eur += addeur
        print(f"EUR balance is updated as {eur} euro\n.")       

    elif(go == 3): 
        print("\nPlease type the amount that you would like to withdraw.")
        takeeur = float(input("EUR: "))
        eur -= takeeur 
        
        if(eur >= 0):
            print(f"EUR balance is updated as {eur} euro.\n")
           
        else:
            eur += takeeur 
            print(f"\nYou have insufficient currency to withdraw {takeeur} euro.\nNo currency is withdrawn.\n")

    elif(go == 9):
        interface()

    eurAccount() 

def goldAccount():
    global gold # probably tl usd and eur need to be added as global
    # update second and third statements to make them dynamic!

    print("\nGold purchasing and sale operations are conducted in currency exchange tab\n")
    print("1. Display gold amount\n2. Gold stock sale price\n3. Gold stock puchasing price\n9. Return main account\n")
    go = input("Go: ")

    if(go == "1"):
        print("\nDear {}, you have {} gram(s) in your Gold account.\n".format(users["name"], str(gold))) 
        # clip decimals in 2 or 3, there are 14 of them and it does not seem okay

    elif(go == "2"): # update it so that it depends on currencies directly rather than static numbers
        print(f"\nSale price of gold is:\nTRY: {500.20}\nUSD: {500.20/8.66}\nEUR: {500.20/10.29}\n")    
        # clip the decimals
        
    elif(go == "3"): # update it so that it depends on currencies directly rather than static numbers
        print(f"\nPurchase price of gold is:\nTRY: {500.28}\nUSD: {500.28/8.66}\nEUR: {500.28/10.29}\n") 
        # clip the decimals

    elif(go == "9"):
        interface()


def currencyExchange(): 
    """ as a second stage, add a layer that shows the value for result of exchange and ask permission 
    from user to imply it """ 
    print("Please state the currency that you will give.")
    xlira = str(input("tl / usd / eur / gold: "))
    print("")
    print("Please state the currency that you will get.")
    ylira = str(input("tl / usd / eur / gold: "))
    print("")
    print(f"Please type the amount of {xlira.upper()} that you would like to exchange to {ylira.upper()}")
    money = float(input(f"{xlira.upper()} to {ylira.upper()} with the amount of: "))
    print("")

    global tl, usd, eur, gold
    """ for now, I didn't add but we can get error message when any of related account is not present 
    by structuring if-else statement inside of each method if(...): if(isusd == True): ...  """
    if(xlira == "tl" and ylira == "usd"):
        if(isusd == True and money <= tl):
            tl -= money
            addmoney = money / 8.66
            usd += addmoney
            print(f"Current balance of {xlira.upper()}: {tl}, {ylira.upper()}: {usd}")
        else:
            checkBool(True, "TRY", isusd, "USD", tl, money) 
    elif(xlira == "tl" and ylira == "eur"):
        if(iseur == True and money <= tl):    
            tl -= money
            addmoney = money / 10.29
            eur += addmoney
            print(f"Current balance of {xlira.upper()}: {tl}, {ylira.upper()}: {eur}")
        else:
            checkBool(True, "TRY", iseur, "Euro", tl, money)    
    elif(xlira == "tl" and ylira == "gold"):
        if(isgold == True and money <= tl):     
            tl -= money
            addmoney = money / 500.29
            gold += addmoney
            print(f"Current balance of {xlira.upper()}: {tl}, {ylira.capitalize()}: {gold} gram(s)") 
        else:
            checkBool(True, "TRY", isgold, "Gold", tl, money)     
    elif(xlira == "usd" and ylira == "tl"):
        if(isusd == True and money <= usd):    
            usd -= money
            addmoney = money * 8.66
            tl += addmoney
            print(f"Current balance of {xlira.upper()}: {usd}, {ylira.upper()}: {tl}") # I erased \n
        else:
            checkBool(isusd, "USD", True, "TRY", usd, money)        
    elif(xlira == "usd" and ylira == "eur"):
        if(isusd == True and iseur == True and money <= usd):
            usd -= money
            addmoney = money / 1.19
            eur += addmoney  
            print(f"Current balance of {xlira.upper()}: {usd}, {ylira.upper()}: {eur}\n")
        else:
            checkBool(isusd, "USD", iseur, "Euro", usd, money) 
    elif(xlira == "usd" and ylira == "gold"):
        if(isusd == True and isgold == True and money <= usd):   
            usd -= money
            addmoney = money / 57.76
            gold += addmoney  
            print(f"Current balance of {xlira.upper()}: {usd}, {ylira.capitalize()}: {gold} gram(s)\n") 
        else:
            checkBool(isusd, "USD", isgold, "Gold", usd, money)          
    elif(xlira == "eur" and ylira == "tl"):
        if(iseur == True and money <= eur):    
            eur -= money
            addmoney = money * 10.29
            tl += addmoney     
            print(f"Current balance of {xlira.upper()}: {eur}, {ylira.upper()}: {tl}\n")
        else:
            checkBool(iseur, "Euro", True, "TRY", eur, money)   
    elif(xlira == "eur" and ylira == "usd"):
        if(iseur == True and isusd == True and money <= eur):    
            eur -= money
            addmoney = money * 1.19
            usd += addmoney
            print(f"Current balance of {xlira.upper()}: {eur}, {ylira.upper()}: {usd}\n")
        else:
            checkBool(iseur, "Euro", isusd, "USD", eur, money) 
    elif(xlira == "eur" and ylira == "gold"):
        if(iseur == True and isgold == True and money <= eur):    
            eur -= money
            addmoney = money / 48.62
            gold += addmoney  
            print(f"Current balance of {xlira.upper()}: {eur}, {ylira.capitalize()}: {gold} gram(s)\n")  
        else:
            checkBool(iseur, "Euro", isgold, "Gold", eur, money)    
    elif(xlira == "gold" and ylira == "tl"):
        if(isgold == True and money <= gold):    
            gold -= money
            addmoney = money * 500.20
            tl += addmoney  
            print(f"Current balance of {xlira.capitalize()}: {gold} gram(s), {ylira.upper()}: {tl}\n")
        else:
            checkBool(isgold, "Gold", True, "TRY", gold, money)
    elif(xlira == "gold" and ylira == "usd"):
        if(isgold == True and isusd == True and money <= gold):    
            gold -= money
            addmoney = money * 57.77
            usd += addmoney  
            print(f"Current balance of {xlira.capitalize()}: {gold} gram(s), {ylira.upper()}: {usd}\n")
        else:
            checkBool(isgold, "Gold", isusd, "USD", gold, money)        
    elif(xlira == "gold" and ylira == "eur"):
        if(isgold == True and iseur == True and money <= gold):    
            gold -= money
            addmoney = money * 48.61
            eur += addmoney  
            print(f"Current balance of {xlira.capitalize()}: {gold} gram(s), {ylira.upper()}: {eur}\n")  
        else:
            checkBool(isgold, "Gold", iseur, "Euro", gold, money)  
    else:
        print("Operation failed.\n") # fit that into conditions
        interface()
    
def createCurrency():
    
    print("Please select an account to generate\n")
    print("1. USD Account\n2. EUR Account\n3. Gold Account\n")
    go = input("Go: ")

    global isusd, iseur, isgold 
    if(go == "1"):
        psw = input("Please type your password to create a USD balance: ")
        print("")
        if(psw == users["password"]):
            isusd = True
            print("USD account is created!\n")
        else:
            print("Password is incorrect, going back to main screen\n")
            interface()
    elif(go == "2"):
        psw = input("Please type your password to create a EUR balance: ")
        print("")
        if(psw == users["password"]):
            iseur = True
            print("Euro account is created!")
        else:
            print("Password is incorrect, going back to main screen\n")
            interface()
    elif(go == "3"):
        psw = input("Please type your password to create a Gold account: ")
        print("")
        if(psw == users["password"]):
            isgold = True
            print("Gold account is created!\n")
        else:
            print("Password is incorrect, going back to main screen\n")
            interface()
    else:
        print("Please type a number among 1 - 3\n") 
        interface()
    
def checkBool(bool1, m1, bool2, m2, unit, mny): # it works fine but when tl comes, it also show money amount even if 
    #.. an account doesn't exist
    if(bool1 == False):
        print(f"You do NOT have {m1} account for exchange operations")
    elif(unit <= mny):
        print(f"You do NOT have sufficient {m1} to exchange it with {m2}")
    if(bool2 == False):
        print(f"You do NOT have {m2} account for exchange operations")
    elif(unit <= mny):
        print(f"You do NOT have sufficient {m1} to exchange it with {m2}") 
    # print("") # is it surplus?
    
def nameCorrection(isuser, name, minnum, maxnum, nm):
    specialChar = ["!","'","^","+","%","&","/","(",")","=","?","_","-","*","|","\"","}","]","[","{","½","$","#","£",">","<",":",".","`",";",",","<","é","æ","ß","@","€","¨","~","´"]
    isuser = True
    if(len(name) > maxnum or len(name) < minnum):
        isuser = False
        print("Your name can NOT be less than three and more than thirteen characters\n")
    elif any(char.isdigit() for char in name or char in specialChar for char in name): # check if it is okay
        isuser = False
        print("Your name can NOT have digit(s) or special character(s)\n")
    if(isuser == True):
        return isuser
    else:
        name = input(f"{nm}: ")
        nameCorrection(isuser, name, minnum, maxnum, nm)
    

def idCorrection(isuser, idnum): 
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    isuser = True
    if not(int(len(idnum)) == 11):
        isuser = False
        print("Identity number must have 11 digits\n")
    elif not all(char in nums for char in idnum):
        isuser = False
        print("Identity number only consist of integers\n")
    if(isuser == True):
        return isuser
    else:
        id = input("Identity number: ")
        idCorrection(isuser, id)
    

def passwCorrection(isuser, psw): 
    isuser = True
    if(len(psw) > 15 or len(psw) < 8):
        isuser = False
        print("Your password can NOT be less than eigth and more than fifteen characters\n")
    elif not any(char.isdigit() for char in psw):
        isuser = False
        print("Password must have at least one digit\n")
    elif not any(char.isupper() for char in psw):
        print("Password must have at least one upper character\n")
        isuser = False
    elif not any(char.islower() for char in psw):
        print("Password must have at least one lower character*n")
        isuser = False 
    if(isuser == True):
        return isuser
    else:
        passw = input("Password: ")
        passwCorrection(isuser, passw)
    

def turnBack(inputVar, method): 
    # in case user type "9", system return stated function which is generally previous one
    if(inputVar == "9"):
        method()
    else:
        pass
    

#-----Execution-----#
menu()
#-----Execution-----#

