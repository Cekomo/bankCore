
# I can code a method that ask for permission to the user after any operation about implementation 
# implement a structure that shows only existing accounts in that list (optional) interface --> go: 2
# addmoney variables still breaks the code
# for pay/withdraw methods, program doesn't execute from "self.themoney += increment" (ln 524)

class BankCore:
    def __init__(self):
        self.tl = 0
        self.usd = 0
        self.eur = 0
        self.gold = 0

        self.isusd = False
        self.iseur = False
        self.isgold = False
        
        self.users = {"name": "Cekomo", "surname": "", "id": "admin", "password": "admin"}
    
    print("Welcome to bankCore version Alpha(0.1)!\nPlase type regarding number for the next operation.\n")

    def menu(self):
        print("1. Log in\n2. Create a new account\n9. Exit\n")
        go = input("Go: ")
        print("")

        if(go == "1"):
            print("Please type your identity number and password.")
            self.login()
            self.menu()
        elif(go == "2"):
            print("Please type related informations that is asked.\n")
            self.register()
            self.menu()
        elif(go == "9"):
            print("Exiting the application.\n")
            exit()
        else:  
            print("Invalid input.\nPlease try again.\n")
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
        elif(self.users["id"] != id or self.users["password"] != passw):
            print("Identity number or password is incorrect.\n")
        else:
            print("Identity number or password is incorrect.\n")


    def register(self): # whichever i type incorrect input, it asked when all are typed correct from the next again
        print("Please type your informations correctly that is asked. (Type \"9\" to go back)\n")
        
        # print("Your name should have in between 2 - 13 characters. It can NOT have any digit or special character")
        self.nameCorrection()

        # print("Your surname should have in between 2 - 15 characters. It can NOT have any digit or special character")  
        self.snameCorrection()
        
        print("Please type your identity number that consist of 11 digits")
        self.idCorrection()
        
        print("Your password must consist of:\n8 - 15 characters,\nAt least one upper letter,\nAt least one lower letter,\nAt least one digit,\nNo special characters.\n")   
        self.passwCorrection() 
        
        print("Your account is created\n")
        self.createUser(self.name, self.sname, self.id, self.passw) 

    def createUser(self, name, sname, id, passw):
        self.users 
        self.users = {"name": name.capitalize(), "surname": sname.capitalize(), "id": id, "password": passw}
        return self.users

    def printUser(self): # it overwrite if another user is typed 
        print("Informations of the user are listed.")
        print("Name: {}\nSurname: {}\nIdentity number: {}\nPassword: {}\n".format(self.users["name"], self.users["surname"], self.users["id"], self.users["password"]))
        
    def interface(self):
        print("1. Show registry informations\n2. Operate currency accounts\n3. Create new currency account\n4. Transfer currency\n5. Exchange Currency\n9. Log out\n")
        go = input("Go: ")
        print("")

        if(go == "1"):
            self.printUser()

        elif(go == "2"):
            # implement a structure that shows only existing accounts in that list (optional)
            self.currencyAccount(self.isusd, self.iseur, self.isgold)

        elif(go == "3"): 
            self.createCurrency()

        elif(go == "4"):
            print("Currency transfer operation is under construction\n")

        elif(go == "5"):
            self.currencyExchange()

        elif(go == "9"):
            self.menu() 

        else:
            self.interface()
        
        self.interface() # after deposit and withdrawing, it doesn't return interface so this is added. check it

    def tryAccount(self):
        self.tl
        print(f"1. Display currency amount\n2. Deposit TRY\n3. Withdraw TRY\n9. Return main screen\n")
        go = input("Go: ")
        print("")

        if(go == "1"):
            print("Dear {}, you have {} tl in your Turkish Lira account.\n".format(self.users["name"], str(self.tl))) 

        elif(go == "2"):
            self.payMoney(self.tl, "TRY", "Turkish liras")       

        elif(go == "3"): 
            self.withdrawMoney(self.tl, "TRY", "Turkish liras")

        elif(go == "9"):
            self.interface()
        else:
            print("Please type any respective number to operate\n")
            self.tryAccount() 

    def usdAccount(self):
        self.usd
        print(f"1. Display currency amount\n2. Deposit USD\n3. Withdraw USD\n9. Return main screen\n")
        go = input("Go: ")
        print("")

        if(go == "1"):
            print("Dear {}, you have {} dollar(s) in your US Dollar account.\n".format(self.users["name"], str(self.usd))) 

        elif(go == "2"):
            self.payMoney(self.usd, "USD", "dollars")       

        elif(go == "3"): 
            self.withdrawMoney(self.usd, "USD", "dollars")  

        elif(go == "9"):
            self.interface()
        else:
            print("Please type any respective number to operate\n")
            self.usdAccount() 

    def eurAccount(self):
        self.eur
        print(f"1. Display currency amount\n2. Deposit EUR\n3. Withdraw EUR\n9. Return main screen\n")
        go = input("Go: ")
        print("")

        if(go == "1"):
            print("Dear {}, you have {} euro in your Euro account.\n".format(self.users["name"], str(self.eur))) 

        elif(go == "2"):
            self.payMoney(self.eur, "EUR", "euros")         

        elif(go == "3"): 
            self.withdrawMoney(self.eur, "EUR", "euros")

        elif(go == "9"):
            self.interface()
        else:
            print("Please type any respective number to operate\n")            
            self.eurAccount() 

    def goldAccount(self):
        self.gold # update second and third statements to make them dynamic!

        print("Gold purchasing and sale operations are conducted in currency exchange tab\n")
        print("1. Display gold amount\n2. Gold stock sale price\n3. Gold stock puchasing price\n9. Return main screen\n")
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
        else:
            print("Please type any respective number to operate\n")
            self.goldAccount()


    def currencyExchange(self): # for money variable, input can not be float. This is bad for gold exchange 
        self.tl, self.usd, self.eur, self.gold
        
        print("Please state the currency that you will give.")
        self.islira = False
        while(self.islira == False): # both structures can be merged into one but there is no need i believe 
            xlira = input("tl / usd / eur / gold: ")
            if(xlira == "tl" or xlira == "usd" or xlira == "eur" or xlira == "gold"):
                self.islira = True
            else:
                print("Please pick one of the currency methods that are stated")
        print("")
        
        print("Please state the currency that you will get.")
        self.islira = False
        while(self.islira == False):
            ylira = input("tl / usd / eur / gold: ")
            if(ylira == "tl" or ylira == "usd" or ylira == "eur" or ylira == "gold"):
                self.islira = True
            else:
                print("Please pick one of the currency methods that are stated")
        print("")
        if(xlira == ylira):
            print("You can NOT exchange money by from an account to same account. Plase type responding currency methods again\n")
            self.currencyExchange()
        else:
            print(f"Please type the amount of {xlira.upper()} that you would like to exchange to {ylira.upper()}")
        
        print("Your asset is shown below\n")
        print(f"TRY: {self.tl}      |     USD: {self.usd}      |      EUR: {self.eur}      |      Gold: {self.gold}\n")
        self.islira = False
        while(self.islira == False):
            money = input(f"{xlira.upper()} to {ylira.upper()} with the amount of: ")
            if(money.isdigit()):
                self.islira = True
            else:
                print("Please type valid number that you would like to transfer")
        
        money = float(money)
        print("")

        if(xlira == "tl" and ylira == "usd"):
            if(self.isusd == True and money <= self.tl):
                self.tl -= money
                addmoney = money / 8.66
                self.usd += addmoney
                print(f"Current balance of {xlira.upper()}: {self.tl}, {ylira.upper()}: {self.usd}\n")
            else:
                self.checkBool(True, "TRY", self.isusd, "USD", self.tl, money) 
        elif(xlira == "tl" and ylira == "eur"):
            if(self.iseur == True and money <= self.tl):    
                self.tl -= money
                addmoney = money / 10.29
                self.eur += addmoney
                print(f"Current balance of {xlira.upper()}: {self.tl}, {ylira.upper()}: {self.eur}\n")
            else:
                self.checkBool(True, "TRY", self.iseur, "Euro", self.tl, money)    
        elif(xlira == "tl" and ylira == "gold"):
            if(self.isgold == True and money <= self.tl):     
                self.tl -= money
                addmoney = money / 500.29
                self.gold += addmoney
                print(f"Current balance of {xlira.upper()}: {self.tl}, {ylira.capitalize()}: {self.gold} gram(s)\n")

            else:
                self.checkBool(True, "TRY", self.isgold, "Gold", self.tl, money)     
        elif(xlira == "usd" and ylira == "tl"):
            if(self.isusd == True and money <= self.usd):    
                self.usd -= money
                addmoney = money * 8.66
                self.tl += addmoney
                print(f"Current balance of {xlira.upper()}: {self.usd}, {ylira.upper()}: {self.tl}\n") 
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
            print("Operation failed. Going back to the main screen\n") # fit that into conditions
            self.interface()
        
    def createCurrency(self):
        
        print("Please select an account to create\n")
        print("1. USD Account\n2. EUR Account\n3. Gold Account\n9. Return main screen\n")
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
                print("Euro account is created!\n")
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
        elif(go == "9"):
            self.interface()
        else: 
            print("Please type any respective number\n")
            self.createCurrency()
        
    def checkBool(self, bool1, m1, bool2, m2, unit, mny): # it works fine but when tl comes, it also show money amount even if 
        #.. an account doesn't exist
        bool3 = False
        if(unit <= mny):
            bool3 = True
        if(bool1 == False):
            print(f"You do NOT have {m1} account for exchange operations\n")
            bool3 = False
        if(bool2 == False):
            print(f"You do NOT have {m2} account for exchange operations\n") 
            bool3 = False
        if(bool3 == True):
            print(f"You do NOT have sufficient {m1} to exchange it with {m2}\n") 
        
    def nameCorrection(self):
        self.name = input("Name: ")
        print("")

        self.turnBack(self.name, self.menu)
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

        self.turnBack(self.sname, self.menu)
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
        
        self.turnBack(self.id, self.menu)
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

        self.turnBack(self.passw, self.menu)
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

    def currencyAccount(self, isusd, iseur, isgold):
        print("1. TRY account\n2. USD Account\n3. EUR Account\n4. Gold Account\n9. Return main screen\n")
        go = input("Go: ")
        print("")
            
        if(go == "1"):
            self.tryAccount()
        elif(go == "2"):
            if(self.isusd == True):
                self.usdAccount()
            else:
                print("You do NOT have US Dollar account to operate it.\n")
                self.interface()
        elif(go == "3"):
            if(self.iseur == True):
                self.eurAccount()
            else:
                print("You do NOT have Euro account to operate it.\n")
                self.interface()
        elif(go == "4"):
            if(self.isgold == True):    
                self.goldAccount()
            else:
                print("You do NOT have Gold account to operate it.\n")
                self.interface()
        elif(go == "9"):
            self.interface()
        else:
            self.currencyAccount(isusd, iseur, isgold)

    def payMoney(self, themoney, m1, m2):
        print("Please type the amount that you would like to deposit.\nType \"0\" to go back")
        themoney = 0
        increment = 0
        ismoney = False
        while(ismoney == False):
            try:
                increment = float(input(f"{m1}: "))
                if(isinstance(increment, float) and increment >= 0):
                    themoney += increment # program does not execute from this point and somehow throw exception
                    # problem is on the self. parameter
                    ismoney = True   
                else:
                    print("")
                    print("Please type a positive value to operate")
            except:
                print("")
                print("Please type numerical values only")
        
        if(increment != 0):
            print("")
            if(m1 == "TRY"):
                self.tl += themoney
                print(f"{m1} balance is updated as {self.tl} {m2}\n")
            elif(m1 == "USD"):
                self.usd += themoney
                print(f"{m1} balance is updated as {self.usd} {m2}\n")
            elif(m1 == "EUR"):
                self.eur += themoney
                print(f"{m1} balance is updated as {self.eur} {m2}\n")
        else:
            print("Returning back to the main screen")

    def withdrawMoney(self, themoney, m1, m2):
        print("Please type the amount that you would like to withdraw.\nType \"0\" to go back")
        themoney = 0
        decrement = 0
        ismoney = False
        while(ismoney == False):
            try:
                decrement = float(input(f"{m1}: "))
                if(isinstance(decrement, float) and decrement >= 0):
                    themoney += decrement
                    ismoney = True
                else:
                    print("")
                    print("Please type a positive value to operate")
            except:
                print("")
                print("Please type numerical values only")
        
        if(decrement != 0):
            print("")
            if(m1 == "TRY" and (self.tl - themoney >= 0)):
                self.tl -= themoney
                print(f"{m1} balance is updated as {self.tl} {m2}\n")
            elif(m1 == "USD" and (self.usd - themoney >= 0)):
                self.usd -= themoney
                print(f"{m1} balance is updated as {self.usd} {m2}\n")
            elif(m1 == "EUR" and (self.eur - themoney >= 0)):
                self.eur -= themoney
                print(f"{m1} balance is updated as {self.eur} {m2}\n")
            else:
                themoney += decrement # this is not necessarry
                print(f"You have insufficient currency to withdraw {decrement} {m2}.\nNo currency is withdrawn.\n")
        else:
            print("Returning back to the main screen")
        

#-----Execution-----#
exe = BankCore()
#exe.menu()
exe.interface() # for experimenting usages, some of the functions may not operate properly 
#-----Execution-----#
