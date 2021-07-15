"""
if there is no registery, line 34 gives an error
adjust currencyExchange method after currencies can store values
exception handlings are another main concept that I will consider for most methods
for now, I didn't add but we can get error message when any of related account is not present 
..by structuring if-else statement inside of each method if(...): if(self.isusd == True): ...  
system gives an error when nothing is typed into go:
checkBool() works fine but when tl comes, it also show money amount even if an account doesn't exist
implement a structure that shows only existing accounts in that list (optional) interface --> go: 2
"""
class BankCore:
    def __init__(self):
        self.tl = 0
        self.usd = 0
        self.eur = 0
        self.gold = 0

        self.isusd = False
        self.iseur = False
        self.isgold = False
        
        self.users = []
    
    print("Welcome to bankCore!\nPlase type regarding number for the next operation.\n")

    def menu(self):
        print("1. Log in\n2. Create a new account\n9. Exit\n")
        go = int(input("Go: "))
        print("")

        if(go == 1):
            print("Please type your identity number and password.")
            self.login()
            self.menu()
        elif(go == 2):
            print("Please type related informations that is asked.\n")
            self.register()
            self.menu()
        elif(go == 9):
            print("Exiting the application.\n")
            exit()
        else:  
            print("Invalid input.\nPlease try again.")
            self.menu()
            
    def login(self):
        #print("Name: {}\nSurname: {}\nIdentity number: {}\nPassword: {}\n".format(self.users["name"], self.users["surname"], self.users["id"], self.users["password"])) # implementation of register saving
        id = input("Identity number: ") # unlike other programs, int is not bounded with approximately 2*10^10
        passw = input("Password: ")
        print("")

        if(self.users["id"] == id and self.users["password"] == passw): 
            print("Logged in.")
            print("Greetings dear {}, please type respective number to operate\n".format(self.users["name"]))
            self.interface()
        else:
            print("Identity number or password is incorrect.")


    def register(self): # whichever i type incorrect input, it asked when all are typed correct from the next again
        print("Please type your informations correctly that is asked. (Type \"9\" to go back)")
        
        print("Your name should have in between 2 - 13 characters. It can NOT have any digit or special character")
        #turnBack(name, menu)
        self.nameCorrection()

        print("Your surname should have in between 2 - 15 characters. It can NOT have any digit or special character")  
        #turnBack(sname, menu)
        self.snameCorrection()
        
        print("Your identity number should only have 11 digits")
        #turnBack(id, menu)
        self.idCorrection()
        
        print("Your password should be in between 8 - 15 characters. Only letters and digits are allowed")   
        #turnBack(passw, menu)
        self.passwCorrection() 
        
        print("Your account is created\n")
        self.createUser(self.name, self.sname, self.id, self.passw) 


    def createUser(self, name, sname, id, upassw):
        self.users 
        self.users = {"name": name.capitalize(), "surname": sname.capitalize(), "id": id, "password": upassw}
        return self.users

    def printUser(self): 
        print("Informations of the user are listed.")
        print("Name: {}\nSurname: {}\nIdentity number: {}\nPassword: {}\n".format(self.users["name"], self.users["surname"], self.users["id"], self.users["password"]))
        # it overwrite if another user is typed 

    def interface(self):
        print("1. Show registry informations\n2. Display existing currency accounts\n3. Create new currency account\n4. Transfer currency\n5. Exchange Currency\n9. Log out\n")
        go = int(input("Go: "))
        print("")

        if(go == 1):
            self.printUser()

        elif(go == 2):
            # implement a structure that shows only existing accounts in that list (optional)
            print("1. TRY account\n2. USD Account\n3. EUR Account\n4. Gold Account\n")
            go = int(input("Go: "))
            print("")
            if(go == 1):
                self.tryAccount()
            elif(go == 2):
                if(self.isusd == True):
                    self.usdAccount()
                else:
                    print("You do NOT have US Dollar account to operate it.\n")
                    self.interface()
            elif(go == 3):
                if(self.iseur == True):
                    self.eurAccount()
                else:
                    print("You do NOT have Euro account to operate it.\n")
                    self.interface()
            elif(go == 4):
                if(self.isgold == True):    
                    self.goldAccount()
                else:
                    print("You do NOT have Gold account to operate it.\n")
                    self.interface()
            else:
                self.interface()

        elif(go == 3): 
            self.createCurrency()

        elif(go == 4):
            # this part will be applied after storage of multiple accounts into dictionary located in another file
            pass

        elif(go == 5):
            self.currencyExchange()

        elif(go == 9):
            self.menu() 

        else:
            self.interface()
        
        self.interface() # after deposit and withdrawing, it doesn't return interface so this is added. check it

    def tryAccount(self):
        self.tl
        print(f"1. Display currency amount\n2. Deposit TRY\n3. Withdraw TRY\n9. Return main account\n")
        go = int(input("Go: "))
        print("")

        if(go == 1):
            print("Dear {}, you have {} tl in your Turkish Lira account.\n".format(self.users["name"], str(self.tl))) 

        elif(go == 2):
            print("Please type the amount that you would like to deposit.\n")
            addtl = float(input("TRY: "))
            self.tl += addtl
            print(f"TRY balance is updated as {self.tl} tl\n")       

        elif(go == 3): 
            print("Please type the amount that you would like to withdraw.")
            taketl = float(input("TRY: "))
            self.tl -= taketl 
            
            if(self.tl >= 0):
                print(f"TRY balance is updated as {self.tl} tl.\n")
            
            else:
                self.tl += taketl 
                print(f"You have insufficient currency to withdraw {taketl} tl.\nNo currency is withdrawn.\n")

        elif(go == 9):
            self.interface()

        self.tryAccount() 

    def usdAccount(self):
        self.usd
        print(f"1. Display currency amount\n2. Deposit USD\n3. Withdraw USD\n9. Return main account\n")
        go = int(input("Go: "))
        print("")

        if(go == 1):
            print("Dear {}, you have {} dollar(s) in your US Dollar account.\n".format(self.users["name"], str(self.usd))) 

        elif(go == 2):
            print("Please type the amount that you would like to deposit.\n")
            addusd = float(input("USD: "))
            self.usd += addusd
            print(f"USD balance is updated as {self.usd} dollars\n.")       

        elif(go == 3): 
            print("Please type the amount that you would like to withdraw.")
            takeusd = float(input("USD: "))
            self.usd -= takeusd 
            
            if(self.usd >= 0):
                print(f"USD balance is updated as {self.usd} dollars.\n")
            
            else:
                self.usd += takeusd 
                print(f"You have insufficient currency to withdraw {takeusd} dollars.\nNo currency is withdrawn.\n")

        elif(go == 9):
            self.interface()

        self.usdAccount() 

    def eurAccount(self):
        self.eur
        print(f"1. Display currency amount\n2. Deposit EUR\n3. Withdraw EUR\n9. Return main account\n")
        go = int(input("Go: "))
        print("")

        if(go == 1):
            print("Dear {}, you have {} euro in your Euro account.\n".format(self.users["name"], str(self.eur))) 

        elif(go == 2):
            print("Please type the amount that you would like to deposit.\n")
            addeur = float(input("EUR: "))
            self.eur += addeur
            print(f"EUR balance is updated as {self.eur} euro\n.")       

        elif(go == 3): 
            print("Please type the amount that you would like to withdraw.")
            takeeur = float(input("EUR: "))
            self.eur -= takeeur 
            
            if(self.eur >= 0):
                print(f"EUR balance is updated as {self.eur} euro.\n")
            
            else:
                self.eur += takeeur 
                print(f"You have insufficient currency to withdraw {takeeur} euro.\nNo currency is withdrawn.\n")

        elif(go == 9):
            self.interface()

        self.eurAccount() 

    def goldAccount(self):
        self.gold # probably tl usd and eur need to be added as global
        # update second and third statements to make them dynamic!

        print("\nGold purchasing and sale operations are conducted in currency exchange tab\n")
        print("1. Display gold amount\n2. Gold stock sale price\n3. Gold stock puchasing price\n9. Return main account\n")
        go = input("Go: ")
        print("")

        if(go == "1"):
            print("Dear {}, you have {} gram(s) in your Gold account.\n".format(self.users["name"], str(self.gold))) 
            # clip decimals in 2 or 3, there are 14 of them and it does not seem okay

        elif(go == "2"): # update it so that it depends on currencies directly rather than static numbers
            print(f"Sale price of gold is:\nTRY: {500.20}\nUSD: {500.20/8.66}\nEUR: {500.20/10.29}\n")    
            # clip the decimals
            
        elif(go == "3"): # update it so that it depends on currencies directly rather than static numbers
            print(f"Purchase price of gold is:\nTRY: {500.28}\nUSD: {500.28/8.66}\nEUR: {500.28/10.29}\n") 
            # clip the decimals

        elif(go == "9"):
            self.interface()


    def currencyExchange(self): 
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

        self.tl, self.usd, self.eur, self.gold
        """ for now, I didn't add but we can get error message when any of related account is not present 
        by structuring if-else statement inside of each method if(...): if(self.isusd == True): ...  """
        if(xlira == "tl" and ylira == "usd"):
            if(self.isusd == True and money <= self.tl):
                self.tl -= money
                addmoney = money / 8.66
                self.usd += addmoney
                print(f"Current balance of {xlira.upper()}: {self.tl}, {ylira.upper()}: {self.usd}")
            else:
                self.checkBool(True, "TRY", self.isusd, "USD", self.tl, money) 
        elif(xlira == "tl" and ylira == "eur"):
            if(self.iseur == True and money <= self.tl):    
                self.tl -= money
                addmoney = money / 10.29
                self.eur += addmoney
                print(f"Current balance of {xlira.upper()}: {self.tl}, {ylira.upper()}: {self.eur}")
            else:
                self.checkBool(True, "TRY", self.iseur, "Euro", self.tl, money)    
        elif(xlira == "tl" and ylira == "gold"):
            if(self.isgold == True and money <= self.tl):     
                self.tl -= money
                addmoney = money / 500.29
                self.gold += addmoney
                print(f"Current balance of {xlira.upper()}: {self.tl}, {ylira.capitalize()}: {self.gold} gram(s)") 
            else:
                self.checkBool(True, "TRY", self.isgold, "Gold", self.tl, money)     
        elif(xlira == "usd" and ylira == "tl"):
            if(self.isusd == True and money <= self.usd):    
                self.usd -= money
                addmoney = money * 8.66
                self.tl += addmoney
                print(f"Current balance of {xlira.upper()}: {self.usd}, {ylira.upper()}: {self.tl}") # I erased \n
            else:
                self.checkBool(self.isusd, "USD", True, "TRY", self.usd, money)        
        elif(xlira == "usd" and ylira == "eur"):
            if(self.isusd == True and self.iseur == True and money <= self.usd):
                self.usd -= money
                addmoney = money / 1.19
                self.eur += addmoney  
                print(f"Current balance of {xlira.upper()}: {self.usd}, {ylira.upper()}: {self.eur}\n")
            else:
                self.checkBool(self.isusd, "USD", self.iseur, "Euro", self.usd, money) 
        elif(xlira == "usd" and ylira == "gold"):
            if(self.isusd == True and self.isgold == True and money <= self.usd):   
                self.usd -= money
                addmoney = money / 57.76
                self.gold += addmoney  
                print(f"Current balance of {xlira.upper()}: {self.usd}, {ylira.capitalize()}: {self.gold} gram(s)\n") 
            else:
                self.checkBool(self.isusd, "USD", self.isgold, "Gold", self.usd, self.money)          
        elif(xlira == "eur" and ylira == "tl"):
            if(self.iseur == True and money <= self.eur):    
                self.eur -= money
                addmoney = money * 10.29
                self.tl += addmoney     
                print(f"Current balance of {xlira.upper()}: {self.eur}, {ylira.upper()}: {self.tl}\n")
            else:
                self.checkBool(self.iseur, "Euro", True, "TRY", self.eur, money)   
        elif(xlira == "eur" and ylira == "usd"):
            if(self.iseur == True and self.isusd == True and money <= self.eur):    
                self.eur -= money
                addmoney = money * 1.19
                self.usd += addmoney
                print(f"Current balance of {xlira.upper()}: {self.eur}, {ylira.upper()}: {self.usd}\n")
            else:
                self.checkBool(self.iseur, "Euro", self.isusd, "USD", self.eur, money) 
        elif(xlira == "eur" and ylira == "gold"):
            if(self.iseur == True and self.isgold == True and money <= self.eur):    
                self.eur -= money
                addmoney = money / 48.62
                self.gold += addmoney  
                print(f"Current balance of {xlira.upper()}: {self.eur}, {ylira.capitalize()}: {self.gold} gram(s)\n")  
            else:
                self.checkBool(self.iseur, "Euro", self.isgold, "Gold", self.eur, money)    
        elif(xlira == "gold" and ylira == "tl"):
            if(self.isgold == True and money <= self.gold):    
                self.gold -= money
                addmoney = money * 500.20
                self.tl += addmoney  
                print(f"Current balance of {xlira.capitalize()}: {self.gold} gram(s), {ylira.upper()}: {self.tl}\n")
            else:
                self.checkBool(self.isgold, "Gold", True, "TRY", self.gold, money)
        elif(xlira == "gold" and ylira == "usd"):
            if(self.isgold == True and self.isusd == True and money <= self.gold):    
                self.gold -= money
                addmoney = money * 57.77
                self.usd += addmoney  
                print(f"Current balance of {xlira.capitalize()}: {self.gold} gram(s), {ylira.upper()}: {self.usd}\n")
            else:
                self.checkBool(self.isgold, "Gold", self.isusd, "USD", self.gold, money)        
        elif(xlira == "gold" and ylira == "eur"):
            if(self.isgold == True and self.iseur == True and money <= self.gold):    
                self.gold -= money
                addmoney = money * 48.61
                self.eur += addmoney  
                print(f"Current balance of {xlira.capitalize()}: {self.gold} gram(s), {ylira.upper()}: {self.eur}\n")  
            else:
                self.checkBool(self.isgold, "Gold", self.iseur, "Euro", self.gold, money)  
        else:
            print("Operation failed.\n") # fit that into conditions
            self.interface()
        
    def createCurrency(self):
        
        print("Please select an account to generate\n")
        print("1. USD Account\n2. EUR Account\n3. Gold Account\n")
        go = input("Go: ")
        print("")

        self.isusd, self.iseur, self.isgold 
        if(go == "1"):
            psw = input("Please type your password to create a USD balance: ")
            print("")
            if(psw == self.users["password"]):
                self.isusd = True
                print("USD account is created!\n")
            else:
                print("Password is incorrect, going back to main screen\n")
                self.interface()
        elif(go == "2"):
            psw = input("Please type your password to create a EUR balance: ")
            print("")
            if(psw == self.users["password"]):
                self.iseur = True
                print("Euro account is created!")
            else:
                print("Password is incorrect, going back to main screen\n")
                self.interface()
        elif(go == "3"):
            psw = input("Please type your password to create a Gold account: ")
            print("")
            if(psw == self.users["password"]):
                self.isgold = True
                print("Gold account is created!\n")
            else:
                print("Password is incorrect, going back to main screen\n")
                self.interface()
        else:
            print("Please type a number among 1 - 3\n") 
            self.interface()
        
    def checkBool(self, bool1, m1, bool2, m2, unit, mny): # it works fine but when tl comes, it also show money amount even if 
        #.. an account doesn't exist
        bool3 = False
        if(unit <= mny):
            bool3 = True
        if(bool1 == False):
            print(f"You do NOT have {m1} account for exchange operations")
            bool3 = False
        if(bool2 == False):
            print(f"You do NOT have {m2} account for exchange operations") 
            bool3 = False
        if(bool3 == True):
            print(f"You do NOT have sufficient {m1} to exchange it with {m2}\n")
        print("") # is it surplus?
        
    def nameCorrection(self):
        self.name = input("Name: ")
        print("")

        specialChar = ["!","'","^","+","%","&","/","(",")","=","?","_","-","*","|","\"","}","]","[","{","½","$","#","£",">","<",":",".","`",";",",","<","é","æ","ß","@","€","¨","~","´"]
        isuser = True
        if(len(self.name) > 13 or len(self.name) < 2):
            isuser = False
            print("Your name can NOT be less than two and more than thirteen characters\n")
        elif any(char.isdigit() for char in self.name or specialChar for char in self.name): # check if it is okay
            isuser = False
            print("Your name can NOT have digit(s) or special character(s)\n")
        if(isuser == True):
            return isuser
        else:
            self.nameCorrection()

    def snameCorrection(self):
        self.sname = input("Surname: ")
        print("")

        specialChar = ["!","'","^","+","%","&","/","(",")","=","?","_","-","*","|","\"","}","]","[","{","½","$","#","£",">","<",":",".","`",";",",","<","é","æ","ß","@","€","¨","~","´"]
        isuser = True
        if(len(self.sname) > 15 or len(self.sname) < 2):
            isuser = False
            print("Your name can NOT be less than three and more than thirteen characters\n")
        elif any(char.isdigit() for char in self.sname or specialChar for char in self.sname): # check if it is okay
            isuser = False
            print("Your surname can NOT have digit(s) or special character(s)\n")
        if(isuser == True):
            return isuser
        else:
            self.snameCorrection()

    def idCorrection(self): 
        self.id = input("Identity number: ")
        print("")
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        isuser = True
        if not(int(len(self.id)) == 11):
            isuser = False
            print("Identity number must have 11 digits\n")
        elif not all(char in nums for char in self.id):
            isuser = False
            print("Identity number only consist of integers\n")
        if(isuser == True):
            return isuser
        else:
            self.idCorrection()    

    def passwCorrection(self): 
        self.passw = input("Password: ")
        print("")

        isuser = True
        if(len(self.passw) > 15 or len(self.passw) < 8):
            isuser = False
            print("Your password can NOT be less than eigth and more than fifteen characters\n")
        elif not any(char.isdigit() for char in self.passw):
            isuser = False
            print("Password must have at least one digit\n")
        elif not any(char.isupper() for char in self.passw):
            print("Password must have at least one upper character\n")
            isuser = False
        elif not any(char.islower() for char in self.passw):
            print("Password must have at least one lower character*n")
            isuser = False 
        if(isuser == True):
            return isuser
        else:
            self.passwCorrection()

    def turnBack(self, inputVar, method): 
        # in case user type "9", system return stated function which is generally previous one
        if(inputVar == "9"):
            method()
        else:
            pass
        

#-----Execution-----#
exe = BankCore()
exe.menu()
#-----Execution-----#