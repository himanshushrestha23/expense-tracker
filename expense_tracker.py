expenses=[]

def add_expense():
    description=input("Enter description: ")
    amount=int(input("Enter amount: "))
    category=input("Enter category: ")
    expense = {
    "description": description,
    "amount": amount,
    "category": category
    }
    expenses.append(expense)

    



def view_expenses():
    count=1
    for expense in expenses:
        print(f"{count}.{expense['description']} - Rs.{expense['amount']} - {expense['category']} ")
        count+=1



while True:
  print("""
  Expense Tracker 

  1. Add Expense
  2. View Expenses
  3. Exit
""")
  user_input=input("Choose an option: ")
  if user_input=="1":
      add_expense()
  elif user_input=="2":
      view_expenses()
  elif user_input=="3":
      break
  else:
      print("Invalid option")