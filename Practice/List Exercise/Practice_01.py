"""Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190

Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this"""

expense_list = [2200,2350,2600,2130,2190]

# Question 1: How much did you spend more than in February compared to January?
more = expense_list[1]-expense_list[0]
print(f'I spend extra {more} dollar in February compared to January.')

# Question 2: Find out your total expense in first quarter (first three months) of the year.
frs_3_month_expn = expense_list[0]+expense_list[1]+expense_list[2]
print(f'My total expense in first quarter was {frs_3_month_expn}.')

# Question 3: Find out if you spent exactly 2000 dollars in any month
item = 2000
print('Did I spent exatally 2000 dollar in any month? ', item in expense_list)

# Question 4: June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list          
exp = 1980
expense_list.append(exp)
print(expense_list)

# Question 5: You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this

refund = expense_list[3]-200
expense_list[3] = refund
print(expense_list)