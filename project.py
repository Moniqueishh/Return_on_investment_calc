# Using OOP- create a program that will calculate the Return on Investment(ROI) for a rental property.

# Create our class
class rentalCalculator():

    
    def __init__(self,income,expenses,investment):
        self.income = income
        self.expenses = expenses
        self.invenstment = investment

    # def weeklyCashFlow(self):
    #     for i in self.income:
    #         x = i
    #         for i in self.expenses:
    #             y = i 
    #             totalCashFlow = x - y 
    #     print(f"Your total monthly cash flow is {totalCashFlow}")


# Create our Methods
# INCOME: need an INPUT for income - EX: $2000********* DONEEEEE
# Rental income (main source of income)
# laundry- extra- 0
# storage- extra- 0
# Total: 2000

    def totalIncome(self):
        while True:
            try:
                resp1 = int(input("What is your total income for this property? >>> "))
                break
                        
            except ValueError: 
                print("Value Error- Please enter a NUMBER below!")
        self.income.append(resp1)


# EXPENSES: NEED AN INPUT FOR TOTAL Expenses- $1610*******- DONEEEEE
# Taxes- $150
# Insurance- $100
# Utilities(electric,water,sewer,trash,gas)- 0
# HOA Fees- 0
# Lawn/snow care- 0
# Vacancy- $100
# Repairs- $100
# CapEx(new roof, water heater, replacing things-upkeep)- $100
# Property management- $200
# Morgage- $860
# TOTAL: $1610

    def totalExpenses(self):
         while True:
            try:
                resp2 = int(input("What are your total expenses for this property? >>> "))
                self.expenses.append(resp2)
                for i in self.income:
                    x = i
                    for i in self.expenses:
                        y = i 
                        totalCashFlow = x - y 
                        return totalCashFlow
                    break
                        
            except ValueError: 
                print("Value Error- Please enter a NUMBER below! >>> ")
            # self.expenses.append(resp2)
            # for i in self.income:
            #     x = i
            #     for i in self.expenses:
            #         y = i 
            #         totalCashFlow = x - y 
            #         return totalCashFlow
        # print(f"Your total monthly cash flow is {totalCashFlow}")

# NEED A CALCULATION FOR TOTAL CASH FLOW- $390********* See above^^^^^^--- DONEEEEE
# CASH FLOW: $390
# (Income - Expenses)
# 2000-1610
# Total: $390

# TOTAL INVESTMENT: $ $50,000- NEED AN INPUT FOR TOTAL investment******
# Down payment- $40,000
# Closing costs- $3,000
# Rehab budget- $7,000
# Misc/other- 0
    def totalInvenstment(self):
        while True:
            try:
                resp3 = int(input("How much was your down payment for the property? >>> "))
                break
            except ValueError:
                print("That's not a number!")

        while True:
            try:
                resp4 = int(input("How about closing costs? >>> "))
                break
            except ValueError:
                print("That's not a number!")

        while True:
            try:        
                resp5 = int(input("How much is your rehab budget? >>> "))
                break
            except ValueError:
                print("That's not a number!")
                break


        resp6 = input("Any other investment amount we need to know about [Y/N?] >>> ")
        if resp6.lower() == "n":
            totalInvest = resp3 +resp4 + resp5 
                    # print(totalInvest) 
        if resp6.lower() == "y":
            while True:
                try:
                    resp7 = int(input("Enter any extra investments? >>> "))
                    break
            
                except ValueError: 
                    print("Value Error- Please enter a NUMBER below!")
            totalInvest = resp3 +resp4 + resp5 + resp7
            # print(totalInvest)
            # return totalInvest
# continue
# print(f"Your total investment on this property is {totalInvest}")
                        

        self.invenstment.append(totalInvest)
    #Annual cash flow


# UNCOMMENT THIS
        print("Now lets calculate......")
        while True:
            letsSee = input("Enter 'ROI' to see your Return on investment! >>> ")
            if letsSee.lower() == "roi":
                for i in self.income:
                    x = i
                    for i in self.expenses:
                        y = i
                        totalCashFlow = x - y 
                        annualCash = totalCashFlow * 12 
                        # return annualCash
                        # print(f"Your Annual cash flow is {annualCash}!")
        #ROI
                total = annualCash / totalInvest
                roi = total * 100
                print(f"Your total Return on Investment for this property is {roi}%!")
                break

            else:
                print("Ivalid input!")

                
                

    

# NEED A CALCULATION FOR ANNUAL CASH FLOW****
# Cash flow x 12 months = annual cash FLOW
# 390 x 12 = $4680


    # def annualCashFlow(self):
    #     for i in self.income:
    #         x = i
    #         for i in self.expenses:
    #             y = i
    #             totalCashFlow = x - y 
    #             annualCash = totalCashFlow * 12 
    #             # return annualCash
    #             print(f"Your Annual cash flow is {annualCash}!")

    #     total = annualCash / self.invenstment()
    #     roi = total * 100
    #     print(f"Your total Return on Investment for this property is {roi}%!")

# NEED A CALCULATION FOR CASH ON CASH- ROI************
# Annual cash flow / RETURN ON INVESTMENT = Cash on Cash Return On Investment  
# 4680 / 50,000 = 9.36% (.0936 x 100)

    # def returnOnInvestment(self):
    #     for i in self.income:
    #         x = i
    #         for i in self.expenses:
    #             y = i
    #             totalCashFlow = x - y 
    #             annualCash = totalCashFlow * 12 
    #     total = annualCash // self.invenstment()
    #     roi = total * 100
    #     print(f"Your total Return on Investment for this property is {roi}%!")




# NEED A PRINT STATEMENT FOR "YOUR RETURN ON INVESTMENT IS {####%}"
# ROI = 9.36% 




#Calling

property1 = rentalCalculator([],[],[])
#property1 = rentalCalculator(income,expenses,investment)

def roi():
    while True:
        resp = input("Would you like to know your return on investment?[Y/N]")
        if resp.lower() == "n":
            print("Cool, have a great day!")
            break

        elif resp.lower() == "y":
            property1.totalIncome()
            # print(property1.income)
            # resp1 = int(input("What is your total income for this property?"))
            # property1.income.append(resp1)
            property1.totalExpenses()
            # print(property1.expenses)
            # resp2 = int(input("What are your total expenses for this property?"))
            # property1.expenses
            property1.totalInvenstment()
            # resp3 = int(input("How much have you invested in the property?"))
            # property1.invenstment.append(resp3)
            # property1.totalInvenstment()
            # print(property1.invenstment)
            # property1.annualCashFlow()
            # property1.returnOnInvestment()
            break
        else:
            print("Invalid input, please enter 'Y' for yes or 'N' for no.")
roi()

