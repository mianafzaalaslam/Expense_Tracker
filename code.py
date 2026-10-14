i = 0
smallest = 0
biggest = 0
total = {}
while i < 3:
    category = input("Enter the expense name: ")
    amount = int(input("Enter the expense amount: ")) 
    total[category] = amount
    i+=1  

biggest = max(total.values())
smallest = min(total.values())
print("Biggest value is: ",biggest)
print("Smallest value is: ",smallest)

for b in total.values():   
     if b > 0:
       print("Your total Expense is: ",sum(total.values()))  
     elif b == 0:
       print("Your expense is 0")
     else:
       print("You take laon")
