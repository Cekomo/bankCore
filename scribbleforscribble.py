# I can code a method that ask for permission to the user after any operation about implementation 
# implement a structure that shows only existing accounts in that list (optional) interface --> go: 2   
# AS A MAIN PROBLEM THAT MUST BE SOLVED IMMIDIATELY, system does not save the values within same run, user should terminate..
#.. to make variables saved in SQL, even the users. All the operations can be done once, otherwise the code overwrites it.
# minimize transferInterface method after handling above problem

import mysql.connector
from mysql.connector.errors import DatabaseError

class BankCore:
    def __init__(self):
        
        self.mydb = mysql.connector.connect (
        database = "userinfo", # respective part for implementation
        host = "127.0.0.1",
        user = "root",
        password = "Bf27a96fae" )

        self.mycursor = self.mydb.cursor()

        self.mycursor.execute("Select * From users")
        self.database = self.mycursor.fetchall()

        self.userlist = []        
        self.idn = 0

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

        self.name =  ""
        self.sname = ""
        self.id =    ""
        self.passw = ""

        self.isusd = False
        self.iseur = False
        self.isgold = False
        
        self.users = {"name": "Cekomo", "surname": "\"Unknown\"", "id": "admin", "password": "admin"}
        

    print("Welcome to bankCore version Alpha(0.4)!\nPlase type regarding number for the next operation.\n")
  
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
        logbool = False

        for data in self.database: 
            if(data[3] == id and data[4] == passw): 
                self.idn = data[0] - 1
                print("Logged in.")
                print("Greetings dear {}, please type respective number to operate\n".format(data[1].capitalize()))
                self.interface(self.idn)
                logbool = True
        if logbool == False:
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
        # self.users 
        # self.users = {"name": name.capitalize(), "surname": sname.capitalize(), "id": id, "password": passw}
        
        for data in self.database:
            cid = data[0] + 1

        values = (cid, name, sname, id, passw, "0", "0", "0", "0", "0", "0", "0")
        sql = "INSERT INTO users(idusers, uname, sname, id, passw, tl, usd, eur, gold, isusd, iseur, isgold) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.mycursor.execute(sql, values)
        
        try:
            self.mydb.commit()
        except mysql.connector.Error as err:
            print("MySQL server does not respond: ", err)
         
        # there were essential variables that equal "0"
        # return self.users
        
    def printUser(self): # it will crash for out of range if id sequence corrupts (i.e idusers jumps from 5 to 8) 
        print("Informations of the user are listed.")
        
        print("Name: {}\nSurname: {}\nIdentity number: {}\nPassword: {}\n".format(self.userlist[1], self.userlist[2], self.userlist[3], self.userlist[4]))

    def interface(self, idd):
        
        self.mydb = mysql.connector.connect (
        database = "userinfo", # respective part for implementation
        host = "127.0.0.1",
        user = "root",
        password = "Bf27a96fae" )
        
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("Select * From users")
        self.database = self.mycursor.fetchall()
        
        for data in self.database[self.idn]: # as far as i understand, it checks respective row everytime for interface access
            self.userlist.append(data)
        
        self.name = self.userlist[1]; self.sname = self.userlist[2]; self.id = self.userlist[3]; self.passw = self.userlist[4]
        self.tl = float(self.userlist[5]); self.usd = float(self.userlist[6]); self.eur = float(self.userlist[7]); self.gold = float(self.userlist[8])
        self.isusd = self.userlist[9]; self.iseur = self.userlist[10]; self.isgold = self.userlist[11] 

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
            print("Please choose a currency type to send\n\n1. TRY\n2. USD\n3. EUR\n")
            self.transferInterface()

        elif(go == "5"):
            self.currencyExchange()

        elif(go == "9"):
            print("Ight, Imma Head Out.\n")
            self.menu() 

        else:
            self.interface(self.idn)
        
        self.interface(self.idn) # after deposit and withdrawing, it doesn't return interface so this is added. check it

    def account(self, mny, mnyU, mnyL, idd):
        mny
        print(f"1. Display currency amount\n2. Deposit {mnyU}\n3. Withdraw {mnyU}\n9. Return main screen\n")
        go = input("Go: ")
        print("")                  

        if(go == "1"):
            print("Dear {}, you have {} {} in your {} account.\n".format(self.userlist[1], str('%.2f'%self.userlist[mny]), mnyL + "(s)", mnyU)) 
        elif(go == "2"):
            self.payMoney(mny, mnyU, mnyL)         
        elif(go == "3"): 
            self.withdrawMoney(mny, mnyU, mnyL)
        elif(go == "9"):
            self.interface(self.idn)
        else:
            print("Please type any respective number to operate\n")            
            self.account(mny, mnyU, mnyL, idd) 

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
            sgoldtl = self.goldtotl - 1.2 
            sgoldusd = self.goldtousd - 0.14
            sgoldeur = self.goldtoeur - 0.12
            print(f"Purchase price of gold is:\nTRY: {'%.2f'%sgoldtl}\nUSD: {'%.2f'%sgoldusd}\nEUR: {'%.2f'%sgoldeur}\n") 
            # numbers are arbitrary
        elif(go == "9"):
            self.interface(self.idn)
        else:
            print("Please type any respective number to operate\n")
            self.goldAccount()

    def currencyExchange(self): 
        self.tl, self.usd, self.eur, self.gold 

        if(self.isusd or self.iseur or self.isgold): # this statement provides direct exit if no account is created
            print("Please state the currency that you will give.")
            self.islira = False
            while(self.islira == False): 
                xlira = input("try / usd / eur / gold: ")
                print("")
                if((xlira == "try" and self.tl > 0) or (xlira == "usd" and self.isusd and self.usd > 0) or (xlira == "eur" and self.iseur and self.eur > 0) or (xlira == "gold" and self.isgold and self.gold > 0)):
                    self.islira = True
                elif((xlira == "usd" and self.isusd == False) or (xlira == "eur" and self.iseur == False) or (xlira == "gold" and self.isgold == False)):
                    print(f"Since there is no created {xlira.upper()} account, currency exchange operation is not possible\n")
                    self.interface(self.idn)
                elif((xlira == "try" and self.tl == 0) or (xlira == "usd" and self.usd == 0) or (xlira == "eur" and self.eur == 0) or (xlira == "gold" and self.gold == 0)):
                    print(f"Since you have no currency to exchange in your {xlira.upper()} account, currency exchange operation is not possible\n")
                    self.interface(self.idn)
                else:
                    print("Please pick one of the currency methods that are stated")
            
            print("Please state the currency that you will get.")
            self.islira = False
            while(self.islira == False):
                ylira = input("try / usd / eur / gold: ")
                print("")
                if(ylira == "try" or (ylira == "usd" and self.isusd) or (ylira == "eur" and self.iseur) or (ylira == "gold" and self.isgold)):
                    self.islira = True
                elif((ylira == "usd" and self.isusd == False) or (ylira == "eur" and self.iseur == False) or (ylira == "gold" and self.isgold == False)):
                    print(f"Since there is no created {ylira.upper()} account, currency exchange operation is not possible\n")
                    self.interface(self.idn)
                else:
                    print("Please pick one of the currency methods that are stated")  

            if(xlira == ylira):
                print("You can NOT exchange money between same accounts. Plase type responding currency methods again\n")
                self.currencyExchange()
            else:
                print(f"Please type the amount of {xlira.upper()} that you would like to exchange to {ylira.upper()}:\n")
            
            if(xlira == "try" and ylira == "usd"): # printing asset and exchange ratios respecting currency input 
                if(self.isusd == True):              
                    self.printAsset(self.tl, "TRY", self.usd, "USD", self.tltousd)
            elif(xlira == "try" and ylira == "eur"):
                if(self.iseur == True):    
                    self.printAsset(self.tl, "TRY", self.eur, "EUR", self.tltoeur)
            elif(xlira == "try" and ylira == "gold"):
                if(self.isgold == True):
                    self.printAsset(self.tl, "TRY", self.gold, "Gold", self.tltogold)
            elif(xlira == "usd" and ylira == "try"):
                if(self.isusd == True):
                    self.printAsset(self.usd, "USD", self.tl, "TRY", self.usdtotl)
            elif(xlira == "usd" and ylira == "eur"):
                if(self.isusd == True and self.iseur == True):
                    self.printAsset(self.usd, "USD", self.eur, "EUR", self.usdtoeur)
            elif(xlira == "usd" and ylira == "gold"):
                if(self.isusd == True and self.isgold == True):
                    self.printAsset(self.usd, "USD", self.gold, "Gold", self.usdtogold)
            elif(xlira == "eur" and ylira == "try"):
                if(self.iseur == True):
                    self.printAsset(self.eur, "EUR", self.tl, "TRY", self.eurtotl)
            elif(xlira == "eur" and ylira == "usd"):
                if(self.iseur == True and self.isusd == True):
                    self.printAsset(self.eur, "EUR", self.usd, "USD", self.eurtousd)
            elif(xlira == "eur" and ylira == "gold"):
                if(self.iseur == True and self.isgold == True): 
                    self.printAsset(self.eur, "EUR", self.gold, "Gold", self.eurtogold)
            elif(xlira == "gold" and ylira == "try"):
                if(self.isgold == True):
                    self.printAsset(self.gold, "Gold", self.tl, "TRY", self.goldtotl)
            elif(xlira == "gold" and ylira == "usd"):
                if(self.isgold == True and self.isusd == True):  
                    self.printAsset(self.gold, "Gold", self.usd, "USD", self.goldtousd)      
            elif(xlira == "gold" and ylira == "eur"):
                if(self.isgold == True and self.iseur == True):
                    self.printAsset(self.gold, "Gold", self.eur, "EUR", self.goldtoeur)
            
            self.islira = False
            while(self.islira == False): # money input and control mechanism
                try:    
                    print("Type \"0\" to go back to main screen")
                    money = float(input(f"{xlira.upper()} to {ylira.upper()} with the amount of: "))
                    if(isinstance(money, float) and money > 0):
                        self.islira = True
                    elif(money == 0):
                        print("\nReturning main screen\n")
                        self.islira = True
                        self.interface(self.idn)
                    else:
                        print("Negative amounts are NOT allowed to be exchanged, please try again (press \"0\" to leave)\n")
                except:
                    print(f"Please type valid value to exchange {xlira.upper()} with {ylira.upper()}")        

            print("")        

            if(xlira == "try" and ylira == "usd"):
                if(self.isusd == True and money <= self.tl):              
                    self.tl -= money
                    addmoney = money * self.tltousd
                    self.usd += addmoney
                    self.insertSQL(self.tl, self.usd, "tl", "usd")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.tl} | {ylira.upper()}: {'%.2f'%self.usd}\n")
                else:
                    self.checkBool(True, "TRY", self.isusd, "USD", self.tl, money) 
            elif(xlira == "try" and ylira == "eur"):
                if(self.iseur == True and money <= self.tl):                
                    self.tl -= money
                    addmoney = money * self.tltoeur
                    self.eur += addmoney
                    self.insertSQL(self.tl, self.eur, "tl", "eur")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.tl} | {ylira.upper()}: {'%.2f'%self.eur}\n")
                else:
                    self.checkBool(True, "TRY", self.iseur, "Euro", self.tl, money)    
            elif(xlira == "try" and ylira == "gold"):
                if(self.isgold == True and money <= self.tl):     
                    self.tl -= money
                    addmoney = money * self.tltogold
                    self.gold += addmoney
                    self.insertSQL(self.tl, self.gold, "tl", "gold")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.tl} | {ylira.capitalize()}: {'%.2f'%self.gold} gram(s)\n")
                else:
                    self.checkBool(True, "TRY", self.isgold, "Gold", self.tl, money)     
            elif(xlira == "usd" and ylira == "try"):
                if(self.isusd == True and money <= self.usd):    
                    self.usd -= money
                    addmoney = money * self.usdtotl
                    self.tl += addmoney
                    self.insertSQL(self.usd, self.tl, "usd", "tl")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.usd} | {ylira.upper()}: {'%.2f'%self.tl}\n") 
                else:
                    self.checkBool(self.isusd, "USD", True, "TRY", self.usd, money)        
            elif(xlira == "usd" and ylira == "eur"):
                if(self.isusd == True and self.iseur == True and money <= self.usd):
                    self.usd -= money
                    addmoney = money * self.usdtoeur
                    self.eur += addmoney  
                    self.insertSQL(self.usd, self.eur, "usd", "eur")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.usd} | {ylira.upper()}: {'%.2f'%self.eur}\n")
                else:
                    self.checkBool(self.isusd, "USD", self.iseur, "Euro", self.usd, money) 
            elif(xlira == "usd" and ylira == "gold"):
                if(self.isusd == True and self.isgold == True and money <= self.usd):   
                    self.usd -= money
                    addmoney = money * self.usdtogold
                    self.gold += addmoney  
                    self.insertSQL(self.usd, self.gold, "usd", "gold")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.usd} | {ylira.capitalize()}: {'%.2f'%self.gold} gram(s)\n") 
                else:
                    self.checkBool(self.isusd, "USD", self.isgold, "Gold", self.usd, money)          
            elif(xlira == "eur" and ylira == "try"):
                if(self.iseur == True and money <= self.eur):    
                    self.eur -= money
                    addmoney = money * self.eurtotl
                    self.tl += addmoney     
                    self.insertSQL(self.eur, self.tl, "eur", "tl")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.eur} | {ylira.upper()}: {'%.2f'%self.tl}\n")
                else:
                    self.checkBool(self.iseur, "Euro", True, "TRY", self.eur, money)   
            elif(xlira == "eur" and ylira == "usd"):
                if(self.iseur == True and self.isusd == True and money <= self.eur):    
                    self.eur -= money
                    addmoney = money * self.eurtousd
                    self.usd += addmoney
                    self.insertSQL(self.eur, self.usd, "eur", "usd")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.eur} | {ylira.upper()}: {'%.2f'%self.usd}\n")
                else:
                    self.checkBool(self.iseur, "Euro", self.isusd, "USD", self.eur, money) 
            elif(xlira == "eur" and ylira == "gold"):
                if(self.iseur == True and self.isgold == True and money <= self.eur):    
                    self.eur -= money
                    addmoney = money * self.eurtogold
                    self.gold += addmoney  
                    self.insertSQL(self.eur, self.gold, "eur", "gold")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.eur} | {ylira.capitalize()}: {'%.2f'%self.gold} gram(s)\n")  
                else:
                    self.checkBool(self.iseur, "Euro", self.isgold, "Gold", self.eur, money)    
            elif(xlira == "gold" and ylira == "try"):
                if(self.isgold == True and money <= self.gold):    
                    self.gold -= money
                    addmoney = money * self.goldtotl
                    self.tl += addmoney  
                    self.insertSQL(self.gold, self.tl, "gold", "tl")
                    print(f"Current balance is updated as | {xlira.capitalize()}: {'%.2f'%self.gold} gram(s) | {ylira.upper()}: {'%.2f'%self.tl}\n")
                else:
                    self.checkBool(self.isgold, "Gold", True, "TRY", self.gold, money)
            elif(xlira == "gold" and ylira == "usd"):
                if(self.isgold == True and self.isusd == True and money <= self.gold):    
                    self.gold -= money
                    addmoney = money * self.goldtousd
                    self.usd += addmoney  
                    self.insertSQL(self.gold, self.usd, "gold", "usd")
                    print(f"Current balance is updated as | {xlira.capitalize()}: {'%.2f'%self.gold} gram(s) | {ylira.upper()}: {'%.2f'%self.usd}\n")
                else:
                    self.checkBool(self.isgold, "Gold", self.isusd, "USD", self.gold, money)        
            elif(xlira == "gold" and ylira == "eur"):
                if(self.isgold == True and self.iseur == True and money <= self.gold):    
                    self.gold -= money
                    addmoney = money * self.goldtoeur
                    self.eur += addmoney 
                    self.insertSQL(self.gold, self.eur, "gold", "eur") 
                    print(f"Current balance is updated as | {xlira.capitalize()}: {'%.2f'%self.gold} gram(s) | {ylira.upper()}: {'%.2f'%self.eur}\n")  
                else:
                    self.checkBool(self.isgold, "Gold", self.iseur, "Euro", self.gold, money)  
            else:
                print("Operation failed. Going back to the main screen\n") # fit that into conditions
                self.interface(self.idn)
                
            try:
                self.mydb.commit()
            except mysql.connector.Error as err:
                print("There is an error of ", err)
            finally:
                self.mydb.close()

        else:
            print("You do NOT have any created account to exchange currency\n")
    # ----------------- exchangeCurrency method ends here ------------------- #

    def createCurrency(self):  
        self.isusd, self.iseur, self.isgold 
        if(self.isusd == False or self.iseur == False or self.isgold == False):     
            print("Please select respective number to create currency account\n")
            print("1. USD Account\n2. EUR Account\n3. Gold Account\n9. Return main screen\n")
            go = input("Go: ")
            print("")
        
        
            if(go == "1" and self.isusd == True):
                print("Your USD account is already created\n")
            elif(go == "1"):
                psw = input("Please type your password to create a USD balance: ")
                print("")
                if(psw == self.passw):
                    self.isusd = True
                    print("USD account is created!\n")
                    idu = self.idn + 1
                    sql = f"Update users Set isusd = {self.isusd} where idusers = {idu}"
                    self.mycursor.execute(sql)
                else:
                    print("Password is incorrect, going back to main screen\n")
                    self.interface(self.idn)
            if(go == "2" and self.iseur == True):
                print("Your EUR account is already created\n")
            elif(go == "2"):
                psw = input("Please type your password to create a EUR balance: ")
                print("")
                if(psw == self.passw):
                    self.iseur = True
                    idu = self.idn + 1
                    sql = f"Update users Set iseur = {self.iseur} where idusers = {idu}"
                    self.mycursor.execute(sql)
                    print("Euro account is created!\n")
                else:
                    print("Password is incorrect, going back to main screen\n")
                    self.interface(self.idn)
            if(go == "3" and self.isgold == True):
                print("Your Gold account is already created\n")
            elif(go == "3"):
                psw = input("Please type your password to create a Gold account: ")
                print("")
                if(psw == self.passw):
                    self.isgold = True
                    idu = self.idn + 1         
                    sql = f"Update users Set isgold = {self.isgold} where idusers = {idu}"
                    self.mycursor.execute(sql)       
                    print("Gold account is created!\n")
                else:
                    print("Password is incorrect, going back to main screen\n")
                    self.interface(self.idn)
            if(go == "9"):
                self.interface(self.idn)
            if(go != "1" and go != "2" and go != "3" and go != "9"): 
                print("Your statement is invalid")
                self.createCurrency()
            
            try:
                self.mydb.commit()
            except mysql.connector.Error as err:
                print("There is an error of ", err)
            finally:
                self.mydb.close()
        
        else:
            print("You have already all the accounts\nNo account available to create\n")
        
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
        specialChar = ["!","'","^","+","%","&","/","(",")","=","?","_","-","*","|","\"","}","]","[","{","½","$","#","£",">","<",":",".","`",";",",","<","é","æ","ß","@","€","¨","~","´","\\"]
        isuser = True
        
        if(len(self.name) > 13 or len(self.name) < 2):
            isuser = False
            print("Your name can NOT be less than two and more than thirteen characters\n")
        elif any(char.isdigit() for char in self.name): 
            isuser = False
            print("Your name can NOT have digit(s)\n")
        elif any(char in specialChar for char in self.name):
            isuser = False
            print("Your name can NOT have special character(s)\n")
        if(isuser == True):
            return isuser
        else:
            self.nameCorrection()

    def snameCorrection(self):
        self.sname = input("Surname: ")
        print("")

        self.turnBack(self.sname, self.menu)
        specialChar = ["!","'","^","+","%","&","/","(",")","=","?","_","-","*","|","\"","}","]","[","{","½","$","#","£",">","<",":",".","`",";",",","<","é","æ","ß","@","€","¨","~","´","\\"]
        isuser = True
        if(len(self.sname) > 15 or len(self.sname) < 2):
            isuser = False
            print("Your name can NOT be less than three and more than thirteen characters\n")
        elif any(char.isdigit() for char in self.sname): 
            isuser = False
            print("Your surname can NOT have digit(s)\n")
        elif any(char in specialChar for char in self.sname): # that is general usage
            isuser = False
            print("Your surname can NOT have special character(s)\n")
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

        specialChar = ["!","'","^","+","%","&","/","(",")","=","?","_","-","*","|","\"","}","]","[","{","½","$","#","£",">","<",":",".","`",";",",","<","é","æ","ß","@","€","¨","~","´","\\"]

        self.turnBack(self.passw, self.menu)
        isuser = True
        if(len(self.passw) > 15 or len(self.passw) < 8):
            isuser = False
            print("Your password can NOT be less than eigth and more than fifteen characters\n")
        elif any(char in specialChar for char in self.passw): # that is general usage
            isuser = False
            print("Your password can NOT have special character(s)\n")
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
            self.account(5, "TRY", "lira", self.idn)
        elif(go == "2"):
            if(self.isusd == True):
                self.account(6, "USD", "dollar", self.idn)
            else:
                print("You do NOT have US Dollar account to operate it.\n")
                self.interface(self.idn)
        elif(go == "3"):
            if(self.iseur == True):
                self.account(7, "EUR", "euro", self.idn)
            else:
                print("You do NOT have Euro account to operate it.\n")
                self.interface(self.idn)
        elif(go == "4"):
            if(self.isgold == True):    
                self.goldAccount()
            else:
                print("You do NOT have Gold account to operate it.\n")
                self.interface(self.idn)
        elif(go == "9"):
            self.interface(self.idn)
        else:
            self.currencyAccount(isusd, iseur, isgold)

    def payMoney(self, themoney, m1, m2):
        print("Please type the amount that you would like to deposit\nType \"0\" to go back")
        themoney = 0
        increment = 0
        ismoney = False
        while(ismoney == False):
            try:
                increment = float(input(f"{m1}: "))
                print("")
                if(isinstance(increment, float) and increment >= 0):
                    themoney += increment 
                    ismoney = True   
                else:
                    print("Please type a positive value to operate")
            except:
                print("")
                print("Please type numerical values only")
        
        idu = self.idn + 1
        if(increment != 0): 
            if(m1 == "TRY"):
                self.tl += themoney
                idu = self.idn + 1
                sql = f"Update users Set tl = {self.tl} where idusers = {idu}"
                self.mycursor.execute(sql)
                print(f"{m1} balance is updated as {'%.2f'%self.tl} {m2}\n")
            elif(m1 == "USD"):
                self.usd += themoney
                sql = f"Update users Set usd = {self.usd} where idusers = {idu}"
                self.mycursor.execute(sql)
                print(f"{m1} balance is updated as {'%.2f'%self.usd} {m2}\n")
            elif(m1 == "EUR"):
                self.eur += themoney
                sql = f"Update users Set eur = {self.eur} where idusers = {idu}"
                self.mycursor.execute(sql)
                print(f"{m1} balance is updated as {'%.2f'%self.eur} {m2}\n")
                
            try:
                self.mydb.commit()
            except mysql.connector.Error as err:
                print("There is an error of ", err)
            finally:
                self.mydb.close()

        else:
            print("Returning back to the main screen\n")

        

    def withdrawMoney(self, themoney, m1, m2):
        if(themoney == 0):
            print(f"There is no currency to withdraw in your {m1} account\n")
            self.interface(self.idn)
        else:   
            print("Please type the amount that you would like to withdraw\nType \"0\" to go back")
            themoney = 0
            decrement = 0
            ismoney = False
            while(ismoney == False):
                try:
                    decrement = float(input(f"{m1}: "))
                    print("")
                    if(isinstance(decrement, float) and decrement > 0):
                        themoney += decrement
                        ismoney = True
                    else:           
                        print("Please type a positive value to operate")
                except:
                    print("")
                    print("Please type numerical values only")
            
            if(decrement != 0):
                if(m1 == "TRY" and (self.tl - themoney >= 0)):
                    self.tl -= themoney
                    idu = self.idn + 1
                    sql = f"Update users Set tl = {self.tl} where idusers = {idu}"
                    self.mycursor.execute(sql)
                    print(f"{m1} balance is updated as {'%.2f'%self.tl} {m2}\n")
                elif(m1 == "USD" and (self.usd - themoney >= 0)):
                    self.usd -= themoney
                    idu = self.idn + 1
                    sql = f"Update users Set tl = {self.tl} where idusers = {idu}"
                    self.mycursor.execute(sql)
                    print(f"{m1} balance is updated as {'%.2f'%self.usd} {m2}\n")
                elif(m1 == "EUR" and (self.eur - themoney >= 0)):
                    self.eur -= themoney
                    idu = self.idn + 1
                    sql = f"Update users Set tl = {self.tl} where idusers = {idu}"
                    self.mycursor.execute(sql)
                    print(f"{m1} balance is updated as {'%.2f'%self.eur} {m2}\n")
                else:
                    themoney += decrement # this is not necessarry
                    print(f"You have insufficient currency to withdraw {'%.2f'%decrement} {m2}.\nNo currency is withdrawn.\n")
                
                try:
                    self.mydb.commit()
                except mysql.connector.Error as err:
                    print("There is an error of ", err)
                finally:
                    self.mydb.close()

            else:
                print("Returning back to the main screen")
        
    def printAsset(self, assMoney1, assMny1, assMoney2, assMny2, excRatio):
        print(f"Your asset in {assMny1} and {assMny2} accounts:")
        print(f"|    {assMny1}: {'%.2f'%assMoney1}    |    {assMny2}: {'%.2f'%assMoney2}    |") 
        print(f"Exchange ratio of", end = " ") 
        print(f"{assMny1} to {assMny2}: {'%.5f'%excRatio}\n")  

    def insertSQL(self, mny2, mny4, mny1, mny3):
        idu = self.idn + 1
        sql1 = f"Update users Set {mny1} = {mny2} where idusers = {idu}"
        self.mycursor.execute(sql1)
        sql2 = f"Update users Set {mny3} = {mny4} where idusers = {idu}"
        self.mycursor.execute(sql2)

    def transferInterface(self): # try to minimize this method
        # checkBalance variable is not working properly, i cant send currency for usd and eur
        if((self.tl > 0) or (self.isusd == True and self.usd > 0) or (self.iseur == True and self.eur > 0)):   
            go = input("Go: ")
            print("")  

            if(go == "1" or go == "2" or go == "3"):
                if(go == "1" and self.tl > 0):
                    idu = self.idn + 1
                    print("Please type type identity number of the user to send TRY")
                    toUser = input("Identity Number: ")
                    print("")
                    
                    bool = False
                    for data in self.database:
                        if(toUser == str(data[3])):
                            bool = True
                            ismoney = False
                            while(ismoney == False):
                                try:
                                    sendMoney = float(input("TRY: "))
                                    print("")
                                    if(isinstance(sendMoney, float) and sendMoney >= 0):
                                        ismoney = True
                                    else:           
                                        print("Please type a positive value to operate")
                                except:
                                    print("")
                                    print("Please type numerical values only")
                            if(sendMoney != 0):
                                if(sendMoney <= self.tl):
                                    self.tl -= sendMoney
                                    sql1 = f"Update users Set tl = {self.tl} where idusers = {idu}"
                                    self.mycursor.execute(sql1)
                                    self.mycursor.execute(f"Select tl from users where id = {data[3]}")
                                    sentMoney = self.mycursor.fetchone()
                                    print(f"{sendMoney} lira(s) is sent successfully\n")
                                    senMoney = "%s" % (sentMoney)
                                    sendMoney += float(senMoney) 
                                    sql2 = f"Update users Set tl = {sendMoney} where id = {data[3]}"
                                    self.mycursor.execute(sql2)
                                else:
                                    print("Your balance is not enough to transfer\n")
                                    self.interface(self.idn)
                            else:
                                print("Going back to the main screen\n")
                                self.interface(self.idn)
                                
                    if(bool == False):
                        print("There is no such registered identity number\n")
                        self.interface(self.idn)

                elif(go == "2" and self.usd > 0 and self.isusd == True):
                    idu = self.idn + 1
                    print("Please type type identity number of the user to send USD")
                    toUser = input("Identity Number: ")
                    print("")

                    bool = False
                    for data in self.database:
                        if(toUser == str(data[3])):
                            self.mycursor.execute(f"Select isusd from users where id = {data[3]}")
                            checkBalance = self.mycursor.fetchone()
                            bool = True
                            ismoney = False
                            if(str(checkBalance) == "(1,)"): # couldn't convert checkBalance boolean, found a way like this
                                while(ismoney == False):
                                    try:
                                        sendMoney = float(input("USD: "))
                                        print("")
                                        if(isinstance(sendMoney, float) and sendMoney >= 0):
                                            ismoney = True
                                        else:           
                                            print("Please type a positive value to operate")
                                    except:
                                        print("")
                                        print("Please type numerical values only")
                                
                                if(sendMoney != 0):
                                    if(sendMoney <= self.usd):
                                        self.usd -= sendMoney
                                        sql1 = f"Update users Set usd = {self.usd} where idusers = {idu}"
                                        self.mycursor.execute(sql1)
                                        self.mycursor.execute(f"Select usd from users where id = {data[3]}")
                                        sentMoney = self.mycursor.fetchone()
                                        print(f"{sendMoney} dollar(s) is sent successfully\n")
                                        senMoney = "%s" % (sentMoney) # I apply this structure first
                                        sendMoney += float(senMoney) 
                                        sql2 = f"Update users Set usd = {sendMoney} where id = {data[3]}"
                                        self.mycursor.execute(sql2)
                                    else:
                                        print("Your balance is not enough to transfer\n")
                                        self.interface(self.idn)
                                else:
                                    print("Going back to the main screen\n")
                                    self.interface(self.idn)
                            else:
                                print("Respective user do NOT have USD account to accept any balance\n")
                                self.interface(self.idn)
                    if(bool == False):
                        print("There is no such registered identity number\n")
                        self.interface(self.idn)
                    elif(str(checkBalance) != "(1,)"):
                        print("Respective user does NOT have USD account to accept currency\n")

                elif(go == "3" and self.eur > 0 and self.iseur == True):
                    idu = self.idn + 1
                    print("Please type type identity number of the user to send EUR")
                    toUser = input("Identity Number: ")
                    print("")
                    bool = False
                    for data in self.database:
                        if(toUser == str(data[3])):
                            self.mycursor.execute(f"Select iseur from users where id = {data[3]}")
                            checkBalance = self.mycursor.fetchone()
                            bool = True
                            ismoney = False
                            if(str(checkBalance) == "(1,)"):
                                while(ismoney == False):
                                    try:
                                        sendMoney = float(input("EUR: "))
                                        print("")
                                        if(isinstance(sendMoney, float) and sendMoney >= 0):
                                            ismoney = True
                                        else:           
                                            print("Please type a positive value to operate")
                                    except:
                                        print("")
                                        print("Please type numerical values only")

                                if(sendMoney != 0):
                                    if(sendMoney <= self.eur):
                                        self.eur -= sendMoney
                                        sql1 = f"Update users Set eur = {self.eur} where idusers = {idu}"
                                        self.mycursor.execute(sql1)
                                        self.mycursor.execute(f"Select eur from users where id = {data[3]}")
                                        sentMoney = self.mycursor.fetchone()
                                        print(f"{sendMoney} euro(s) is sent successfully\n")
                                        senMoney = "%s" % (sentMoney)
                                        sendMoney += float(senMoney) 
                                        sql2 = f"Update users Set eur = {sendMoney} where id = {data[3]}"
                                        self.mycursor.execute(sql2)
                                    else:
                                        print("Your balance is not enough to transfer\n")
                                        self.interface(self.idn)
                                else:
                                    print("Going back to the main screen\n")
                                    self.interface(self.idn)
                            else:
                                print("Respective user do NOT have EUR account to accept any balance\n")
                                self.interface(self.idn)
                    if(bool == False):
                        print("There is no such registered identity number\n")
                        self.interface(self.idn)
                    elif(str(checkBalance) != "(1,)"):
                        print("Respective user does NOT have EUR account to accept currency\n")
                        
        else:
            print("There is no money in any of your currency account to transfer\nGoing back to the main screen\n")
            self.interface(self.idn)
    
        try:
            self.mydb.commit()
        except mysql.connector.Error as err:
            print("There is an error of ", err)
        finally:
            self.mydb.close()

#-----Execution-----#

exe = BankCore()
exe.menu() # this is the main program 
# exe.interface(0) # for experimenting usages, some of the functions may not operate properly 
# exe.currencyExchange() # for experimenting usages, some of the functions may not operate properly 

#-----Execution-----#
