
annual_salary=int(input("Enter the starting salary:​ "))

def reach_house(annual_salary,guess):             
    total_cost = 1000000     
    semi_annual_raise = 0.07  
    portion_down_payment = 0.25    
    current_savings = 0   
    r = 0.04   
    month = 0  
    payment = portion_down_payment*total_cost 
    month_salary = annual_salary/12
    while month < 36:    
        current_savings = current_savings + current_savings*r/12 + month_salary*guess
        month += 1
        if month % 6 == 0:               
            month_salary = month_salary + month_salary*semi_annual_raise
        if current_savings >= payment-100:    
            return True
    return False

low = 0
high = 10000
bisection_search = 0        
if reach_house(annual_salary,high/10000) == False:
    print("It is not possible to pay the down payment in three years.")
else:      
    while high-low >= 1:
        bisection_search += 1
        ans = (high+low)/2   
        if reach_house(annual_salary,ans/10000):  
            high = ans
        else:
            low = ans      
    print("Best savings rate:%.4f" %(ans/10000)) 
    print("Steps in bisection search:",bisection_search)
