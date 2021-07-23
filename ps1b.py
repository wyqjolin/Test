
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentof your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as decimal: "))

month_salary = annual_salary/12
portion_down_payment = 0.25
cost = portion_down_payment * total_cost
current_savings = 0
r = 0.04
month = 0

while current_savings <= cost:
    current_savings = current_savings + current_savings*r/12 +month_salary*portion_saved
    month += 1
    if month % 6 == 0: 
        month_salary = month_salary + month_salary*semi_annual_raise

print("Number of months: ",month)