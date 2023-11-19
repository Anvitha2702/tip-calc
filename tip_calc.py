print("Welcome to the tip calculator")
bill=float(input("What was the total bill?Rs. "))
tip=int(input("What percentage of tip would you like to give? 10, 12 or 15?"))
people=int(input("How many people to split the bill?"))
tip_percent=tip/100
total_bill=(bill*tip_percent)+bill
each_person_bill="{:.2f}".format((total_bill/people))
print(f"Each person should pay: Rs. {each_person_bill}")