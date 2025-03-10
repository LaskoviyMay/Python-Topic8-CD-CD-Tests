def calculate_salary(base_salary, cargo_coefficient, cargo_volume, bonuses, deductions):
    """
    Function to calculate month salary 

    """
    # Calculate salary
    salary = base_salary + (cargo_coefficient * cargo_volume) + bonuses - deductions

    # Check salary
    if salary < base_salary:
        salary = base_salary

    # Round salary
    return round(salary, 2)


# Parameters
base_salary = 10000
cargo_coefficient = 0.01
cargo_volume = 700000
bonuses = 500
deductions = 200

# Calculate month salary
month_salary = calculate_salary(base_salary, cargo_coefficient, cargo_volume, bonuses, deductions)

# Print result
print(f"Salary is: {month_salary} $")
