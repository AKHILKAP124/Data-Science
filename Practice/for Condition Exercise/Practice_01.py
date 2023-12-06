"""After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads"""

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
for i in result:
    if i == "heads":
        i
print(f'{len(i)} times got heads' )     


"""Print square of all numbers between 1 to 10 except even numbers"""

for i in range(1,11):
    if i % 2 != 0 :
        print(i**2)
    

"""Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. 
If expense is not found then it should print that as well."""

# monthly expense list from Jan to May
expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
# Question 1: Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. 

month = int(input("Enter the month Expense : "))
m=0
for i in range(len(expense_list)):
    if month == expense_list[i]:
        m = i
        break
if m != 0:
    print(f'You spent {month} dollar in {month_list[m]} Month')
else:
    print(f'You didn\'t spend {month} in any month')  
    

"""Lets say you are running a 5 km race. Write a program that,

Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message"""          
for i in range(1,6):
    if i in [1,2,3,4]:
        tired = input(f'{i} km complete, Are You Tired? :')
        if tired == 'yes':
            print("you didn't finish the race")
            break
        else:
            continue
    elif i == 5:
        print(f'Congratulation You complete 5 km race')  
        

"""Write a program that prints following shape

*
**
***
****
*****"""  

def print_shape1(n):
    for i in range(n):
        print("*" * (i) + " " * (n - i))

print_shape1(6)


def print_shape2(n):
    for i in range(n):
        print(" " *(n - i) + "*" * (i) )

print_shape2(6)        