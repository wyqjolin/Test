
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Please enter the portion of salary to be saved: "))
total_cost = int(input("Please enter the cost of your dream home: "))
month_salary = annual_salary/12

portion_down_payment = 0.25
cost = portion_down_payment * total_cost
current_savings = 0
r = 0.04
month = 0

while current_savings <= cost:
    current_savings = current_savings + current_savings*r/12 +month_salary*portion_saved
    month += 1

print("Number of months: ",month)