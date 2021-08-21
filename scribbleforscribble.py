# implement a structure that shows only existing accounts in that list (optional) interface --> go: 2  
# i can limit minimum and maximum value for all money related methods

import json
import requests
import time
import mysql.connector
# from mysql.connector.errors import DatabaseError

class BankCore:
    def __init__(self):

        self.tl = 0 
        self.usd = 0 
        self.eur = 0
        self.gold = 0

        self.userlist = []        
        self.idn = 0

        # variables to change exchange ratios dynamically for exchanceCurrency method 
        # Source: "exchangeratesapi.io"
        apiURL = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=698d889676879382f142cb906f52f58b&format=1")
        apiURL = json.loads(apiURL.text) 
        
        # gold ratios are depended to ONS, not gr.; so, they are multiplied with 31.1034807
        self.tltousd = (1 / (apiURL["rates"]['TRY'])) * (apiURL["rates"]['USD'])
        self.usdtotl = (apiURL["rates"]['TRY']) * (1 / (apiURL["rates"]['USD']))
        self.tltoeur = 1 / (apiURL["rates"]['TRY'])
        self.eurtotl = apiURL["rates"]['TRY']
        self.tltogold = (apiURL["rates"]['XAU'] * 31.1034807) * (1 / (apiURL["rates"]['TRY']))
        self.goldtotl = (1 / (apiURL["rates"]['XAU'] * 31.1034807)) * apiURL["rates"]['TRY']
        self.usdtoeur = 1 / (apiURL["rates"]['USD'])
        self.eurtousd = apiURL["rates"]['USD']
        self.goldtousd = (apiURL["rates"]['USD']) * (1 / (apiURL["rates"]['XAU'] * 31.1034807))
        self.usdtogold = (apiURL["rates"]['XAU'] * 31.1034807) * (1 / (apiURL["rates"]['USD']))
        self.goldtoeur = 1 / (apiURL["rates"]['XAU'] * 31.1034807)
        self.eurtogold = apiURL["rates"]['XAU'] * 31.1034807 

        self.name =  ""
        self.sname = ""
        self.id =    ""
        self.passw = ""

        self.isusd = False
        self.iseur = False
        self.isgold = False
        

    print("Welcome to bankCore version Beta(1.9)!\nPlase type regarding number for the next operation.\n")
  
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
            quit()
        else:  
            print("Invalid input.\nPlease try again.\n")
            self.menu()

    def login(self):
        
        self.mydb = mysql.connector.connect (
        database = "userinfo", # respective part for implementation
        host = "127.0.0.1",
        user = "root",
        password = "Bf27a96fae" )

        self.mycursor = self.mydb.cursor()

        self.mycursor.execute("Select * From users")
        self.database = self.mycursor.fetchall()
        
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
                logbool = True
                       
                self.name = data[1]; self.sname = data[2]; self.id = data[3]; self.passw = data[4]
                self.isusd = data[9]; self.iseur = data[10]; self.isgold = data[11] 

                self.tl = float(data[5]) 
                self.usd = float(data[6]) 
                self.eur = float(data[7])
                self.gold = float(data[8])

                time.sleep(1)
                self.interface(self.idn)

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
        
    def printUser(self): 
        print("Informations of the user are listed.")
        time.sleep(0.2)
        print("Name: {}\nSurname: {}\nIdentity number: {}\nPassword: {}\n".format(self.name, self.sname, self.id, self.passw))
        time.sleep(2)

    def interface(self, idd):
        
        self.mydb = mysql.connector.connect (
        database = "userinfo", # respective part for implementation
        host = "127.0.0.1",
        user = "root",
        password = "Bf27a96fae" )
        
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("Select * From users")
        self.database = self.mycursor.fetchall()
        
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
            self.mydb.close()
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
            time.sleep(0.2)
            print("Dear {}, you have {} {} in your {} account.\n".format(self.name, str('%.2f'%mny), mnyL + "(s)", mnyU)) 
            time.sleep(2)
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

        time.sleep(0.2)
        if(go == "1"):
            print("Dear {}, you have {} gram(s) in your Gold account.\n".format(self.name, str('%.4f'%self.gold))) 
            time.sleep(2)
        elif(go == "2"): 
            print(f"Sale price of gold is:\nTRY: {'%.2f'%self.goldtotl}\nUSD: {'%.2f'%self.goldtousd}\nEUR: {'%.2f'%self.goldtoeur}\n")
            time.sleep(2)         
        elif(go == "3"): 
            sgoldtl = self.goldtotl - 1.2 
            sgoldusd = self.goldtousd - 0.14
            sgoldeur = self.goldtoeur - 0.12
            print(f"Purchase price of gold is:\nTRY: {'%.2f'%sgoldtl}\nUSD: {'%.2f'%sgoldusd}\nEUR: {'%.2f'%sgoldeur}\n") 
            # numbers are arbitrary
            time.sleep(2)
        elif(go == "9"):
            self.interface(self.idn)
        else:
            print("Please type any respective number to operate\n")
            self.goldAccount()


    def currencyExchange(self): 
        self.tl, self.usd, self.eur, self.gold 

        if(self.isusd or self.iseur or self.isgold): # this statement provides direct exit if no account is created
            print("Please state the currency that you will give.")
            time.sleep(0.2)
            self.islira = False
            while(self.islira == False): 
                xlira = input("try / usd / eur / gold: ")
                print("")
                if((xlira == "try" and self.tl > 0) or (xlira == "usd" and self.isusd and self.usd > 0) or (xlira == "eur" and self.iseur and self.eur > 0) or (xlira == "gold" and self.isgold and self.gold > 0)):
                    self.islira = True
                elif((xlira == "usd" and self.isusd == False) or (xlira == "eur" and self.iseur == False) or (xlira == "gold" and self.isgold == False)):
                    print(f"Since there is no created {xlira.upper()} account, currency exchange operation is not possible\n")
                    time.sleep(1)
                    self.interface(self.idn)
                elif((xlira == "try" and self.tl == 0) or (xlira == "usd" and self.usd == 0) or (xlira == "eur" and self.eur == 0) or (xlira == "gold" and self.gold == 0)):
                    print(f"Since you have no currency to exchange in your {xlira.upper()} account, currency exchange operation is not possible\n")
                    time.sleep(1)
                    self.interface(self.idn)
                else:
                    time.sleep(1)
                    print("Please pick one of the currency methods that are stated")
            
            print("Please state the currency that you will get.")
            time.sleep(0.2)
            self.islira = False
            while(self.islira == False):
                ylira = input("try / usd / eur / gold: ")
                print("")
                if(ylira == "try" or (ylira == "usd" and self.isusd) or (ylira == "eur" and self.iseur) or (ylira == "gold" and self.isgold)):
                    self.islira = True
                elif((ylira == "usd" and self.isusd == False) or (ylira == "eur" and self.iseur == False) or (ylira == "gold" and self.isgold == False)):
                    print(f"Since there is no created {ylira.upper()} account, currency exchange operation is not possible\n")
                    time.sleep(1)
                    self.interface(self.idn)
                else:
                    print("Please pick one of the currency methods that are stated")  
                    time.sleep(1)

            if(xlira == ylira):
                print("You can NOT exchange money between same accounts. Plase type responding currency methods again\n")
                time.sleep(1)
                self.currencyExchange()
            else:
                print(f"Please type the amount of {xlira.upper()} that you would like to exchange to {ylira.upper()}:\n")
                time.sleep(1)
            
            if(xlira == "try" and ylira == "usd"): # printing asset and exchange ratios respecting currency input 
                if(self.isusd == True):              
                    self.printAssets(self.tl, "TRY", self.usd, "USD", self.tltousd)
            elif(xlira == "try" and ylira == "eur"):
                if(self.iseur == True):    
                    self.printAssets(self.tl, "TRY", self.eur, "EUR", self.tltoeur)
            elif(xlira == "try" and ylira == "gold"):
                if(self.isgold == True):
                    self.printAssets(self.tl, "TRY", self.gold, "Gold", self.tltogold)
            elif(xlira == "usd" and ylira == "try"):
                if(self.isusd == True):
                    self.printAssets(self.usd, "USD", self.tl, "TRY", self.usdtotl)
            elif(xlira == "usd" and ylira == "eur"):
                if(self.isusd == True and self.iseur == True):
                    self.printAssets(self.usd, "USD", self.eur, "EUR", self.usdtoeur)
            elif(xlira == "usd" and ylira == "gold"):
                if(self.isusd == True and self.isgold == True):
                    self.printAssets(self.usd, "USD", self.gold, "Gold", self.usdtogold)
            elif(xlira == "eur" and ylira == "try"):
                if(self.iseur == True):
                    self.printAssets(self.eur, "EUR", self.tl, "TRY", self.eurtotl)
            elif(xlira == "eur" and ylira == "usd"):
                if(self.iseur == True and self.isusd == True):
                    self.printAssets(self.eur, "EUR", self.usd, "USD", self.eurtousd)
            elif(xlira == "eur" and ylira == "gold"):
                if(self.iseur == True and self.isgold == True): 
                    self.printAssets(self.eur, "EUR", self.gold, "Gold", self.eurtogold)
            elif(xlira == "gold" and ylira == "try"):
                if(self.isgold == True):
                    self.printAssets(self.gold, "Gold", self.tl, "TRY", self.goldtotl)
            elif(xlira == "gold" and ylira == "usd"):
                if(self.isgold == True and self.isusd == True):  
                    self.printAssets(self.gold, "Gold", self.usd, "USD", self.goldtousd)      
            elif(xlira == "gold" and ylira == "eur"):
                if(self.isgold == True and self.iseur == True):
                    self.printAssets(self.gold, "Gold", self.eur, "EUR", self.goldtoeur)
            
            self.islira = False
            while(self.islira == False): # money input and control mechanism
                bool = True
                try:    
                    print("Type \"0\" to go back to the main screen")
                    time.sleep(0.2)
                    money = float(input(f"{xlira.upper()} to {ylira.upper()} with the amount of: "))
                    if(isinstance(money, float) and money > 0):
                        self.islira = True
                    elif(money == 0):
                        print("\nReturning main screen")
                        time.sleep(0.2)
                        self.islira = True
                        bool = False
                    else:
                        print("Negative amounts are NOT allowed to be exchanged, please try again (press \"0\" to leave)\n")
                        time.sleep(1)
                except:
                    print(f"Please type valid value to exchange {xlira.upper()} with {ylira.upper()}") 
                    time.sleep(1)       

            print("")        

            if(bool == False): # I instantiate bool and make statement for the problem below
                # it connects from exchangeCurrency to permissionExchange even if the connection is closed, fix this
                self.interface(self.idn)
            elif(xlira == "try" and ylira == "usd"):
                if(self.isusd == True and money <= self.tl):              
                    self.tl -= money
                    addmoney = money * self.tltousd
                    self.usd += addmoney
                    self.exchangePermission(addmoney, "dollar(s)", "USD", money, "lira(s)")
                    self.insertSQL(self.tl, self.usd, "tl", "usd")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.tl} | {ylira.upper()}: {'%.2f'%self.usd} |\n")
                    time.sleep(2)  
                else:
                    self.checkBool(True, "TRY", self.isusd, "USD", self.tl, money) 
            elif(xlira == "try" and ylira == "eur"):
                if(self.iseur == True and money <= self.tl):                
                    self.tl -= money
                    addmoney = money * self.tltoeur
                    self.eur += addmoney
                    self.exchangePermission(addmoney, "euro(s)", "EUR", money, "lira(s)")
                    self.insertSQL(self.tl, self.eur, "tl", "eur")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.tl} | {ylira.upper()}: {'%.2f'%self.eur} |\n")
                    time.sleep(2)  
                else:
                    self.checkBool(True, "TRY", self.iseur, "Euro", self.tl, money)    
            elif(xlira == "try" and ylira == "gold"):
                if(self.isgold == True and money <= self.tl):     
                    self.tl -= money
                    addmoney = money * self.tltogold
                    self.gold += addmoney
                    self.exchangePermission(addmoney, "gram(s)", "Gold", money, "lira(s)")
                    self.insertSQL(self.tl, self.gold, "tl", "gold")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.tl} | {ylira.capitalize()}: {'%.2f'%self.gold} gram(s) |\n")
                    time.sleep(2)  
                else:
                    self.checkBool(True, "TRY", self.isgold, "Gold", self.tl, money)     
            elif(xlira == "usd" and ylira == "try"):
                if(self.isusd == True and money <= self.usd):    
                    self.usd -= money
                    addmoney = money * self.usdtotl
                    self.tl += addmoney
                    self.exchangePermission(addmoney, "lira(s)", "TRY", money, "dollar(s)")
                    self.insertSQL(self.usd, self.tl, "usd", "tl")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.usd} | {ylira.upper()}: {'%.2f'%self.tl} |\n") 
                    time.sleep(2)  
                else:
                    self.checkBool(self.isusd, "USD", True, "TRY", self.usd, money)        
            elif(xlira == "usd" and ylira == "eur"):
                if(self.isusd == True and self.iseur == True and money <= self.usd):
                    self.usd -= money
                    addmoney = money * self.usdtoeur
                    self.eur += addmoney  
                    self.exchangePermission(addmoney, "euro(s)", "EUR", money, "dollar(s)")
                    self.insertSQL(self.usd, self.eur, "usd", "eur")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.usd} | {ylira.upper()}: {'%.2f'%self.eur} |\n")
                    time.sleep(2)  
                else:
                    self.checkBool(self.isusd, "USD", self.iseur, "Euro", self.usd, money) 
            elif(xlira == "usd" and ylira == "gold"):
                if(self.isusd == True and self.isgold == True and money <= self.usd):   
                    self.usd -= money
                    addmoney = money * self.usdtogold
                    self.gold += addmoney  
                    self.exchangePermission(addmoney, "gram(s)", "Gold", money, "dollar(s)")
                    self.insertSQL(self.usd, self.gold, "usd", "gold")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.usd} | {ylira.capitalize()}: {'%.2f'%self.gold} gram(s) |\n") 
                    time.sleep(2)  
                else:
                    self.checkBool(self.isusd, "USD", self.isgold, "Gold", self.usd, money)          
            elif(xlira == "eur" and ylira == "try"):
                if(self.iseur == True and money <= self.eur):    
                    self.eur -= money
                    addmoney = money * self.eurtotl
                    self.tl += addmoney     
                    self.exchangePermission(addmoney, "lira(s)", "TRY", money, "euro(s)")
                    self.insertSQL(self.eur, self.tl, "eur", "tl")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.eur} | {ylira.upper()}: {'%.2f'%self.tl} |\n")
                    time.sleep(2)  
                else:
                    self.checkBool(self.iseur, "Euro", True, "TRY", self.eur, money)   
            elif(xlira == "eur" and ylira == "usd"):
                if(self.iseur == True and self.isusd == True and money <= self.eur):    
                    self.eur -= money
                    addmoney = money * self.eurtousd
                    self.usd += addmoney
                    self.exchangePermission(addmoney, "dollar(s)", "USD", money, "euro(s)")
                    self.insertSQL(self.eur, self.usd, "eur", "usd")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.eur} | {ylira.upper()}: {'%.2f'%self.usd} |\n")
                    time.sleep(2)  
                else:
                    self.checkBool(self.iseur, "Euro", self.isusd, "USD", self.eur, money) 
            elif(xlira == "eur" and ylira == "gold"):
                if(self.iseur == True and self.isgold == True and money <= self.eur):    
                    self.eur -= money
                    addmoney = money * self.eurtogold
                    self.gold += addmoney  
                    self.exchangePermission(addmoney, "gram(s)", "Gold", money, "euro(s)")
                    self.insertSQL(self.eur, self.gold, "eur", "gold")
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.eur} | {ylira.capitalize()}: {'%.2f'%self.gold} gram(s) |\n") 
                    time.sleep(2)   
                else:
                    self.checkBool(self.iseur, "Euro", self.isgold, "Gold", self.eur, money)    
            elif(xlira == "gold" and ylira == "try"):
                if(self.isgold == True and money <= self.gold):    
                    self.gold -= money
                    addmoney = money * self.goldtotl
                    self.tl += addmoney  
                    self.exchangePermission(addmoney, "lira(s)", "TRY", money, "gram(s)")
                    self.insertSQL(self.gold, self.tl, "gold", "tl")
                    print(f"Current balance is updated as | {xlira.capitalize()}: {'%.2f'%self.gold} gram(s) | {ylira.upper()}: {'%.2f'%self.tl} |\n")
                    time.sleep(2)  
                else:
                    self.checkBool(self.isgold, "Gold", True, "TRY", self.gold, money)
            elif(xlira == "gold" and ylira == "usd"):
                if(self.isgold == True and self.isusd == True and money <= self.gold):    
                    self.gold -= money
                    addmoney = money * self.goldtousd
                    self.usd += addmoney  
                    self.exchangePermission(addmoney, "dollar(s)", "USD", money, "gram(s)")
                    self.insertSQL(self.gold, self.usd, "gold", "usd")
                    print(f"Current balance is updated as | {xlira.capitalize()}: {'%.2f'%self.gold} gram(s) | {ylira.upper()}: {'%.2f'%self.usd} |\n")
                    time.sleep(2)  
                else:
                    self.checkBool(self.isgold, "Gold", self.isusd, "USD", self.gold, money)        
            elif(xlira == "gold" and ylira == "eur"):
                if(self.isgold == True and self.iseur == True and money <= self.gold):    
                    self.gold -= money
                    addmoney = money * self.goldtoeur
                    self.eur += addmoney 
                    self.exchangePermission(addmoney, "euro(s)", "EUR", money, "gram(s)")
                    self.insertSQL(self.gold, self.eur, "gold", "eur") 
                    print(f"Current balance is updated as | {xlira.capitalize()}: {'%.2f'%self.gold} gram(s) | {ylira.upper()}: {'%.2f'%self.eur} |\n")
                    time.sleep(2)  
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


    def createCurrency(self):  
        self.isusd, self.iseur, self.isgold 
        if(self.isusd == False or self.iseur == False or self.isgold == False):     
            print("Please select respective number to create currency account\n")
            time.sleep(0.2)
            print("1. USD Account\n2. EUR Account\n3. Gold Account\n9. Return main screen\n")
            time.sleep(0.2)
            go = input("Go: ")
            print("")
            time.sleep(0.2)
        
            if(go == "1" and self.isusd == True):
                print("Your USD account is already created\n")
                time.sleep(1)
            elif(go == "1"):
                psw = input("Please type your password to create a USD balance: ")
                print("")
                if(psw == self.passw):
                    self.isusd = True
                    print("USD account is created!\n")
                    idu = self.idn + 1
                    sql = f"Update users Set isusd = {self.isusd} where idusers = {idu}"
                    self.mycursor.execute(sql)
                    time.sleep(1)
                else:
                    print("Password is incorrect, going back to main screen\n")
                    time.sleep(1)
                    self.interface(self.idn)
            if(go == "2" and self.iseur == True):
                print("Your EUR account is already created\n")
                time.sleep(1)
            elif(go == "2"):
                psw = input("Please type your password to create a EUR balance: ")
                print("")
                if(psw == self.passw):
                    self.iseur = True
                    idu = self.idn + 1
                    sql = f"Update users Set iseur = {self.iseur} where idusers = {idu}"
                    self.mycursor.execute(sql)
                    print("Euro account is created!\n")
                    time.sleep(1)
                else:
                    print("Password is incorrect, going back to main screen\n")
                    time.sleep(1)
                    self.interface(self.idn)
            if(go == "3" and self.isgold == True):
                print("Your Gold account is already created\n")
                time.sleep(1)
            elif(go == "3"):
                psw = input("Please type your password to create a Gold account: ")
                print("")
                if(psw == self.passw):
                    self.isgold = True
                    idu = self.idn + 1         
                    sql = f"Update users Set isgold = {self.isgold} where idusers = {idu}"
                    self.mycursor.execute(sql)       
                    print("Gold account is created!\n")
                    time.sleep(1)
                else:
                    print("Password is incorrect, going back to main screen\n")
                    time.sleep(1)
                    self.interface(self.idn)
            if(go == "9"):
                self.interface(self.idn)
            if(go != "1" and go != "2" and go != "3" and go != "9"): 
                print("Your statement is invalid")
                time.sleep(1)
                self.createCurrency()
            
            try:
                self.mydb.commit()
            except mysql.connector.Error as err:
                print("There is an error of ", err)
            finally:
                self.mydb.close()
        
        else:
            print("You have already all the accounts\nNo account available to create\n")
            time.sleep(1)


    def checkBool(self, bool1, m1, bool2, m2, unit, mny): 
        time.sleep(0.2)
        bool3 = False
        if(unit <= mny):
            bool3 = True
        if(bool1 == False):
            print(f"You do NOT have {m1} account for exchange operations\n")
            bool3 = False
            time.sleep(1)
        if(bool2 == False):
            print(f"You do NOT have {m2} account for exchange operations\n") 
            bool3 = False
            time.sleep(1)
        if(bool3 == True):
            print(f"You do NOT have sufficient {m1} to exchange it with {m2}\n") 
            time.sleep(1)


    def nameCorrection(self):
        time.sleep(0.2)
        self.name = input("Name: ")
        print("")

        self.turnBack(self.name, self.menu)
        specialChar = ["!","'","^","+","%","&","/","(",")","=","?","_","-","*","|","\"","}","]","[","{","½","$","#","£",">","<",":",".","`",";",",","<","é","æ","ß","@","€","¨","~","´","\\", " ", "\t", "\b"]
        isuser = True
        
        if(len(self.name) > 13 or len(self.name) < 2):
            isuser = False
            print("Your name can NOT be less than two and more than thirteen characters\n")
            time.sleep(1)
        elif any(char.isdigit() for char in self.name): 
            isuser = False
            print("Your name can NOT have digit(s)\n")
            time.sleep(1)
        elif any(char in specialChar for char in self.name):
            isuser = False
            print("Your name can NOT have special character(s)\n")
            time.sleep(1)
        if(isuser == True):
            return isuser
        else:
            self.nameCorrection()

    def snameCorrection(self):
        time.sleep(0.2)
        self.sname = input("Surname: ")
        print("")

        self.turnBack(self.sname, self.menu)
        specialChar = ["!","'","^","+","%","&","/","(",")","=","?","_","-","*","|","\"","}","]","[","{","½","$","#","£",">","<",":",".","`",";",",","<","é","æ","ß","@","€","¨","~","´","\\", " ", "\t", "\b"]
        isuser = True
        if(len(self.sname) > 15 or len(self.sname) < 2):
            isuser = False
            print("Your name can NOT be less than three and more than thirteen characters\n")
            time.sleep(1)
        elif any(char.isdigit() for char in self.sname): 
            isuser = False
            print("Your surname can NOT have digit(s)\n")
            time.sleep(1)
        elif any(char in specialChar for char in self.sname): # that is general usage
            isuser = False
            print("Your surname can NOT have special character(s)\n")
            time.sleep(1)
        if(isuser == True):
            return isuser
        else:
            self.snameCorrection()

    def idCorrection(self): 
        time.sleep(0.2)
        self.id = input("Identity number: ")
        print("")
        
        self.turnBack(self.id, self.menu)
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        isuser = True
        if not(int(len(self.id)) == 11):
            isuser = False
            print("Identity number must have 11 digits\n")
            time.sleep(1)
        elif not all(char in nums for char in self.id):
            isuser = False
            print("Identity number only consist of integers\n")
            time.sleep(1)
        if(isuser == True):
            return isuser
        else:
            self.idCorrection()    

    def passwCorrection(self): 
        time.sleep(0.2)
        self.passw = input("Password: ")
        print("")

        specialChar = ["!","'","^","+","%","&","/","(",")","=","?","_","-","*","|","\"","}","]","[","{","½","$","#","£",">","<",":",".","`",";",",","<","é","æ","ß","@","€","¨","~","´","\\", " ", "\t", "\b"]

        self.turnBack(self.passw, self.menu)
        isuser = True
        if(len(self.passw) > 15 or len(self.passw) < 8):
            isuser = False
            print("Your password can NOT be less than eigth and more than fifteen characters\n")
            time.sleep(1)
        elif any(char in specialChar for char in self.passw): # that is general usage
            isuser = False
            print("Your password can NOT have special character(s)\n")
            time.sleep(1)
        elif not any(char.isdigit() for char in self.passw):
            isuser = False
            print("Password must have at least one digit\n")
            time.sleep(1)
        elif not any(char.isupper() for char in self.passw):
            print("Password must have at least one upper character\n")
            isuser = False
            time.sleep(1)
        elif not any(char.islower() for char in self.passw):
            print("Password must have at least one lower character*n")
            isuser = False 
            time.sleep(1)
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
            self.account(self.tl, "TRY", "lira", self.idn)
        elif(go == "2"):
            if(self.isusd == True):
                self.account(self.usd, "USD", "dollar", self.idn)
            else:
                print("You do NOT have US Dollar account to operate it.\n")
                time.sleep(1)
                self.interface(self.idn)
        elif(go == "3"):
            if(self.iseur == True):
                self.account(self.eur, "EUR", "euro", self.idn)
            else:
                print("You do NOT have Euro account to operate it.\n")
                time.sleep(1)
                self.interface(self.idn)
        elif(go == "4"):
            if(self.isgold == True):    
                self.goldAccount()
            else:
                print("You do NOT have Gold account to operate it.\n")
                time.sleep(1)
                self.interface(self.idn)
        elif(go == "9"):
            self.interface(self.idn)
        else:
            self.currencyAccount(isusd, iseur, isgold)


    def payMoney(self, themoney, m1, m2):
        print("Please type the amount that you would like to deposit\nType \"0\" to go back\n")
        self.printAsset(themoney, m1, 1)
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
        
        time.sleep(0.2)
        idu = self.idn + 1
        if(increment != 0): 
            if(m1 == "TRY"):
                self.tl += themoney
                idu = self.idn + 1
                sql = f"Update users Set tl = {self.tl} where idusers = {idu}"
                self.mycursor.execute(sql)
                print(f"{m1} balance is updated as {'%.2f'%self.tl} {m2}\n")
                time.sleep(1)
            elif(m1 == "USD"):
                self.usd += themoney
                sql = f"Update users Set usd = {self.usd} where idusers = {idu}"
                self.mycursor.execute(sql)
                print(f"{m1} balance is updated as {'%.2f'%self.usd} {m2}\n")
                time.sleep(1)
            elif(m1 == "EUR"):
                self.eur += themoney
                sql = f"Update users Set eur = {self.eur} where idusers = {idu}"
                self.mycursor.execute(sql)
                print(f"{m1} balance is updated as {'%.2f'%self.eur} {m2}\n")
                time.sleep(1)

            time.sleep(0.2)    
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
            print("Please type the amount that you would like to withdraw\nType \"0\" to go back\n")
            self.printAsset(themoney, m1, 1)
            themoney = 0
            decrement = 0
            ismoney = False
            while(ismoney == False):
                try:
                    decrement = float(input(f"{m1}: "))
                    print("")
                    if(isinstance(decrement, float) and decrement >= 0):
                        themoney += decrement
                        ismoney = True
                    else:           
                        print("Please type a positive value to operate")
                except:
                    print("")
                    print("Please type numerical values only")
            
            time.sleep(0.2)
            if(decrement != 0):
                if(m1 == "TRY" and (self.tl - themoney >= 0)):
                    self.tl -= themoney
                    idu = self.idn + 1
                    sql = f"Update users Set tl = {self.tl} where idusers = {idu}"
                    self.mycursor.execute(sql)
                    print(f"{m1} balance is updated as {'%.2f'%self.tl} {m2}\n")
                    time.sleep(1)
                elif(m1 == "USD" and (self.usd - themoney >= 0)):
                    self.usd -= themoney
                    idu = self.idn + 1
                    sql = f"Update users Set usd = {self.usd} where idusers = {idu}"
                    self.mycursor.execute(sql)
                    print(f"{m1} balance is updated as {'%.2f'%self.usd} {m2}\n")
                    time.sleep(1)
                elif(m1 == "EUR" and (self.eur - themoney >= 0)):
                    self.eur -= themoney
                    idu = self.idn + 1
                    sql = f"Update users Set eur = {self.eur} where idusers = {idu}"
                    self.mycursor.execute(sql)
                    print(f"{m1} balance is updated as {'%.2f'%self.eur} {m2}\n")
                    time.sleep(1)
                else:
                    themoney += decrement # this is not necessarry
                    print(f"You have insufficient currency to withdraw {'%.2f'%decrement} {m2}.\nNo currency is withdrawn.\n")
                
                time.sleep(0.2)
                try:
                    self.mydb.commit()
                except mysql.connector.Error as err:
                    print("There is an error of ", err)
                finally:
                    self.mydb.close()

            else:
                print("Returning back to the main screen")


    def printAssets(self, assMoney1, assMny1, assMoney2, assMny2, excRatio):
        print(f"Your asset in {assMny1} and {assMny2} accounts:")
        print(f"|    {assMny1}: {'%.2f'%assMoney1}    |    {assMny2}: {'%.2f'%assMoney2}    |")
        time.sleep(0.2) 
        print(f"Exchange ratio of", end = " ") 
        print(f"{assMny1} to {assMny2}: {'%.5f'%excRatio}\n\nDatas are taken from \"exchangeratesapi.io\"\n")  
        time.sleep(2)

    def printAsset(self, assMoney1, assMny1, a):
        if(a == 1):
            print(f"Your asset in {assMny1} account:")
            print(f"|    {assMny1}: {'%.2f'%assMoney1}    |\n")
            time.sleep(1)
        elif(a == 2):
            print(f"Your asset in {assMny1} account decreased to:")
            print(f"|    {assMny1}: {'%.2f'%assMoney1}    |\n")
            time.sleep(1)


    def insertSQL(self, mny2, mny4, mny1, mny3):
        idu = self.idn + 1
        sql1 = f"Update users Set {mny1} = {mny2} where idusers = {idu}"
        self.mycursor.execute(sql1)
        sql2 = f"Update users Set {mny3} = {mny4} where idusers = {idu}"
        self.mycursor.execute(sql2)


    def transferInterface(self): 
        if((self.tl > 0) or (self.isusd == True and self.usd > 0) or (self.iseur == True and self.eur > 0)):   
            bool = False
            while(bool == False):
                go = input("Go: ")
                time.sleep(0.2)
                print("")
                if(go == "0"):
                    self.interface(self.idn)
                elif(go == "1" or go == "2" or go == "3"):
                    bool = True
                else:
                    print("Please only type respective number\Press \"0\" to return\n") 
                    time.sleep(0.2)

            if(go == "1" or go == "2" or go == "3"):
                if(go == "1"):
                    if(self.tl > 0):
                        self.transferCurrency("TRY", "lira", self.tl, "tl", "tl", True) # method must be handled for this section
                    else:
                        print("You do NOT have any currency in your TRY account\n")
                        time.sleep(1)

                elif(go == "2"):
                    if(self.isusd == True and self.usd > 0):
                        self.transferCurrency("USD", "dollar", self.usd, "usd", "isusd", False)
                    elif(self.isusd == False): 
                        print("You do NOT have USD account to send currency\n")
                        time.sleep(1)
                        self.interface(self.idn)
                    elif(self.usd == 0):
                        print("You do NOT have any currency in your USD account\n")
                        time.sleep(1)
                        self.interface(self.idn)

                elif(go == "3"):
                    if(self.iseur == True):
                        self.transferCurrency("EUR", "euro", self.eur, "eur", "iseur", False)
                    elif(self.iseur == False):
                        print("You do NOT have EUR account to send currency\n")
                        time.sleep(1)
                        self.interface(self.idn)
                    elif(self.eur == 0):
                        print("You do NOT have any currency in your EUR account\n")
                        time.sleep(1)
                        self.interface(self.idn)

        else:
            print("There is no money in any of your currency account to transfer\nGoing back to the main screen\n")
            time.sleep(1)
            self.interface(self.idn)
    
        try:
            self.mydb.commit()
        except mysql.connector.Error as err:
            print("There is an error of ", err)
        finally:
            self.mydb.close()


    def transferCurrency(self, moneytype, moneyunit, money, lmoney, ismoneyy, tlpass):
        idu = self.idn + 1
        print(f"Please type identity number of the user to send {moneytype}\nPress \"0\" to return\n")
        time.sleep(0.2)
        bool = False; boool = False
        while(bool == False): # this while structure is little bit nonsense
            toUser = input("Identity Number: ")
            print("")
            if(toUser == "0"):
                print("Going back to the main screen")
                time.sleep(0.2)
                boool = True
            if(toUser != self.id):
                bool = True
            else:
                print("You can NOT send currency to your account. Please try again\nPress \"0\" to return")
                time.sleep(0.2)

        bool = False
        for data in self.database:
            if(toUser == str(data[3])):
                self.mycursor.execute(f"Select {ismoneyy} from users where id = {data[3]}")
                checkBalance = self.mycursor.fetchone()
                bool = True
                ismoney = False
                if(str(checkBalance) == "(1,)" or tlpass == True): # couldn't convert checkBalance boolean, found a way like this
                    self.printAsset(money, moneytype, 1) 
                    while(ismoney == False):
                        try:
                            sendMoney = float(input(f"{moneytype}: "))
                            print("")
                            if(isinstance(sendMoney, float) and sendMoney >= 0):
                                ismoney = True
                            else:           
                                print("Please type a positive value to operate")
                                time.sleep(0.2)
                        except:
                            print("")
                            print("Please type numerical values only")
                            time.sleep(0.2)
                    
                    if(sendMoney != 0):
                        if(sendMoney <= money):
                            money -= sendMoney
                            sql1 = f"Update users Set {lmoney} = {money} where idusers = {idu}"
                            self.mycursor.execute(sql1)
                            self.mycursor.execute(f"Select {lmoney} from users where id = {data[3]}")
                            sentMoney = self.mycursor.fetchone()
                            print(f"{sendMoney} {moneyunit}(s) is sent successfully\n")
                            time.sleep(0.2)
                            self.printAsset(money, moneytype, 2) 
                            senMoney = "%s" % (sentMoney) # I apply this structure first
                            sendMoney += float(senMoney) 
                            sql2 = f"Update users Set {lmoney} = {sendMoney} where id = {data[3]}"
                            self.mycursor.execute(sql2)
                        else:       
                            print("Your balance is not enough to transfer\n")
                            time.sleep(1)
                            self.interface(self.idn)
                    else:
                        print("Going back to the main screen\n")
                        time.sleep(1)
                        self.interface(self.idn)
                else:
                    print(f"Respective user do NOT have {moneytype} account to accept any balance\n")
                    time.sleep(1)
                    self.interface(self.idn)

        if(bool == False and toUser != "0"):
            print("There is no such registered identity number\n")
            time.sleep(1)
            self.interface(self.idn)
        elif(boool == True):
            self.interface(self.idn)
        elif(str(checkBalance) != "(1,)" and tlpass == False):
            print(f"Respective user does NOT have {moneytype} account to accept currency\n")
            time.sleep(1)


    def exchangePermission(self, money1, moneytype1, accountName, money2, moneytype2): 
        print(f"You will receive {'%.2f'%money1} {moneytype1} to your {accountName} account by spending {'%.2f'%money2} {moneytype2}\n")
        time.sleep(2)
        bool = False
        while(bool == False):
            print("1. Accept\n2. Refuse")
            go = input("Go: ")
            if(go == "1" or go == "2"):
                bool = True
            else:
                print("Please press respective number only\nPress \"2\" to return\n")
                time.sleep(1)
                bool = False
       
        if(go == "1"):
            pass
        elif(go == "2"): 
            if(moneytype1 == "lira(s)"):
                self.tl -= money1
            if(moneytype1 == "dollar(s)"):
                self.usd -= money1
            if(moneytype1 == "euro(s)"):
                self.eur -= money1
            if(moneytype1 == "gram(s)"):
                self.gold -= money1
            if(moneytype2 == "lira(s)"):
                self.tl += money2
            if(moneytype2 == "dollar(s)"):
                self.usd += money2
            if(moneytype2 == "euro(s)"):
                self.eur += money2
            if(moneytype2 == "gram(s)"):
                self.gold += money2
            
            print("")
            print("Operation denied. Going back to main screen\n")
            time.sleep(1)
            self.interface(self.idn)
        print("")


#-----Execution-----#

exe = BankCore()
exe.menu() # this is the main program 
# exe.interface(0) # for experimenting usages, some of the functions may not operate properly 
# exe.currencyExchange() # for experimenting usages, some of the functions may not operate properly 

#-----Execution-----#
