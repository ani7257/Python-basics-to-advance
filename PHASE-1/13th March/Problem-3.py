n_adults=int(input("Enter the number of adults:"))
n_childs=int(input("Enter the number of child:"))
total=((n_adults*37550.0)+((n_childs*37550.0)/3))
print(total)
total1=total*0.07
total2=total+total1
print("With your service tax",total2)

total_amount=total2*0.90
print(total_amount)

