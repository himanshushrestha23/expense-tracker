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
    print("Added Successfully!")

def view_expenses():
    count=1
    for expense in expenses:
        print(f"{count}.{expense['description']} - Rs.{expense['amount']} - {expense['category']} ")
        count+=1

def update_expense():
    view_expenses()
    update_choice=int(input("Choose an expense to update: "))

    index=update_choice-1

    new_description=input("Enter new description: ")
    new_amount=int(input("Enter new amount: "))
    new_category=input("Enter new category: ")
    
    selected_expense=expenses[index]

    selected_expense['description']=new_description
    selected_expense['amount']=new_amount
    selected_expense['category']=new_category
    print("Updated Successfully!")
    

def delete_expense():
    view_expenses()
    delete_choice=int(input("Choose an expense to delete: "))
    
    index=delete_choice-1

    expenses.pop(index)
    print("Deleted Successfully!")



while True:
  print("""
Expense Tracker 

  1. Add Expense
  2. View Expenses
  3. Update Expense
  4. Delete Expense
  5. Exit
""")
  user_input=input("Choose an option: ")
  if user_input=="1":
      add_expense()
  elif user_input=="2":
      view_expenses()
  elif user_input=="3":
      update_expense()
  elif user_input=="4":
      delete_expense()
  elif user_input=="5":
      break
  else:
      print("Invalid option")