"""
if there is no registery, line 34 gives an error
adjust currencyExchange method after currencies can store values
exception handlings are another main concept that I will consider for most methods
"""

users = []
tl = 0
usd = 0
eur = 0
gold = 0

print("Welcome to bankCore!\nPlase type regarding number for the next operation.\n")

def menu():
    print("1. Log in\n2. Create a new account\n9. Log out\n")
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
        exit
    else:  
        print("Invalid input.\nPlease try again.")
        menu()
        
def login():
    id = int(input("Identity number: ")) # unlike other programs, int is not bounded with approximately 2*10^10
    passw = input("Password: ")

    if(users["id"] == id and users["password"] == passw): 
        print("Logged in.\n")
        print("Greetings dear {}, please type respective number to operate\n".format(users["name"]
        ))
        interface()
    else:
        print("Identity number or password is incorrect.")


def register():
    print("Please type your informations correctly that is asked.")
    
    name = input("Name: ")
    sname = input("Surname: ")
    id = int(input("Identity number: ")) 
    passw = input("Password: ")

    createUser(name, sname, id, passw)

def createUser(name, sname, id, passw):
    global users 
    users = {"name": name.capitalize(), "surname": sname.capitalize(), "id": id, "password": passw}
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
            usdAccount()
        elif(go == 3):
            eurAccount()
        elif(go == 4):
            goldAccount()
            pass
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
        print("\nDear {}, you have {} tl in your Turkish Lira account.\n".format(users["name"], str(tl))) 

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
    go = int(input("Go: "))

    if(go == 1):
        print("\nDear {}, you have {} gram(s) in your Gold account.\n".format(users["name"], str(gold))) 
        # clip decimals in 2 or 3, there are 14 of them and it does not seem okay

    elif(go == 2): # update it so that it depends on currencies directly rather than static numbers
        print(f"\nSale price of gold is:\nTRY: {500.20}\nUSD: {500.20/8.66}\nEUR: {500.20/10.29}\n")    
        # clip the decimals
        
    elif(go == 3): # update it so that it depends on currencies directly rather than static numbers
        print(f"\nPurchase price of gold is:\nTRY: {500.28}\nUSD: {500.28/8.66}\nEUR: {500.28/10.29}\n") 
        # clip the decimals

    elif(go == 9):
        interface()


def currencyExchange(): 
    """ as a second stage, add a layer that shows the value for result of exchange and ask permission 
    from user to imply it """ 
    print("Please state the currency that you will give.")
    xlira = str(input("tl / usd / eur / gold: "))
    print("Please state the currency that you will get.")
    ylira = str(input("tl / usd / eur / gold: "))
    print(f"Please type the amount of {xlira.upper()} that you would like to exchange to {ylira.upper()}")
    money = float(input(f"{xlira.upper()} to {ylira.upper()} with the amount of: "))
    
    global tl, usd, eur, gold
    if(xlira == "tl" and ylira == "usd" and money <= tl):
        tl -= money
        addmoney = money / 8.66
        usd += addmoney
        print(f"Current balance of {xlira.upper()}: {tl}, {ylira.upper()}: {usd}\n") 
    elif(xlira == "tl" and ylira == "eur" and money <= tl):
        tl -= money
        addmoney = money / 10.29
        eur += addmoney
        print(f"Current balance of {xlira.upper()}: {tl}, {ylira.upper()}: {eur}\n")    
    elif(xlira == "tl" and ylira == "gold" and money <= tl):
        tl -= money
        addmoney = money / 500.29
        gold += addmoney
        print(f"Current balance of {xlira.upper()}: {tl}, {ylira.capitalize()}: {gold} gram(s)\n")      
    elif(xlira == "usd" and ylira == "tl" and money <= usd):
        usd -= money
        addmoney = money * 8.66
        tl += addmoney
        print(f"Current balance of {xlira.upper()}: {usd}, {ylira.upper()}: {tl}\n")        
    elif(xlira == "usd" and ylira == "eur" and money <= usd):
        usd -= money
        addmoney = money / 1.19
        eur += addmoney  
        print(f"Current balance of {xlira.upper()}: {usd}, {ylira.upper()}: {eur}\n") 
    elif(xlira == "usd" and ylira == "gold" and money <= usd):
        usd -= money
        addmoney = money / 57.76
        gold += addmoney  
        print(f"Current balance of {xlira.upper()}: {usd}, {ylira.capitalize()}: {gold} gram(s)\n")           
    elif(xlira == "eur" and ylira == "tl" and money <= eur):
        eur -= money
        addmoney = money * 10.29
        tl += addmoney     
        print(f"Current balance of {xlira.upper()}: {eur}, {ylira.upper()}: {tl}\n")   
    elif(xlira == "eur" and ylira == "usd" and money <= eur):
        eur -= money
        addmoney = money * 1.19
        usd += addmoney
        print(f"Current balance of {xlira.upper()}: {eur}, {ylira.upper()}: {usd}\n") 
    elif(xlira == "eur" and ylira == "gold" and money <= eur):
        eur -= money
        addmoney = money / 48.62
        gold += addmoney  
        print(f"Current balance of {xlira.upper()}: {eur}, {ylira.capitalize()}: {gold} gram(s)\n")      
    elif(xlira == "gold" and ylira == "tl" and money <= gold):
        gold -= money
        addmoney = money * 500.20
        tl += addmoney  
        print(f"Current balance of {xlira.capitalize()}: {gold} gram(s), {ylira.upper()}: {tl}\n")
    elif(xlira == "gold" and ylira == "usd" and money <= gold):
        gold -= money
        addmoney = money * 57.77
        usd += addmoney  
        print(f"Current balance of {xlira.capitalize()}: {gold} gram(s), {ylira.upper()}: {usd}\n")
    elif(xlira == "gold" and ylira == "eur" and money <= gold):
        gold -= money
        addmoney = money * 48.61
        eur += addmoney  
        print(f"Current balance of {xlira.capitalize()}: {gold} gram(s), {ylira.upper()}: {eur}\n")    
    else:
        print("You do not meet necesarry statements.") # fit that into conditions
        interface()
    
def createCurrency():
    print("Please select an account to generate\n")
    print("1. USD Account\n2. EUR Account\n3. Gold Account\n")
    go = input("Go: ")
    psw = input("Please type your password to continue: ")

    if(psw == users["password"]):
        if(go == 1):
            pass
        elif(go == 2):
            pass
        elif(go == 3):
            pass
        else:
            print("Out of scope") # arrange the text. structure is asking password and responding about "go" 
            #variable later fix it as well
    else:
        print("Password is incorrect")
        interface()
    

#-----Execution-----#
menu()
#-----Execution-----#

