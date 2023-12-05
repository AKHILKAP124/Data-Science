"""Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
Write a program that asks user to enter a city name and it should tell which country the city belongs to
Write a program that asks user to enter two cities and it tells you if they both are in same country or not. 
For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"""

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# Question 1: Write a program that asks user to enter a city name and it should tell which country the city belongs to
user = input("Enter your City Name :")

if user in india:
    print('City is belong to Country India')
elif user in pakistan:
    print('City is belong to Country Pakistan')
elif user in bangladesh:
    print('City is belong to Country Bangladesh') 
else:
    print('Sorry, No data Fount')
    
    
# Question 2: Write a program that asks user to enter two cities and it tells you if they both are in same country or not. 
city1 = input("Enter first City Name : ")
city2 = input("Enter second City Name : ")

if city1 in india and city2 in india:
    print('Both cities belong to India')
elif city1 in pakistan and city2 in pakistan:
    print('Both cities belong to Pakistan')
elif city1 in bangladesh and city2 in bangladesh:
    print('Both cities belong to Bangladesh')
else:
    print("They don't belong to same country")
    
    
