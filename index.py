# application letter writer. 
#application type ( loan and employment)
#details about customer
#details (writers addresss)  - Name of the Person or  Church for address
                    #          - Post Office Box 
                    #          - Town of resident
                    #          - Date 
#details (receipient addreesss)    -  Name of bank
                    #          - Post Office Box 
                    #          - Town of bank
                    #          - Date 
#details (loan)                - amount requesting for 
                            #   -  purpose
                            #  - account number 
                            
                            
#Dictionary for keeping details of  customer

#the letter sample can be stored as normal text  and regular expressions will be used to change details of  the letter



from datetime import datetime , date 
from time import sleep
import re
from random import randint ,choice
from loansamples import sample
#Details for loan
class Self_details:
     def name():
         name = input("Full name ")
         return name 
     def town():
         town = input("Town ")
         return town 
     def age():
         age = int(input("Age "))
         return age
     def sex():
         sex = input("Sex ")
         return sex
     def box_number():
         box_number = input("Enter box number ")
         return box_number
     def loan_amount():
         loan_amount = input("Enter amount requesting for [Example: GHC534,00] ")
         return loan_amount
     

# Receipient address
class Receipient_ad:
    def bank_name ():
        bank_name = input("Enter Bank name ")
        return bank_name
    
    def box_number_bank():
        box_number_bank = input("Enter bank box number ")
        return box_number_bank
    
    def bank_branch():
        bank_branch = input("Enter the branch of the bank [example: Sefwi Bekwai Branch] ")
        return bank_branch

        
customer_self_d = dict()

ask_type_of_letter = input("What type of letter do you want to create  [EMPLOYEMT/LOAN/OVERDRAFT ]").lower()

if ask_type_of_letter  == "loan" or "overdraft":
    print("Fill in your details")
    sleep(2)
    applicant = Self_details
    name = applicant.name()
    age = applicant.age()
    town = applicant.town()
    sex = applicant.sex()
    box_number = applicant.box_number()
    loan_amount = applicant.loan_amount()
    
    #address of bank(receipient address)
    address = Receipient_ad
    bankname = address.bank_name()
    bankbox = address.box_number_bank()
    branch = address.bank_branch()
    
    
#printing address
def address_print():
    print(" " * 80, name + ",")
    print(" " * 80, "Post Office Box ",box_number+ ",")
    print(" " *  80,town+".")
    dat = datetime.now()
    print(" " * 80, str(dat.date())+ ".")
    print("The Manager"+",")
    print(bankname+",")
    print("Post Office Box",bankbox+",")
    print(branch+",")
    
address_print()
print(" "* 6, "Dear Sir/Madam")
heading = "APPLICATIONF FOR LOAN"
print("   "*20, heading)
    



# def processer():
randomizer = choice(sample)
pattern = re.compile(r"amount*")
change = pattern.sub(loan_amount, randomizer)

pattern_for_age = re.compile(r"age")
change1 = pattern_for_age.sub(str(age), change)

if age <  40:
    pattern_for_gender = re.compile(r"gender")
    change2 = pattern_for_gender.sub(sex, change1)
    pattern_for_adverb =re.compile(r"adverb")
    change3 = pattern_for_adverb.sub(r"young", change2)

elif age > 40:
    pattern_for_gender = re.compile(r"gender")
    change2 = pattern_for_gender.sub(sex, change1)
    pattern_for_adverb =re.compile(r"adverb")
    change3 = pattern_for_adverb.sub(r"", change2)


pattern_for_town = re.compile(r"Town")
change4 = pattern_for_town.sub("Sefwi Bibiani",change3)

pattern_for_accno = re.compile(r"acctno")
change5 = pattern_for_accno.sub("242353400003", change4)

pattern_for_reason = re.compile(r"reason")
change6 = pattern_for_reason.sub("to pay my rent", change5)

patter_for_experience = re.compile(r"number of years")
change7 = patter_for_experience.sub(str(5), change6)
print(change7)








