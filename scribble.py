# I can code a method that ask for permission to the user after any operation about implementation 
# implement a structure that shows only existing accounts in that list (optional) interface --> go: 2
# even if the account is created, it still prints about creation of account
# spaces are adjusted by considering decimals of exchange ratios, for instance if eurtotl decreases more, need to be adjusted again..
# ..for display of user's asset and exchange ratios, I can code a structure that only shows related components of exchange..
# i.e for TRY to USD, try and usd assets and their ratios 
# even if the things can become messy in currencyExchange method, this method can be merged and save up hundreds lines of codes

class BankCore:
    def __init__(self):
        self.tl = 0
        self.usd = 0
        self.eur = 0
        self.gold = 0

        # variables to change exchange ratios dynamically for exchanceCurrency method 
        self.tltousd = 0.117
        self.usdtotl = 8.524
        self.tltoeur = 0.0994
        self.eurtotl = 10.064
        self.tltogold = 0.002016
        self.goldtotl = 496.052
        self.usdtoeur = 0.847
        self.eurtousd = 1.1806
        self.goldtousd = 58.2916
        self.usdtogold = 0.017155
        self.goldtoeur = 49.3588
        self.eurtogold = 0.02026

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

    def account(self, mny, mnyU, mnyL):
        mny
        print(f"1. Display currency amount\n2. Deposit {mnyU}\n3. Withdraw {mnyU}\n9. Return main screen\n")
        go = input("Go: ")
        print("")

        if(go == "1"):
            print("Dear {}, you have {} {} in your {} account.\n".format(self.users["name"], str('%.2f'%mny), mnyL + "(s)", mnyU)) 

        elif(go == "2"):
            self.payMoney(mny, mnyU, mnyL)         

        elif(go == "3"): 
            self.withdrawMoney(mny, mnyU, mnyL)

        elif(go == "9"):
            self.interface()
        else:
            print("Please type any respective number to operate\n")            
            self.account(mny, mnyU, mnyL) 

    def goldAccount(self):
        self.gold
        print("Gold purchasing and sale operations are conducted in currency exchange tab\n")
        print("1. Display gold amount\n2. Gold stock sale price\n3. Gold stock puchasing price\n9. Return main screen\n")
        go = input("Go: ")
        print("")

        if(go == "1"):
            print("Dear {}, you have {} gram(s) in your Gold account.\n".format(self.users["name"], str('%.4f'%self.gold))) 

        elif(go == "2"): 
            print(f"Sale price of gold is:\nTRY: {'%.2f'%self.goldtotl}\nUSD: {'%.2f'%self.goldtousd}\nEUR: {'%.2f'%self.goldtoeur}\n")    
            
            
        elif(go == "3"): 
            print(f"Purchase price of gold is:\nTRY: {'%.2f'%self.goldtotl-1.2}\nUSD: {'%.2f'%self.goldtousd-0.14}\nEUR: {'%.2f'%self.goldtoeur-0.12}\n") 
            # numbers are arbitrary

        elif(go == "9"):
            self.interface()
        else:
            print("Please type any respective number to operate\n")
            self.goldAccount()


    def currencyExchange(self): # even if the things can become messy, this method can be merged and save up hundreds lines of codes
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
            print(f"Please type the amount of {xlira.upper()} that you would like to exchange to {ylira.upper()}:\n")
        
        if(xlira == "tl" and ylira == "usd"):
            if(self.isusd == True):              
                self.printAsset(self.tl, "TRY", self.usd, "USD", self.tltousd)
        elif(xlira == "tl" and ylira == "eur"):
            if(self.iseur == True):    
                self.printAsset(self.tl, "TRY", self.eur, "EUR", self.tltoeur)
        elif(xlira == "tl" and ylira == "gold"):
            if(self.isgold == True):
                self.printAsset(self.tl, "TRY", self.gold, "Gold", self.tltogold)
        elif(xlira == "usd" and ylira == "tl"):
            if(self.isusd == True):
                self.printAsset(self.usd, "USD", self.tl, "TRY", self.usdtotl)
        elif(xlira == "usd" and ylira == "eur"):
            if(self.isusd == True and self.iseur == True):
                self.printAsset(self.usd, "USD", self.eur, "EUR", self.usdtoeur)
        elif(xlira == "usd" and ylira == "gold"):
            if(self.isusd == True and self.isgold == True):
                self.printAsset(self.usd, "USD", self.gold, "Gold", self.usdtogold)
        elif(xlira == "eur" and ylira == "tl"):
            if(self.iseur == True):
                self.printAsset(self.eur, "EUR", self.tl, "TRY", self.eurtotl)
        elif(xlira == "eur" and ylira == "usd"):
            if(self.iseur == True and self.isusd == True):
                self.printAsset(self.eur, "EUR", self.usd, "USD", self.eurtousd)
        elif(xlira == "eur" and ylira == "gold"):
            if(self.iseur == True and self.isgold == True): 
                self.printAsset(self.eur, "EUR", self.gold, "Gold", self.eurtogold)
        elif(xlira == "gold" and ylira == "tl"):
            if(self.isgold == True):
                self.printAsset(self.gold, "Gold", self.tl, "TRY", self.goldtotl)
        elif(xlira == "gold" and ylira == "usd"):
            if(self.isgold == True and self.isusd == True):  
                self.printAsset(self.gold, "Gold", self.usd, "USD", self.goldtousd)      
        elif(xlira == "gold" and ylira == "eur"):
            if(self.isgold == True and self.iseur == True):
                self.printAsset(self.gold, "Gold", self.eur, "EUR", self.goldtoeur)
        else:
            pass
        
        self.islira = False
        while(self.islira == False):
            try:    
                money = float(input(f"{xlira.upper()} to {ylira.upper()} with the amount of: "))
                if(isinstance(money, float) and money >= 0):
                    self.islira = True
                else:
                    print("Negative amounts are NOT allowed to be exchanged")
            except:
                print(f"Please type valid value to exchange {xlira.upper()} with {ylira.upper()}")        

        print("")        

        if(xlira == "tl" and ylira == "usd"):
            if(self.isusd == True and money <= self.tl):              
                self.tl -= money
                addmoney = money * self.tltousd
                self.usd += addmoney
                print(f"Current balance of {xlira.upper()}: {'%.2f'%self.tl}, {ylira.upper()}: {'%.2f'%self.usd}\n")
            else:
                self.checkBool(True, "TRY", self.isusd, "USD", self.tl, money) 
        elif(xlira == "tl" and ylira == "eur"):
            if(self.iseur == True and money <= self.tl):                
                self.tl -= money
                addmoney = money * self.tltoeur
                self.eur += addmoney
                print(f"Current balance of {xlira.upper()}: {'%.2f'%self.tl}, {ylira.upper()}: {'%.2f'%self.eur}\n")
            else:
                self.checkBool(True, "TRY", self.iseur, "Euro", self.tl, money)    
        elif(xlira == "tl" and ylira == "gold"):
            if(self.isgold == True and money <= self.tl):     
                self.tl -= money
                addmoney = money * self.tltogold
                self.gold += addmoney
                print(f"Current balance of {xlira.upper()}: {'%.2f'%self.tl}, {ylira.capitalize()}: {'%.4f'%self.gold} gram(s)\n")
            else:
                self.checkBool(True, "TRY", self.isgold, "Gold", self.tl, money)     
        elif(xlira == "usd" and ylira == "tl"):
            if(self.isusd == True and money <= self.usd):    
                self.usd -= money
                addmoney = money * self.usdtotl
                self.tl += addmoney
                print(f"Current balance of {xlira.upper()}: {'%.2f'%self.usd}, {ylira.upper()}: {'%.2f'%self.tl}\n") 
            else:
                self.checkBool(self.isusd, "USD", True, "TRY", self.usd, money)        
        elif(xlira == "usd" and ylira == "eur"):
            if(self.isusd == True and self.iseur == True and money <= self.usd):
                self.usd -= money
                addmoney = money * self.usdtoeur
                self.eur += addmoney  
                print(f"Current balance of {xlira.upper()}: {'%.2f'%self.usd}, {ylira.upper()}: {'%.2f'%self.eur}\n")
            else:
                self.checkBool(self.isusd, "USD", self.iseur, "Euro", self.usd, money) 
        elif(xlira == "usd" and ylira == "gold"):
            if(self.isusd == True and self.isgold == True and money <= self.usd):   
                self.usd -= money
                addmoney = money * self.usdtogold
                self.gold += addmoney  
                print(f"Current balance of {xlira.upper()}: {'%.2f'%self.usd}, {ylira.capitalize()}: {'%.4f'%self.gold} gram(s)\n") 
            else:
                self.checkBool(self.isusd, "USD", self.isgold, "Gold", self.usd, money)          
        elif(xlira == "eur" and ylira == "tl"):
            if(self.iseur == True and money <= self.eur):    
                self.eur -= money
                addmoney = money * self.eurtotl
                self.tl += addmoney     
                print(f"Current balance of {xlira.upper()}: {'%.2f'%self.eur}, {ylira.upper()}: {'%.2f'%self.tl}\n")
            else:
                self.checkBool(self.iseur, "Euro", True, "TRY", self.eur, money)   
        elif(xlira == "eur" and ylira == "usd"):
            if(self.iseur == True and self.isusd == True and money <= self.eur):    
                self.eur -= money
                addmoney = money * self.eurtousd
                self.usd += addmoney
                print(f"Current balance of {xlira.upper()}: {'%.2f'%self.eur}, {ylira.upper()}: {'%.2f'%self.usd}\n")
            else:
                self.checkBool(self.iseur, "Euro", self.isusd, "USD", self.eur, money) 
        elif(xlira == "eur" and ylira == "gold"):
            if(self.iseur == True and self.isgold == True and money <= self.eur):    
                self.eur -= money
                addmoney = money * self.eurtogold
                self.gold += addmoney  
                print(f"Current balance of {xlira.upper()}: {'%.2f'%self.eur}, {ylira.capitalize()}: {'%.4f'%self.gold} gram(s)\n")  
            else:
                self.checkBool(self.iseur, "Euro", self.isgold, "Gold", self.eur, money)    
        elif(xlira == "gold" and ylira == "tl"):
            if(self.isgold == True and money <= self.gold):    
                self.gold -= money
                addmoney = money * self.goldtotl
                self.tl += addmoney  
                print(f"Current balance of {xlira.capitalize()}: {'%.4f'%self.gold} gram(s), {ylira.upper()}: {'%.2f'%self.tl}\n")
            else:
                self.checkBool(self.isgold, "Gold", True, "TRY", self.gold, money)
        elif(xlira == "gold" and ylira == "usd"):
            if(self.isgold == True and self.isusd == True and money <= self.gold):    
                self.gold -= money
                addmoney = money * self.goldtousd
                self.usd += addmoney  
                print(f"Current balance of {xlira.capitalize()}: {'%.4f'%self.gold} gram(s), {ylira.upper()}: {'%.2f'%self.usd}\n")
            else:
                self.checkBool(self.isgold, "Gold", self.isusd, "USD", self.gold, money)        
        elif(xlira == "gold" and ylira == "eur"):
            if(self.isgold == True and self.iseur == True and money <= self.gold):    
                self.gold -= money
                addmoney = money * self.goldtoeur
                self.eur += addmoney  
                print(f"Current balance of {xlira.capitalize()}: {'%.4f'%self.gold} gram(s), {ylira.upper()}: {'%.2f'%self.eur}\n")  
            else:
                self.checkBool(self.isgold, "Gold", self.iseur, "Euro", self.gold, money)  
        else:
            print("Operation failed. Going back to the main screen\n") # fit that into conditions
            self.interface()
        
    def createCurrency(self):  
        print("Please select respective number to create currency account\n")
        print("1. USD Account\n2. EUR Account\n3. Gold Account\n9. Return main screen\n")
        go = input("Go: ")
        print("")

        self.isusd, self.iseur, self.isgold 
        if(go == "1" and self.isusd == True):
            print("Your USD account is already created\n")
        elif(go == "1"):
            psw = input("Please type your password to create a USD balance: ")
            print("")
            if(psw == self.users["password"]):
                self.isusd = True
                print("USD account is created!\n")
            else:
                print("Password is incorrect, going back to main screen\n")
                self.interface()
        if(go == "2" and self.iseur == True):
            print("Your EUR account is already created\n")
        elif(go == "2"):
            psw = input("Please type your password to create a EUR balance: ")
            print("")
            if(psw == self.users["password"]):
                self.iseur = True
                print("Euro account is created!\n")
            else:
                print("Password is incorrect, going back to main screen\n")
                self.interface()
        if(go == "3" and self.isgold == True):
            print("Your Gold account is already created\n")
        elif(go == "3"):
            psw = input("Please type your password to create a Gold account: ")
            print("")
            if(psw == self.users["password"]):
                self.isgold = True
                print("Gold account is created!\n")
            else:
                print("Password is incorrect, going back to main screen\n")
                self.interface()
        if(go == "9"):
            self.interface()
        if(go != "1" and go != "2" and go != "3" and go != "9"): 
            print("Your statement is invalid")
            self.createCurrency()
        
    def checkBool(self, bool1, m1, bool2, m2, unit, mny): 
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
            self.account(self.tl, "TRY", "lira")
        elif(go == "2"):
            if(self.isusd == True):
                self.account(self.usd, "USD", "dollar")
            else:
                print("You do NOT have US Dollar account to operate it.\n")
                self.interface()
        elif(go == "3"):
            if(self.iseur == True):
                self.account(self.eur, "EUR", "euro")
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
                    themoney += increment 
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
                print(f"{m1} balance is updated as {'%.2f'%self.tl} {m2}\n")
            elif(m1 == "USD"):
                self.usd += themoney
                print(f"{m1} balance is updated as {'%.2f'%self.usd} {m2}\n")
            elif(m1 == "EUR"):
                self.eur += themoney
                print(f"{m1} balance is updated as {'%.2f'%self.eur} {m2}\n")
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
                print(f"{m1} balance is updated as {'%.2f'%self.tl} {m2}\n")
            elif(m1 == "USD" and (self.usd - themoney >= 0)):
                self.usd -= themoney
                print(f"{m1} balance is updated as {'%.2f'%self.usd} {m2}\n")
            elif(m1 == "EUR" and (self.eur - themoney >= 0)):
                self.eur -= themoney
                print(f"{m1} balance is updated as {'%.2f'%self.eur} {m2}\n")
            else:
                themoney += decrement # this is not necessarry
                print(f"You have insufficient currency to withdraw {'%.2f'%decrement} {m2}.\nNo currency is withdrawn.\n")
        else:
            print("Returning back to the main screen")
        
    def printAsset(self, assMoney1, assMny1, assMoney2, assMny2, excRatio):
        print(f"Your asset in {assMny1} and {assMny2} accounts:")
        print(f"|    {assMny1}: {'%.2f'%assMoney1}    |    {assMny2}: {'%.2f'%assMoney2}    |") 
        print(f"Exchange ratio of", end = " ") 
        print(f"{assMny1} to {assMny2}: {'%.5f'%excRatio}\n")

#-----Execution-----#

exe = BankCore()
# exe.menu() # this is the main program 
exe.interface() # for experimenting usages, some of the functions may not operate properly 
# exe.currencyExchange() # for experimenting usages, some of the functions may not operate properly 

#-----Execution-----#
