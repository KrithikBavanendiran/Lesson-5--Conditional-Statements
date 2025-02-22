value=float(input("Please enter the value: "))
cost=float(input("Please enter the cost: "))
if (cost>value):
    amount=cost-value
    print("Total Profit={0}".format(amount))
else:
    print("No profit!")