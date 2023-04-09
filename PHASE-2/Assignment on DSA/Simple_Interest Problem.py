#Question 1
'''
Write a python lambda expression for calculating simple interest.
If simple interest is greater than 1000, display as “Platinum Member”, otherwise “Gold Member”.
Use the below formula to calculate the simple interest.
simple_interest=(principal_amount*duration in years*rate_of_interest)/100
'''

#Program
simple_interest = lambda P, R, T: (P * R * T) / 100

P = float(input("Enter the principal amount: "))
T = float(input("Enter the duration in years: "))
R = float(input("Enter the rate of interest: "))

SI = simple_interest(P, R, T)
if SI > 1000:
    membership = "Platinum Member"
else:
    membership = "Gold Member"
print("Simple interest: $", round(SI, 2))
print("Membership level: ", membership)
