"""Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
Ask user to enter his fasting sugar level
If it is below 80 to 100 range then print that sugar is low
If it is above 100 then print that it is high otherwise print that it is normal"""

level = input('Enter your Fasting sugar level :')
level= int(level)
if (level>=80 and level<=100):
    print('Your sugar level is Normal')
elif (level<80):
    print('Your sugar level is Low')
elif (level>=101):
    print('Your sugar level is High')
else:
    print('Wrong Input')