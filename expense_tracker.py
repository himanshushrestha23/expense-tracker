expenses=[]


try:
    with open("expenses.txt","r") as file:
        for line in file:
                parts=line.split(":")
                description=parts[0]
                amount=int(parts[1])
                category=parts[2].strip()
                expense = {
                    "description": description,
                    "amount": amount,
                    "category": category
                    }
                print(expense)
                expenses.append(expense)
                print(expenses)

except FileNotFoundError:
    pass


def add_expense():
   
            description=input("Enter description: ")
            while True: 
                try:
                        amount=int(input("Enter amount: "))
                        break
                except ValueError:
                            print("Invalid input, should be a number")
            
            category=input("Enter category: ")
            expense = {
            "description": description,
            "amount": amount,
            "category": category
            }
            expenses.append(expense)
            print("Added Successfully!")
            

       
def view_expenses():
    if not expenses:
             print("There are no expenses")

    else:
        count=1
        for expense in expenses:
            print(f"{count}.{expense['description']} - Rs.{expense['amount']} - {expense['category']} ")
            count+=1

def update_expense():
    if not expenses:
         print("There are no expenses")

    else:
        view_expenses()
        
       
        while True: 
            update_choice=int(input("Choose an expense to update: "))
            if update_choice <1 or update_choice > len(expenses):
                print("Invalid option, try again")
                

            else:

                index=update_choice-1

                new_description=input("Enter new description: ")

                while True: 
                                try:
                                        new_amount=int(input("Enter new amount: "))
                                        break
                                except ValueError:
                                            print("Invalid input, should be a number")
                
                new_category=input("Enter new category: ")
                
                selected_expense=expenses[index]

                selected_expense['description']=new_description
                selected_expense['amount']=new_amount
                selected_expense['category']=new_category
                print("Updated Successfully!")
                break
               
    

def delete_expense():

        if not expenses:
            print("There are no expenses")
        else:
            
            
                view_expenses()
                while True: 
                    try:
                        delete_choice=int(input("Choose an expense to delete: "))
                        if delete_choice <1 or delete_choice > len(expenses):
                            print("Invalid option, try again")

                        else:
                            index=delete_choice-1
                            expenses.pop(index)
                            print("Deleted Successfully!")
                            break

                    except IndexError:
                        print("Invalid option, try again")
                
                

            
            

    

def show_total():
    total=0
    for expense in expenses:
        total+=expense['amount']

    print(f"Total Expense: Rs.{total}")
    



while True:
  print("""
Expense Tracker 

  1. Add Expense
  2. View Expenses
  3. Update Expense
  4. Delete Expense
  5. Show Total
  6. Exit
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
      show_total()
  elif user_input=="6":
      with open("expenses.txt","w") as file:
        for expense in expenses:
            file.write(f"{expense['description']}:{expense['amount']}:{expense['category']}\n")
      break
  else:
      print("Invalid option")