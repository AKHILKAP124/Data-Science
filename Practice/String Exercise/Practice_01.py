"""Create 3 variables to store street, city and country, now create address variable to store entire address. 
Use two ways of creating this variable, one using + operator and the other using f-string. 
Now Print the address in such a way that the street, city and country prints in a separate line"""

street = input("Enter Street Name :")
city = input("Enter City Name :")
Country = input("Enter Country Name :")

add1 = street + ", " + city + ", " + Country + "."
add2 = f"{street}, {city}, {Country}."

print(" ")
print("Adress print form 1 is :",add1)
print(" ")
print("Adress print form 2 is :",add2)