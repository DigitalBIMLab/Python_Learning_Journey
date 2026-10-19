'''Problem 1 — Personal Expense Analyzer
Write a Python program that accepts a user's monthly income and expenses across multiple categories. Calculate the total expenses, remaining balance, savings percentage, and the category with the highest spending. Display a summary report.'''


'''FIRST TRY'''
# #MONTHLY INCOME
# monthly_income = float(input("Type your monthly income: "))      #If monthly_income is 0, calculating Saving causes a ZeroDivisionError.

# #EXPENSES      #use lowercase snake_case, such as monthly_income and personal_expenses, instead of Groceries_Food or Saving.
# Groceries_Food   = float(input("Type your Meal expenses: "))
# Rent               = float(input("Type your Rent expenses: "))
# Travel             = float(input("Type your Travel expenses: "))
# Personal_Belongings= float(input("Type your Personal expenses: "))

# print(f"Monthy Income: Rs.{round(monthly_income,2)}")

# print("Expenses")
# print(f"Groceries & Food: Rs.{round(Groceries_Food,2)}")
# print(f"Rent: Rs.{round(Rent,2)}")
# print(f"Travel: Rs.{round(Travel,2)}")
# print(f"Personal_Belongings: Rs.{round(Personal_Belongings,2)}")

# sum_01 = (Groceries_Food+Rent+Travel+Personal_Belongings)   #a + b is sufficient; (a + b) is not needed here.
# #Replace sum_01 and sum_02 with total_expenses and remaining_balance.
# sum_02 = (monthly_income-sum_01)
# Saving = ((sum_02/monthly_income)*100)

# print(f"Total Expense:{round(sum_01,2)}Rs.")
# print(f"Remaining Balance:{round(sum_02,2)}Rs.")
# print(f"Savings %:{round(Saving,2)}")


'''IMPROVED VERSION'''
#MONTHLY INCOME
monthly_income = float(input("Type your monthly income: "))

#MONTHLY EXPENSES
expenses={
    "Groceries & Food"      : float(input("Type your Meal expenses: ")),
    "Rent"                  : float(input("Type your Rent expenses: ")),
    "Travel"                : float(input("Type your Travel expenses: ")),
    "Personal Belongings"   : float(input("Type your Personal expenses: "))  
}

#CALCULATION
total_expenses = sum(expenses.values())
remianing_balance = monthly_income-total_expenses
saving_perstantag = (
    remianing_balance / monthly_income * 100
    if monthly_income > 0 else 0            #If monthly_income > 0 is true, calculate the savings percentage,
)
highest_expense = max(expenses,key=expenses.get)

#MONTHLY REPORT
print("\n====== Monthly Expenses Report ======")
print(f"{'Monthly Income':<20} {monthly_income:.2f}Rs.")
for category, amount in expenses.items():
    print(f"{category:<20} {amount:.2f}Rs.")

print("-" * 36)
print(f"{'Total Expenses':<20} {total_expenses:.2f}Rs.")            #<20 to give equal distance. 20 is character no.
print(f"{'Remaining Balance':<20} {remianing_balance:.2f}Rs.")      #.2f is a formatting instruction in an f-string.
print(f"{'Savings Percentage':<20} {saving_perstantag:.2f}%")
print(f"{'Highest Expense':<20} {highest_expense}")

# {category:<20}	Left-align within 20 characters
# {category:>20}	Right-align within 20 characters
# {category:^20}	Center-align within 20 characters