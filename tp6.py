# Shopping Discount Calculator

def calculate_final_price(original_price: float, discount_percentage: float = 0) -> float:
   
    discount_fraction = discount_percentage / 100
   
    discount_amount = original_price * discount_fraction

    final_price = original_price - discount_amount

    return final_price

print(calculate_final_price(100))          
print(calculate_final_price(100, 20))      
print(calculate_final_price(250, 15))     

# Invoice Line Item Processor

def calculate_invoice_total(tax_rate: float, *item_costs: float) -> float:
    
    subtotal = sum(item_costs)

    tax_amount = subtotal * (tax_rate / 100)

    total = subtotal + tax_amount

    total_rounded = round(total, 2)

    return total_rounded

print(calculate_invoice_total(8))                    
print(calculate_invoice_total(10, 100))               
print(calculate_invoice_total(5, 50, 25, 25))        
print(calculate_invoice_total(7.5, 20.99, 15.50))     

# Employee Profile Builder

def create_employee_profile(employee_id: str, department: str, **additional_info) -> tuple[str, dict]:

    employee_dict = {
        "employee_id": employee_id,
        "department": department
    }
 
    employee_dict.update(additional_info)

    summary = f"Employee ID: {employee_id}, Department: {department}"

    return summary, employee_dict

summary, profile = create_employee_profile(
    "EMP001", 
    "Engineering", 
    name="Alice", 
    salary=75000, 
    remote=True
)

print(summary)


print(profile)


summary2, profile2 = create_employee_profile("EMP002", "HR")
print(summary2) 
print(profile2)  

# Loan Payment Calculator Factory

def create_payment_calculator(
    principal: float,
    annual_rate: float,
    years: int,
    compounds_per_year: int = 12
):

    def calculate_payment() -> float:
    
        total_periods = years * compounds_per_year
        if annual_rate == 0:
            payment = principal / total_periods
        else:
            rate_per_period = (annual_rate / 100) / compounds_per_year
            payment = principal * rate_per_period / (1 - (1 + rate_per_period) ** -total_periods)
        
        return round(payment, 2)

    return calculate_payment

mortgage_calculator = create_payment_calculator(principal=300000, annual_rate=4, years=30)
print(mortgage_calculator())  

zero_interest_calculator = create_payment_calculator(principal=12000, annual_rate=0, years=1)
print(zero_interest_calculator())  

# Task Dependency Estimator

def estimate_project_hours(tasks):
   
    if not hasattr(estimate_project_hours, "call_count"):
        estimate_project_hours.call_count = 0
    estimate_project_hours.call_count += 1

 
    def helper(task_list):
        total = 0  
        max_parallel = 0  

        for task in task_list:

            if "subtasks" in task and task["subtasks"]:
                hours = helper(task["subtasks"])
            else:
                hours = task["hours"]

            if task.get("parallel") == True:
                if hours > max_parallel:
                    max_parallel = hours
            else:
                total = total + hours  

        return total + max_parallel

    return helper(tasks)


tasks = [
    {"name": "Design", "hours": 4},
    {"name": "Development", "hours": 10, "subtasks": [
        {"name": "API", "hours": 6},
        {"name": "DB", "hours": 8, "parallel": True}
    ]},
    {"name": "Testing", "hours": 3}
]

print(estimate_project_hours(tasks))
print(estimate_project_hours.call_count)
