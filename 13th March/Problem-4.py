x=int(input("Enter the 5 rs coin:"))
y=int(input("Enter the 1 rs coin:"))
z=int(input("Amount to be Made:"))
print(z//5)
if ((y+5*x)>=z):
    print("5 rs coin needed:",z//5)
    print("1 rs coin needed:",z-(x*5))
else:
    print("-1")


