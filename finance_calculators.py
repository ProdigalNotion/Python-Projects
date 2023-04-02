import math
# prints general statement for user to understand investment or bond.
print ("investment - to calculate the amount of interest you'll earn on your investment\nbond - to calculate the amount you'll have to pay on a home loan")
# creates an input where the user can enter 'investment' or 'bond' - i used the .lower at the end to ensure whatever is inputted is read in lower-case.
type_of_investment = (input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower())
# checks whether investment has been chosen - then allows user to enter deposit, percentage, years and simple/compound. - i used int function to ensure only numbers can be entered.
if type_of_investment == 'investment':
    investment_deposit = int(input("Enter the amount of money you are depositing: "))
    investment_percentage = int(input("Enter the interest rate: "))
    investment_years = int(input("Enter the amount of years you would like to invest:"))
    investment_type = (input("Enter if you would like simple or compound interest:").lower())
# checks whether simple interest has been chosen then calculates and prints the sum total of interest user receives at the end of investment.
   if investment_type == 'simple':
        simple_interest = investment_deposit * (1 + (investment_percentage / 100) * investment_years)
        print (simple_interest)
# checks whether compound interest has been chosen then calculates and prints the sum total of interest user receiv ed at the end of investment.
    elif investment_type == 'compound':
        compound_interest = investment_deposit * math.pow((1 + (investment_percentage / 100)), investment_years)
        print (compound_interest)
# checks whether bond has been chosen, allows user to enter house value, interest rate, amount of months planned to repay bond, calculates repayment and prints out the repayment plan monthly.
elif type_of_investment == 'bond':
    bond_house_value = int(input("Enter the present value of your house: "))
    bond_interest_rate = int(input("Enter the interest rate: "))
    bond_months = int(input("Enter the amount of months you plan to repay the bond: "))
    repayment = (((bond_interest_rate / 100) / 12) * bond_house_value) / (1 - (1 + ((bond_interest_rate / 100) / 12)) ** ( - bond_months))
    print (repayment)
#prints out if the user does not enter 'investment' or 'bond' when first choosing investment type.
else: print("Sorry, you have not entered the type of investment.")
