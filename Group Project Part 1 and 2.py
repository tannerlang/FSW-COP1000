x= 10
if x==5:
    print("Hello")
elif x < 5:
    print("Goodbye")
elif x >= 10:
    print("IDK")
    
# x=5, Hello
# x=-2, Goodbye
# x=10, IDK
# x=8, No Result
# x=18, IDK


#Part 2
#x = input("Enter a Number")
#if int(x) in range(0,6):                #checks 0, 1, 2, 3, 4, 5
#    print("between 0 and 5", x)
#elif int(x) in range(6,11):             #checks 6,7,8,9,10
#    print("between 6 and 10", x)
#else:
#    print("out of range")
    
# Output of 5 = between 0 and 5
# Output of -2 = out of range
# Output of 6 = between 6 and 10
# Output of 10 = between 6 and 10
# Output of 11 = out of range

#Part 2.2
x = input("Enter a Number")
if int(x) >=0 and int(x) <=5:              #checks 0, 1, 2, 3, 4, 5
    print("between 0 and 5", x)
elif int(x) >5 and int(x) <=10:             #checks 6,7,8,9,10
    print("between 6 and 10", x)
else:
    print("out of range")

# Output of 5 = between 0 and 5
# Output of -2 = out of range
# Output of 6 = between 6 and 10
# Output of 10 = between 6 and 10
# Output of 11 = out of range

