# tl = 0
# eur = 0

# def menu():
#     a = input("Go: ")

#     if(a == "1"):
#         methodA()
#     elif(a == "2"):
#         methodB()
#     elif(a == "3"):
#         print(f"TL: {tl}, EUR: {eur}")
#         menu()
#     else:
#         print("Wrong input.")
#         menu()
    
#     menu()

# def methodA():
#     b = float(input("Value: "))
#     global tl
#     tl += b
    

# def methodB():
#     b = float(input("Value: "))
#     global eur
#     eur += b
    

# menu()
"""
def account(lira, trl, tll, turk):

    print(f"1. Display currency amount\n2. Deposit {trl}\n3. Withdraw {trl}\n9. Return main account\n")
    go = int(input("Go: "))

    if(go == 1):
        print("\nDear {}, you have {} {} in your {} account.\n".format(users["name"], str(lira), trl, turk)) 

    elif(go == 2):
        print("\nPlease type the amount that you would like to deposit.\n")
        addtl = float(input(f"{trl}: "))
        lira += addtl
        print(f"{trl} balance is updated as {lira} {tll}\n.")       

    elif(go == 3): 
        #global tl, usd, eur
        print("\nPlease type the amount that you would like to withdraw.")
        taketl = float(input(f"{trl}: "))
        lira -= taketl 
        
        if(lira >= 0):
            print(f"{trl} balance is updated as {lira} {tll}.\n")
           
        else:
            lira += taketl 
            print(f"\nYou have insufficient currency to withdraw {taketl} {tll}.\nNo currency is withdrawn.\n")

    elif(go == 9):
        interface()

    account(lira, trl, tll, turk) 
    # it overwrites since return function goes back to interface, any operation must be done there
"""

"""
# def goldAccount():
#     global gold # probably tl usd and eur need to be added as global

#     print("1. Display gold amount\n2. Purchase gold by using currency\n3. Sell gold\n9. Return main account\n")
#     go = int(input("Go: "))

#     if(go == 1):
#         print("\nDear {}, you have {} gram(s) in your Gold account.\n".format(users["name"].capitalize(), str(gold))) 

#     elif(go == 2):
#         print("\nPlease type the amount that you would like to purchase.\n")
#         addgold = float(input("Gold: "))
#         gold += addgold
#         print(f"Gold balance is updated as {gold} gram(s)\n.")       

#     elif(go == 3): 
#         print("\nPlease type the amount that you would like to sell.")
#         takegold = float(input("Gold: "))
#         gold -= takegold 
        
#         if(gold >= 0):
#             print(f"Gold balance is updated as {gold} gram(s).\n")
           
#         else:
#             gold += takegold 
#             print(f"\nYou have insufficient gold stock to withdraw {takegold} gram(s).\nNo gold is withdrawn.\n")

#     elif(go == 9):
#         interface()
"""

""" # these are the methods that are replaced by account() method, in account I did state them into one method

    def tryAccount(self):
        self.tl
        print(f"1. Display currency amount\n2. Deposit TRY\n3. Withdraw TRY\n9. Return main screen\n")
        go = input("Go: ")
        print("")

        if(go == "1"):
            print("Dear {}, you have {} tl in your Turkish Lira account.\n".format(self.users["name"], str('%.2f'%self.tl))) 

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
            print("Dear {}, you have {} dollar(s) in your US Dollar account.\n".format(self.users["name"], str('%.2f'%self.usd))) 

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
            print("Dear {}, you have {} euro in your Euro account.\n".format(self.users["name"], str('%.2f'%self.eur))) 

        elif(go == "2"):
            self.payMoney(self.eur, "EUR", "euros")         

        elif(go == "3"): 
            self.withdrawMoney(self.eur, "EUR", "euros")

        elif(go == "9"):
            self.interface()
        else:
            print("Please type any respective number to operate\n")            
            self.eurAccount() 
"""
#----------------------------------------------------------------#
# def account(self, mny, mnyU, mnyL):
#         mny
#         print(f"1. Display currency amount\n2. Deposit {mnyU}\n3. Withdraw {mnyU}\n9. Return main screen\n")
#         go = input("Go: ")
#         print("")

#         if(go == "1"):
#             print("Dear {}, you have {} {} in your {} account.\n".format(self.users["name"], str('%.2f'%mny), mnyL, mnyL.capitalize())) 

#         elif(go == "2"):
#             self.payMoney(mny, mnyU, mnyL)         

#         elif(go == "3"): 
#             self.withdrawMoney(mny, mnyU, mnyL)

#         elif(go == "9"):
#             self.interface()
#         else:
#             print("Please type any respective number to operate\n")            
#             self.eurAccount() 
#----------------------------------------------------------------#
# spaces are adjusted by considering decimals of exchange ratios, for instance if eurtotl decreases more, need to be adjusted again
# print("Your asset is shown below")
# print(f"      TRY: {'%.2f'%self.tl}      |        USD: {'%.2f'%self.usd}       |          EUR: {'%.2f'%self.eur}          |      Gold: {'%.4f'%self.gold}\n")

# print("Exchange ratios are shown below")
# print(f"TRY to USD: {'%.2f'%self.tltousd}     |    USD to TRY: {'%.2f'%self.usdtotl}    |     EUR to TRY : {'%.2f'%self.eurtotl}      |   Gold to TRY: {'%.4f'%self.goldtotl}")
# print(f"TRY to EUR: {'%.2f'%self.tltoeur}     |    USD to EUR: {'%.2f'%self.usdtoeur}    |      EUR to USD : {'%.2f'%self.eurtousd}      |   Gold to USD: {'%.4f'%self.goldtousd}")
# print(f"TRY to Gold: {'%.4f'%self.tltogold}  |   USD to Gold: {'%.4f'%self.usdtogold}  |    EUR to Gold : {'%.4f'%self.eurtogold}     |   Gold to EUR: {'%.4f'%self.goldtoeur}\n")
