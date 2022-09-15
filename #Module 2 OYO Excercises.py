#Module 2 OYO Excercises

#Exercise 1
#Prompt the user to enter their name and greet them
name = input("Enter your name: ")
print("Nice to meet you", name + "!")

#Exercise 2
#Prompt the user to enter a sales tax rate
tax_Rate = float(input("Enter a sales tax rate: "))
price = int(input("Enter a price: "))
total_Price = (price * tax_Rate) + price
print("The total price is:", total_Price)

#Exercise 3
#Write Program using Flowchart

#dec variables
hits = 0
atBat = 0
battingAverage = 0.0
#input
hits = int(input("Enter the numbert of hits: "))
atBat = int(input("Enter the number of times at bat: "))
#process
battingAverage = hits/atBat
#output
print("The player's batting average is ", battingAverage)
