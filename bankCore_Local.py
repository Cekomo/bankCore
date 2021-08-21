# implement a structure that shows only existing accounts in that list (optional) interface --> go: 2
# oprHistory shows only date, you can adjust it as date & time as well
# Prosperity of this card belongs to bankCore # add that to second-low line for back side

# upper limit can be made to not gain error from mySQL for currencies, since upper limit of depositing is 1000000, it is..
# ..not easy to exceed limit

import random
import json
import requests
from math import floor
import time
import mysql.connector
import datetime

class BankCore:
    def __init__(self):

        self.tl = 0
        self.usd = 0
        self.eur = 0
        self.gold = 0

        self.idn = 0
        self.iban = ""

        # this variables are instantiate with the ratio of respective currencies when currencyExchange() is adressed
        self.tltousd = 0
        self.usdtotl = 0
        self.tltoeur = 0
        self.eurtotl = 0
        self.tltogold = 0
        self.goldtotl = 0
        self.usdtoeur = 0
        self.eurtousd = 0
        self.goldtousd = 0
        self.usdtogold = 0
        self.goldtoeur = 0
        self.eurtogold = 0

        self.name =  ""
        self.sname = ""
        self.id =    ""
        self.passw = ""

        self.isusd = False
        self.iseur = False
        self.isgold = False


    print("Welcome to bankCore version (2.5)!\nPlase type regarding number for the next operation.\n")

    def menu(self):
        print("1. Log in\n2. Create a new account\n3. About bankCore\n9. Exit\n")
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
        elif(go == "3"):
            self.aboutBankCore()
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
                self.iban = str(data[12])

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
        b = False
        self.passwCorrection(b)

        self.createIBAN()

        print("Your account is created\n")
        self.createUser(self.name, self.sname, self.id, self.passw, self.iban)
        # self.oprHistory(2, 6, 0, 0, "", 0, 0, 0, "")
        # self.mydb.commit() 

    def createUser(self, name, sname, id, passw, iban):

        self.mydb = mysql.connector.connect (
        database = "userinfo", # respective part for implementation
        host = "127.0.0.1",
        user = "root",
        password = "Bf27a96fae" )

        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("Select * From users")
        self.database = self.mycursor.fetchall()

        for data in self.database:
            cid = data[0] + 1

        name = name.capitalize()
        sname = sname.capitalize()

        act = (cid, None, None, None, None, None, None, None, None, None, None) # actions are left as 'NULL'
        acting = "INSERT INTO actions(id, act1, act2, act3, act4, act5, act6, act7, act8, act9, act10) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.mycursor.execute(acting, act)
        # i recruit that since there is no allocated space for nwe user, oprHistory is writing the first user's history last + 1 = initial
        # it seems it has circular structure for users

        values = (cid, name, sname, id, passw, "0", "0", "0", "0", "0", "0", "0", iban, "0")
        sql = "INSERT INTO users(idusers, uname, sname, id, passw, tl, usd, eur, gold, isusd, iseur, isgold, iban, card) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.mycursor.execute(sql, values)
        
        try:
            self.mydb.commit()
        except mysql.connector.Error as err:
            print("MySQL server does not respond: ", err)


    def printUser(self):
        print("Informations of the user are listed.")
        time.sleep(0.2)
        print("Name: {}\nSurname: {}\nIdentity number: {}\nPassword: {}\n".format(self.name, self.sname, self.id, self.passw))
        time.sleep(2)

    def aboutBankCore(self):
        print(f"1. Version\n2. Where to store user data\n3. About currency exchange ratios\n4. Future versions of bankCore\n5. Possible problems\n6. About developer\n9. Go back\n")
        time.sleep(1)
        bool = False
        nums = ["1", "2", "3", "4", "5", "6", "9"]
        while bool == False:
            go = input("Go: ")
            print("")
            if go in nums:
                bool = True
            else:
                print("Please only type a number that is shown")

        if(go == "1"):
            print("You are using bankCore Version 2.0\n")
            time.sleep(1)
        elif(go == "2"):
            print("All user related data are stored in local mySQL server\n")
            time.sleep(1)
        elif(go == "3"):
            print("Currency exchange ratios are taken from \"exchangeratesapi.io\"\nRatios are updated by daily\n")
            time.sleep(1)
        elif(go == "4"):
            print("In the future versions of bankCore:\n- User data storage mechanism will be on online server\n- bankCore will have its own user interface\n- User interface will be integrated to a website\n")
            time.sleep(2)
        elif(go == "5"):
            print("There may be some problems related with external modules:\n- MySQL problem occurs if there is no connection with its server\n- In order to receive currency exchange ratios, system must have an internet connection")
            print("- If currency exchange ratios are taken too much, taking those data externally will not be possible for a month\n\nPlease contact with developer if you realize any sort of bugs\n")
            time.sleep(1)
        elif(go == "6"):
            print("Hello, I am Cemil Şahin and I code this program within 27 days (current version is 2.0)\nIf you have any issue, you can contact with the developer by using the e-mail below:")
            print("\"derdinekeder_alayinagider_asaletinyeter_kasapceko@sagolera.com\"\n")
            time.sleep(4)
            print("Just kidding, use this: \"cemils18@gmail.com\"\n")
            time.sleep(1)
        elif(go == "9"):
            pass


    def interface(self, idd):

        self.mydb = mysql.connector.connect (
        database = "userinfo", # respective part for implementation
        host = "127.0.0.1",
        user = "root",
        password = "Bf27a96fae" )

        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("Select * From users")
        self.database = self.mycursor.fetchall()

        print("1. Show registry operations\n2. Operate currency accounts\n3. Create new currency account\n4. Transfer currency\n5. Exchange Currency\n6. Operation History\n7. Virtual card | coreCard\n9. Log out\n")
        go = input("Go: ")
        print("")

        if(go == "1"):
            self.registryOperations()
            # self.printUser() # adjust this method for 1.

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

        elif(go == "6"):
            self.oprHistory(1, 0, 0, 0, 0, 0, 0, 0, "")
        
        elif(go == "7"):
            print("1. Monitor personal cardCore\n2. Create an virtual card | cardCore\n9. Return to the main screen\n")
            self.cardMaker(1)

        elif(go == "9"):
            self.mydb.close()
            print("Ight, Imma Head Out.\n")
            self.menu()

        else:
            self.interface(self.idn)

        self.interface(self.idn) # after deposit and withdrawing, it doesn't return interface so this is added. check it


    def registryOperations(self):
        print("1. Registry informations\n2. Balance informations\n3. Change password\n4. Delete personal account\n9. Go back\n")
        bool = False
        time.sleep(0.2)
        while(bool == False):
            go = input("Go: ")
            print("")
            if(go == "9"):
                self.interface(self.idn)
            elif(go == "1" or go == "2" or go == "3" or go == "4"):
                bool = True
            else:
                print("Please type any respective number to go\nType \"9\" to go back")
                time.sleep(1)

        if(go == "1"): # hide the password and show just some parts of it
            print(f"Dear {self.name} {self.sname}, you can see your registry informations below\n")
            print(f"Identity number: {self.id}\nPassword: {self.passw}\n")
            time.sleep(2)


        elif(go == "2"):
            print(f"Dear {self.name}, you can see your balance informations below\n\nTRY: {'%.2f'%self.tl}\n")
            time.sleep(0.2)
            if(self.isusd == True):
                print(f"USD: {'%.2f'%self.usd}\n")
            else:
                print(f"USD: Nonactivated\n")
            time.sleep(0.2)
            if(self.iseur == True):
                print(f"EUR: {'%.2f'%self.eur}\n")
            else:
                print(f"EUR: Nonactivated\n")
            time.sleep(0.2)
            if(self.isgold == True):
                print(f"GOLD: {'%.2f'%self.gold} gram(s)\n")
            else:
                print(f"GOLD: Nonactivaated\n")
            time.sleep(2)
        elif(go == "3"):
            print("Please type your current password first to change with new")
            
            self.acceptPassw(1)
            self.oprHistory(2, 7, 0, 0, 0, 0, 0, 0, 0)
            self.mydb.commit()

        elif(go == "4"):
            print("Please type your current password to delete your existing account")
            self.acceptPassw(2)

    def acceptPassw(self, a):
        psw = input("Password: ")
        time.sleep(0.2)
        print("")
        if psw == "9":
            self.interface(self.idn)
        elif psw == self.passw and a == 1:
            time.sleep(0.2)
            print("Please type your new password\nIt must include: 8 - 15 characters, upper letter, lower letter, digit, no special character\n")
            b = True
            self.passwCorrection(b)
            psw = str(self.passw)
            self.mycursor.execute(f"Update users Set passw = '{psw}' where id = {self.id}") # when I do not use single quote, mysql thinks that the
            # .. password itself is a column
            self.mydb.commit()

            print("Your password is changed!\n")
        elif psw == self.passw and a == 2:
            time.sleep(0.2)
            print("Do you want to delete your account? (Type any other key to return)")
            time.sleep(1)
            print("This action can NOT be undone!\n")
            time.sleep(2)
            go = input("Type \"I agree to delete my existing account\" to delete your account permenantly:\n--> ")
            print("")
            if go == "I agree to delete my existing account":
                self.deleteAccount()
                print("Your account is deleted successfully\n")
                time.sleep(2)
                self.menu()
            else:
                print("Typing of agreement statement is incorrect\n")
                self.registryOperations()

        else:
            print("Your current password is incorrect\nType \"9\" to return main screen\n")
            time.sleep(1)
            self.registryOperations()

    def deleteAccount(self): # not checked if its correct
        idu = self.idn + 1
        sql = f"Delete From users where idusers = {idu}"
        acting = f"Delete From actions where id = {idu}"
        self.mycursor.execute(sql)
        self.mycursor.execute(acting)
        try:
            self.mydb.commit()
        except mysql.connector.Error as err:
            print("There is an error of ", err)
        finally:
            self.mydb.close()

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

        try:
            # variables to change exchange ratios dynamically for exchanceCurrency method
            # Source: "exchangeratesapi.io"
            apiURL = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=698d889676879382f142cb906f52f58b&format=1")
            apiURL = json.loads(apiURL.text)

            print("Currency exchange ratio data are taken from \"exchangeratesapi.io\"\n")
            time.sleep(1)

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

        except:
            print("Connection lost with external server\nCurrency exchange ratios will be used locally\n")
            time.sleep(1)

            #-- THE VALUES MAY NOT BE UP-TO-DATE! --#
            self.tltousd = 0.11868
            self.usdtotl = 8.42632
            self.tltoeur = 0.10112
            self.eurtotl = 9.88894
            self.tltogold = 0.00206
            self.goldtotl = 484.65990
            self.usdtoeur = 0.85210
            self.eurtousd = 1.17358
            self.goldtousd = 57.51738
            self.usdtogold = 0.01739
            self.goldtoeur = 49.01028
            self.eurtogold = 0.02040
            # values can be got from updatecurrencies.py file from time to time

        self.tl, self.usd, self.eur, self.gold

        if(self.isusd or self.iseur or self.isgold): # this statement provides direct exit if no account is created
            print("Please state the currency that you will give.\nPress \"0\" to return")
            time.sleep(0.2)
            self.islira = False
            while(self.islira == False):
                xlira = input("TRY / USD / EUR / GOLD: ")
                xlira = xlira.lower()
                print("")
                if(xlira == "0" or xlira == "9"):
                    self.interface(self.idn)
                    self.islira = True
                elif((xlira == "try" and self.tl > 0) or (xlira == "usd" and self.isusd and self.usd > 0) or (xlira == "eur" and self.iseur and self.eur > 0) or (xlira == "gold" and self.isgold and self.gold > 0)):
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

            print("Please state the currency that you will get.\nPress \"0\" to return")
            time.sleep(0.2)
            self.islira = False
            while(self.islira == False):
                ylira = input("TRY / USD / EUR / GOLD: ")
                ylira = ylira.lower()
                print("")
                if(ylira == "0" or ylira == "9"):
                    self.interface(self.idn)
                    self.islira = True
                elif(ylira == "try" or (ylira == "usd" and self.isusd) or (ylira == "eur" and self.iseur) or (ylira == "gold" and self.isgold)):
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
                    if(isinstance(money, float) and money >= 0.01 and xlira == "gold"):
                        pass
                    elif(isinstance(money, float) and money >= 1):
                        self.islira = True
                    elif(money == 0):
                        print("\nReturning main screen")
                        time.sleep(0.2)
                        self.islira = True
                        bool = False
                    elif(money < 1):
                        print(f"You can only use integer to send {xlira.upper()}\n")
                        time.sleep(1)

                    else:
                        print("Negative amounts are NOT allowed to be exchanged, please try again (press \"0\" to leave)\n")
                        time.sleep(1)
                except:
                    print(f"Please type valid value to exchange {xlira.upper()} with {ylira.upper()}")
                    time.sleep(1)
                    print("")

            print("")

            if(bool == False): # I instantiate bool and make statement for the problem below
                # it connects from exchangeCurrency to permissionExchange even if the connection is closed, fix this
                self.interface(self.idn)
            elif(xlira == "try" and ylira == "usd"):
                money = floor(money)
                if(self.isusd == True and money <= self.tl):
                    self.tl -= money
                    addmoney = money * self.tltousd
                    self.usd += addmoney
                    self.exchangePermission(addmoney, "dollar(s)", "USD", money, "lira(s)")
                    self.insertSQL(self.tl, self.usd, "tl", "usd", money, addmoney)
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.tl} | {ylira.upper()}: {'%.2f'%self.usd} |\n")
                    time.sleep(2)
                else:
                    self.checkBool(True, "TRY", self.isusd, "USD", self.tl, money)
            elif(xlira == "try" and ylira == "eur"):
                money = floor(money)
                if(self.iseur == True and money <= self.tl):
                    self.tl -= money
                    addmoney = money * self.tltoeur
                    self.eur += addmoney
                    self.exchangePermission(addmoney, "euro(s)", "EUR", money, "lira(s)")
                    self.insertSQL(self.tl, self.eur, "tl", "eur", money, addmoney)
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.tl} | {ylira.upper()}: {'%.2f'%self.eur} |\n")
                    time.sleep(2)
                else:
                    self.checkBool(True, "TRY", self.iseur, "Euro", self.tl, money)
            elif(xlira == "try" and ylira == "gold"):
                money = floor(money)
                if(self.isgold == True and money <= self.tl):
                    self.tl -= money
                    addmoney = money * self.tltogold
                    self.gold += addmoney
                    self.exchangePermission(addmoney, "gram(s)", "Gold", money, "lira(s)")
                    self.insertSQL(self.tl, self.gold, "tl", "gold", money, addmoney)
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.tl} | {ylira.capitalize()}: {'%.2f'%self.gold} gram(s) |\n")
                    time.sleep(2)
                else:
                    self.checkBool(True, "TRY", self.isgold, "Gold", self.tl, money)
            elif(xlira == "usd" and ylira == "try"):
                money = floor(money)
                if(self.isusd == True and money <= self.usd):
                    self.usd -= money
                    addmoney = money * self.usdtotl
                    self.tl += addmoney
                    self.exchangePermission(addmoney, "lira(s)", "TRY", money, "dollar(s)")
                    self.insertSQL(self.usd, self.tl, "usd", "tl", money, addmoney)
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.usd} | {ylira.upper()}: {'%.2f'%self.tl} |\n")
                    time.sleep(2)
                else:
                    self.checkBool(self.isusd, "USD", True, "TRY", self.usd, money)
            elif(xlira == "usd" and ylira == "eur"):
                money = floor(money)
                if(self.isusd == True and self.iseur == True and money <= self.usd):
                    self.usd -= money
                    addmoney = money * self.usdtoeur
                    self.eur += addmoney
                    self.exchangePermission(addmoney, "euro(s)", "EUR", money, "dollar(s)")
                    self.insertSQL(self.usd, self.eur, "usd", "eur", money, addmoney)
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.usd} | {ylira.upper()}: {'%.2f'%self.eur} |\n")
                    time.sleep(2)
                else:
                    self.checkBool(self.isusd, "USD", self.iseur, "Euro", self.usd, money)
            elif(xlira == "usd" and ylira == "gold"):
                money = floor(money)
                if(self.isusd == True and self.isgold == True and money <= self.usd):
                    self.usd -= money
                    addmoney = money * self.usdtogold
                    self.gold += addmoney
                    self.exchangePermission(addmoney, "gram(s)", "Gold", money, "dollar(s)")
                    self.insertSQL(self.usd, self.gold, "usd", "gold", money, addmoney)
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.usd} | {ylira.capitalize()}: {'%.2f'%self.gold} gram(s) |\n")
                    time.sleep(2)
                else:
                    self.checkBool(self.isusd, "USD", self.isgold, "Gold", self.usd, money)
            elif(xlira == "eur" and ylira == "try"):
                money = floor(money)
                if(self.iseur == True and money <= self.eur):
                    self.eur -= money
                    addmoney = money * self.eurtotl
                    self.tl += addmoney
                    self.exchangePermission(addmoney, "lira(s)", "TRY", money, "euro(s)")
                    self.insertSQL(self.eur, self.tl, "eur", "tl", money, addmoney)
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.eur} | {ylira.upper()}: {'%.2f'%self.tl} |\n")
                    time.sleep(2)
                else:
                    self.checkBool(self.iseur, "Euro", True, "TRY", self.eur, money)
            elif(xlira == "eur" and ylira == "usd"):
                money = floor(money)
                if(self.iseur == True and self.isusd == True and money <= self.eur):
                    self.eur -= money
                    addmoney = money * self.eurtousd
                    self.usd += addmoney
                    self.exchangePermission(addmoney, "dollar(s)", "USD", money, "euro(s)")
                    self.insertSQL(self.eur, self.usd, "eur", "usd", money, addmoney)
                    print(f"Current balance is updated as | {xlira.upper()}: {'%.2f'%self.eur} | {ylira.upper()}: {'%.2f'%self.usd} |\n")
                    time.sleep(2)
                else:
                    self.checkBool(self.iseur, "Euro", self.isusd, "USD", self.eur, money)
            elif(xlira == "eur" and ylira == "gold"):
                money = floor(money)
                if(self.iseur == True and self.isgold == True and money <= self.eur):
                    self.eur -= money
                    addmoney = money * self.eurtogold
                    self.gold += addmoney
                    self.exchangePermission(addmoney, "gram(s)", "Gold", money, "euro(s)")
                    self.insertSQL(self.eur, self.gold, "eur", "gold", money, addmoney)
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
                    self.insertSQL(self.gold, self.tl, "gold", "tl", money, addmoney)
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
                    self.insertSQL(self.gold, self.usd, "gold", "usd", money, addmoney)
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
                    self.insertSQL(self.gold, self.eur, "gold", "eur", money, addmoney)
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
                    self.oprHistory(2, 3, 0, 0, "USD", 0, 0, 0, "")
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
                    self.oprHistory(2, 3, 0, 0, "EUR", 0, 0, 0, "")
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
                    self.oprHistory(2, 3, 0, 0, "GOLD", 0, 0, 0, "")
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
        
        x = 0; y = 0; z = 0
        try:
            a = 0
            while 2*a <= 8:
                y += int(self.id[2*a])
                a += 1   
            a = 0
            while 2*a + 1 <= 7:
                z += int(self.id[2*a+1])
                a += 1
            for i in self.id[:-1]:
                x += int(i)
            
            q1 = (7*y + 9*z); q1 = str(q1)
            q2 = (7*y - z); q2 = str(q2)
            x = str(x)
            # print(self.id[10], self.id[-1], self.id[9], q1[-1], q2[-1], x[-1:])
            if(x[-1:] == self.id[10] and self.id[-1] == x[-1] and q1[-1] == self.id[9] and q2[-1] == self.id[9]):
                pass
            else:
                print("Identity number is not valid\n")
                isuser = False
                time.sleep(1)
        except:
            print("Identity number only consist of integers\n")
            time.sleep(1)

        if(isuser == True):
            return isuser
        else:
            self.idCorrection()

    def passwCorrection(self, b):
        time.sleep(0.2)
        oldpsw = self.passw 
        self.passw = input("Password: ")
        print("")

        specialChar = ["!","'","^","+","%","&","/","(",")","=","?","_","-","*","|","\"","}","]","[","{","½","$","#","£",">","<",":",".","`",";",",","<","é","æ","ß","@","€","¨","~","´","\\", " ", "\t", "\b"]

        isuser = True
        if(self.passw == "9" and b == True):
            self.passw = oldpsw
            self.interface(self.idn)
        elif(self.passw == "9" and b == False):
            self.menu()
        
        self.turnBack(self.passw, self.menu)
        if(oldpsw == self.passw):
            isuser = False
            print("Your password can NOT be the same with the old one\n")
        elif(len(self.passw) > 15 or len(self.passw) < 8):
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
            self.passwCorrection(b)


    def createIBAN(self): # IBAN: TR26 3437 8813 1000 xxxx xxxx xx
        rand = random.randint(1000000000, 9999999999) # I adjusted it as 10^10 but it limits the range
        # to prevent that, a structure like below can be implemented (below does not work although it seems correct)
        rand = "%s" % (rand)
        # res = 10 - len(rand) 
        # if res > 0:
        #     while res == 0:
        #         "0" + rand
        #         res -= 1

        self.iban = "TR26343788131000" + rand # rest 10 nuember will be random for each user


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
                s = "(s)"
                increment = float(input(f"{m1}: "))
                print("")
                if(increment == 0):
                    ismoney = True
                elif(increment > 1000000):
                    print(f"The maximum lodgement amount is 1000000 {m2 + s}")
                elif(isinstance(increment, float) and increment >= 10):
                    themoney += floor(increment)
                    ismoney = True
                elif(increment > 0 and increment < 10):
                    print(f"The minimum lodgement amount is 10 {m2 + s}")
                else:
                    print("Please type a positive value to operate")
            except:
                print("")
                print("Please type numerical values only")

        time.sleep(0.2)
        idu = self.idn + 1
        if(increment != 0):
            if(m1 == "TRY"):
                self.tl += floor(themoney)
                idu = self.idn + 1
                sql = f"Update users Set tl = {self.tl} where idusers = {idu}"
                self.mycursor.execute(sql)
                print(f"{m1} balance is updated as {'%.2f'%self.tl} {m2}\n")
                self.oprHistory(2, 1, floor(themoney), 0, "TRY", 0, 0, 0, "")
                time.sleep(1)
            elif(m1 == "USD"):
                self.usd += floor(themoney)
                sql = f"Update users Set usd = {self.usd} where idusers = {idu}"
                self.mycursor.execute(sql)
                print(f"{m1} balance is updated as {'%.2f'%self.usd} {m2}\n")
                self.oprHistory(2, 1, floor(themoney), 0, "USD", 0, 0, 0, "")
                time.sleep(1)
            elif(m1 == "EUR"):
                self.eur += floor(themoney)
                sql = f"Update users Set eur = {self.eur} where idusers = {idu}"
                self.mycursor.execute(sql)
                print(f"{m1} balance is updated as {'%.2f'%self.eur} {m2}\n")
                self.oprHistory(2, 1, floor(themoney), 0, "EUR", 0, 0, 0, "")
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
                    if(decrement == 0):
                        ismoney = True
                    elif(isinstance(decrement, float) and decrement >= 10):
                        themoney += floor(decrement)
                        ismoney = True
                    elif(decrement > 0 and decrement < 10):
                        s = "(s)"
                        print(f"The minimum withdrawal amount is 10 {m2 + s}")
                    else:
                        print("Please type a positive value to operate")
                except:
                    print("")
                    print("Please type numerical values only")

            time.sleep(0.2)
            if(decrement != 0):
                if(m1 == "TRY" and (self.tl - themoney >= 0)):
                    self.tl -= floor(themoney)
                    idu = self.idn + 1
                    sql = f"Update users Set tl = {self.tl} where idusers = {idu}"
                    self.mycursor.execute(sql)
                    print(f"{m1} balance is updated as {'%.2f'%self.tl} {m2}\n")
                    self.oprHistory(2, 2, 0, floor(themoney), "TRY", 0, 0, 0, "")
                    time.sleep(1)
                elif(m1 == "USD" and (self.usd - themoney >= 0)):
                    self.usd -= floor(themoney)
                    idu = self.idn + 1
                    sql = f"Update users Set usd = {self.usd} where idusers = {idu}"
                    self.mycursor.execute(sql)
                    print(f"{m1} balance is updated as {'%.2f'%self.usd} {m2}\n")
                    self.oprHistory(2, 2, 0, floor(themoney), "USD", 0, 0, 0, "")
                    time.sleep(1)
                elif(m1 == "EUR" and (self.eur - themoney >= 0)):
                    self.eur -= floor(themoney)
                    idu = self.idn + 1
                    sql = f"Update users Set eur = {self.eur} where idusers = {idu}"
                    self.mycursor.execute(sql)
                    print(f"{m1} balance is updated as {'%.2f'%self.eur} {m2}\n")
                    self.oprHistory(2, 2, 0, floor(themoney), "EUR", 0, 0, 0, "")
                    time.sleep(1)
                else:
                    themoney += floor(decrement) # this is not necessarry
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
        print(f"{assMny1} to {assMny2}: {'%.5f'%excRatio}\n")
        time.sleep(2)

    def printAsset(self, assMoney1, assMny1, a):
        if(a == 1):
            print(f"Your asset in {assMny1} account:")
            print(f"|    {assMny1}: {'%.2f'%assMoney1}    |\n")
            print(f"Transfer fee: 0.00 {assMny1}")
            time.sleep(1)
        elif(a == 2):
            print(f"Your asset in {assMny1} account decreased to:")
            print(f"|    {assMny1}: {'%.2f'%assMoney1}    |\n")
            time.sleep(1)


    def insertSQL(self, mny2, mny4, mny1, mny3, mny, addmny):
        idu = self.idn + 1
        sql1 = f"Update users Set {mny1} = {mny2} where idusers = {idu}"
        self.mycursor.execute(sql1)
        sql2 = f"Update users Set {mny3} = {mny4} where idusers = {idu}"
        self.mycursor.execute(sql2)
        self.oprHistory(2, 5, 0, 0, mny1, mny, 0, addmny, mny3) # it will need specialization afterwards


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
                    print("Please only type respective number\nPress \"0\" to return\n")
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
            toUser = input("IBAN: ")
            print("")
            if(toUser == "0"):
                print("Going back to the main screen")
                time.sleep(0.2)
                boool = True
            if(toUser != self.iban):
                bool = True
            else:
                print("You can NOT send currency to your account. Please try again\nPress \"0\" to return")
                time.sleep(0.2)

        bool = False
        for data in self.database:
            if(toUser == str(data[12])):
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
                            if money == self.tl:
                                self.tl -= floor(sendMoney)
                            elif money == self.usd:
                                self.usd -= floor(sendMoney)
                            elif money == self.eur:
                                self.eur -= floor(sendMoney)

                            money -= floor(sendMoney)
                            sql1 = f"Update users Set {lmoney} = {money} where idusers = {idu}"
                            self.mycursor.execute(sql1)

                            self.mycursor.execute(f"Select {lmoney} from users where id = {data[3]}")
                            sentMoney = self.mycursor.fetchone()
                            print(f"{floor(sendMoney)} {moneyunit}(s) is sent successfully\n")
                            time.sleep(0.2)
                            self.printAsset(money, moneytype, 2)
                            senMoney = "%s" % (sentMoney) # I apply this structure first time in my life
                            sendMoney = floor(sendMoney) #!
                            hMoney = sendMoney
                            sendMoney += float(senMoney)

                            sql2 = f"Update users Set {lmoney} = {sendMoney} where id = {data[3]}"
                            self.mycursor.execute(sql2)
                            # I guess i need user's name/surname data here instead of his id
                            fullname = data[1] + " " + data[2]
                            self.oprHistory(2, 4, 0, 0, lmoney.upper(), hMoney, fullname, 0, 0) # moneytype, sendMoney, data[3], 0, 0)
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
            print("There is no such registered IBAN\n")
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

    def oprHistory(self, type1, type2, depo, withd, curType, tranMoney, toWhom, transMoney, curnType): 
        # i canceled create account notation for history since it causes harsh problems to solve, besides there is not that much need for it
        if type1 == 1:
            idu = self.idn + 1
            self.mycursor.execute(f"Select * from actions where id = {idu}")
            operations = self.mycursor.fetchall()
            i = 1
            print("Account's most recent operations are listed (from More Current to Less)")
            time.sleep(1)
            for o in operations:
                while i <= 10:
                    time.sleep(0.2)
                    if o[i] != "on" and o[i] != None:
                        act = o[i].split(",")
                        if act[0] == "1":
                            print(f"{i}-", end = " ")
                            act[1] = float(act[1])
                            print(f"Lodgement - {act[2]}: {'%.2f'%act[1]} is deposited | {act[3]}")
                        elif act[0] == "2":
                            print(f"{i}-", end = " ")
                            act[1] = float(act[1])
                            print(f"Withdrawal - {act[2]}: {'%.2f'%act[1]} is withdrawn | {act[3]}")
                        elif act[0] == "3":
                            print(f"{i}-", end = " ")
                            print(f"Currency Account Creation - {act[1]} account is created | {act[2]}")
                        elif act[0] == "4":
                            if act[2] == "TL":
                                act[2] = "TRY"
                            print(f"{i}-", end = " ")
                            act[1] = float(act[1])
                            print(f"Currency Transfer - {act[2]}: {'%.2f'%act[1]} is transferred to {act[3]} | {act[4]}")
                        elif act[0] == "5":
                            if act[2]  == "tl":
                                act[2] = "TRY"
                            elif act[4] == "tl":
                                act[4] = "TRY"
                            print(f"{i}-", end = " ")
                            act[1] = float(act[1]); act[3] = float(act[3])
                            print(f"Currency Exchange - {act[4].upper()}: {'%.2f'%act[3]} is exchanged with {act[2].upper()}: {'%.2f'%act[1]} | {act[5]} ")
                        elif act[0] == "6":
                            print(f"{i}-", end = " ")
                            print(f"Virtual Card - Your cardCore is created | {act[1]}")
                        elif act[0] == "7":
                            print(f"{i}-", end = " ")
                            print(f"Password Change - Password is changed | {act[1]}")
                    else:
                        if(i == 9):
                            print("- No operation made")
                    i += 1

            time.sleep(2)
            print("")

        elif type1 == 2:
            idu = self.idn + 1
            rang = [9, 8, 7, 6, 5, 4, 3, 2, 1]
            for r in rang:
                self.mycursor.execute(f"Select act{r} from actions where id = {idu}")
                operations = self.mycursor.fetchone()
                t = r + 1
                operations = str(operations)
                operationss = operations[2:]
                operatio = operationss[:-3]
                self.mycursor.execute(f"Update actions Set act{t} = '{operatio}' where id = {idu}")
                self.mydb.commit()

            # timenow = datetime.datetime.now() # for date and precise hour
            timenow = datetime.date.today() # just for date

            operation = ""
            if type2 == 0:
                pass
            elif type2 == 1:
                operation = "1," + str(depo) + "," + str(curType) + "," + str(timenow)
            elif type2 == 2:
                operation = "2," + str(withd) + "," + str(curType) + "," + str(timenow)
            elif type2 == 3:
                operation = "3," + str(curType) + "," + str(timenow)
            elif type2 == 4:
                operation = "4," + str(tranMoney) + "," + str(curType) + "," + str(toWhom) + "," + str(timenow)
            elif type2 == 5:
                operation = "5," + str(tranMoney) + "," + str(curType) + "," + str(transMoney) + "," + str(curnType) + "," + str(timenow)
            elif type2 == 6:
                operation = "6," + str(timenow) 
            elif type2 == 7:
                operation = "7," + str(timenow)

            
            self.mycursor.execute(f"Update actions Set act1 = '{operation}' where id = {idu}")


    def cardMaker(self, a): # cdate as xx/xx | 2 spaces for cardnumber
        idu = self.idn + 1
        self.mycursor.execute(f"Select card from users where idusers = {idu}")
        cardinfo = self.mycursor.fetchone()
        cardinfo = str(cardinfo)
        cardinf = cardinfo[2:] 
        cardinfo = cardinf[:-3] 
        passgate = cardinfo.split(",")
        
        if a == 1:
            bool = False
            while bool == False:
                go = input("Go: ")
                if go == "1" or go == "2" or go == "9":
                    print("")
                    bool = True
                else: 
                    print("Please type respective number to go\n")
        else:
            go = "3"
        
        if (a == 0 or go == "2"):
            if passgate[0] == "0": # check that if its passgate[0]   
                psw = input("Please type your password to create cardCore: ")
                print("")

                if(psw == self.passw):
                    cardnumber = str(random.randint(1000, 9999)) + "  " + str(random.randint(1000, 9999))
                    cno = random.randint(100, 999)
                    today = datetime.date.today()
                    cdate = datetime.timedelta(days = 2520)
                    cdate = str(today + cdate) 
                    x = cdate.split("-")
                    cdate = x[0][2:] + "/" + x[1]
                    cardinfo = "1," + str(cardnumber) + "," + str(cdate) + "," + str(cno)
                    self.mycursor.execute(f"Update users Set card = '{cardinfo}' where id = {self.id}") 
                    self.mydb.commit()
                    print("Virtual card cardCore is created!\n")
                    self.oprHistory(2, 6, 0, 0, "", 0, 0, 0, "")
                    self.mydb.commit()
                    time.sleep(2)
                else:
                    print("Password is incorrect, going back to main screen\n")
                    time.sleep(1)
                    self.interface(self.idn)

            elif passgate[0] == "1":
                print("You already have virtual coreCard\nCan NOT create anymore before it expires\n")
                time.sleep(1)
                self.interface(self.idn)

        if (go == "1"):
            if passgate[0] == "1":    
                
                print("Your personal coreCard")
                print( f" ______________________________________\n|                                      |\n|  coreCard                            |")
                print(f"|                                      |\n|                                      |\n|        3465  2613  {passgate[1]}        |")
                print(f"|                                      |\n|                       {passgate[2]}     VISA |\n|______________________________________|")
                time.sleep(1)

                print( f" ______________________________________\n|                                      |\n|██████████████████████████████████████|")
                print(f"|██████████████████████████████████████|\n|                                      |\n|   𓅃   ███████████{passgate[3]}                 |")
                print(f"|                                      |\n|                                      |\n|______________________________________|\n\n")
                time.sleep(2)

            elif passgate[0] == "0":
                print("You do NOT have personal coreCard to display\n")
                time.sleep(1)
                print("Would you like to create new virtual card | coreCard?\n1. Accept\n2. Refuse\n")
                time.sleep(2)
                bool = False
                while bool == False:
                    go = input("Go: ")
                    if go == "1" or go == "2" or go == "0":
                        print("")
                        bool = True
                    else: 
                        print("Please type respective number to go\n")

                if go == "1":
                    self.cardMaker(0)
                else:
                    self.interface(self.idn)        


#-----Execution-----#

exe = BankCore()
exe.menu() # this is the main program

#-----Execution-----#
