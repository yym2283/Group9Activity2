"""
Group 3 activity 2
members: 
Elsayed, Mahmoud, mee5011: aed_to_eur, aed_to_britshPound, aed_to_dollar functions
Mersha, Yeshiwas, yym2283: Main Function
Nathershah, Faizahnadir, fn6379: dollar_to_aed, britishPound_to_aed, eur_to_aed functions
Manifesto :The program is used to convert different currencies.
          It converts AED to other currencies or other currencies to AED.
          Github link: https://github.com/yym2283/Group9Activity2
"""

'''The constants used for conversion'''
aed_eur=0.25     #Convertion rate from AED to Euro
aed_pound=0.22   #Convertion rate from AED to Pounds
aed_dol=0.27     #Convertion rate from AED to USD
dol_aed=3.67     #Convertion rate from USD to AED 
pound_aed=4.64   #Convertion rate from Pound to AED
eur_aed= 3.98    #Convertion rate from Euro to AED

def aed_to_eur(money):
    
    eur=money*aed_eur
    print(money,"AED is equal to",eur,"EUR")

def aed_to_britishPound(money):
    
    pound=money*aed_pound
    print(money,"AED is equal to",pound,"British Pound")

def aed_to_dollar(money):
   
    dollar=money*aed_dol
    print(money,"AED is equal to",dollar,"USD")

def dollar_to_aed(amount):
    
    aed= amount*dol_aed
    print(amount,"USD is equal to",aed,"AED")

def britishPound_to_aed(amount):
    
    aed=amount*pound_aed
    print(amount,"British Pound is equal to",aed,"AED")

def eur_to_aed(amount):
   
    aed=amount*eur_aed
    print(amount,"EUR is equal to",aed,"AED")

def main():
    while True:    
        print('''    
*************************
Welcome to Currency Converter
****************************
1. AED to other currencies
2. Other Currencies to AED
3. Exit
**************************
            ''')
        n=int(input("Enter your choice (1/2/3):"))
        if n==1:
                while True:
                    print("No. \tConversion method       \tConversion Rate ")
                    print("**   ******************        *******************")
                    print("1    \tAED to Euro (EUR)            \t",aed_eur)
                    print("2    \tAED to British Pound (GBP)   \t",aed_pound)
                    print("3    \tAED to US Dollar             \t",aed_dol) 
                    print("4    \tExit ")
                    print("**************************************************")
                    choice= int(input("Enter your choice (either: 1/2/3/4):"))
                    if choice==1:
                        print("You are now converting from AED to Euros.")
                        amount=float(input("Enter your amount: "))
                        aed_to_eur(amount)  
                    elif choice==2:
                        print("You are now converting from AED to British Pounds.")
                        amount=float(input("Enter your amount: "))
                        aed_to_britishPound(amount)
                    elif choice==3:
                        print("You are now converting from AED to US Dollars.")
                        amount=float(input("Enter your amount: "))
                        aed_to_dollar(amount)
                    elif choice==4:
                        print("Currency converter is closed!")
                    else:
                        print("Input Error! Try again.")
                        continue
                    break
        elif n==2:
                while True:
                    print("Sno. \tConversion Direction       \tConversion Rate ")
                    print("***   ******************       ******************")
                    print("1    \tEuro (EUR) to AED            \t",eur_aed)
                    print("2    \tBritish Pound (GBP) to AED   \t",pound_aed)
                    print("3    \tUS Dollar to AED             \t",dol_aed) 
                    print("4    \tExit ")
                    print("*************************************************")
                    select= int(input("Enter your choice (either: 1/2/3/4):"))
                    if select==1:
                        print("You are now converting from Euros to AED.")
                        amount=float(input("Enter your amount: "))
                        eur_to_aed(amount) 
                    elif select==2:
                        print("You are now converting from British Pounds to AED.")
                        amount=float(input("Enter your amount: "))
                        britishPound_to_aed(amount)
                    elif select==3:
                        print("You are now converting from US Dollars to AED.")
                        amount=float(input("Enter your amount: "))
                        dollar_to_aed(amount)
                    elif select==4:
                        print("Currency converter is closed!")
                    else:
                        print("Input Error! Try again.")
                        continue
                    break
        elif n==3:
                print("Program is exit!")
                break
        else:
                print("Invalid input!")
                print("Try again.")
                continue
        m= int(input('Do you want to continue conversion? Enter 1 if you say "Yes",or 0 if you say "No". '))
        if m==1:
             continue
        elif m==0:
             break
        else:
             print('Invalid input!')  
             break          

if __name__=="__main__":
    main()