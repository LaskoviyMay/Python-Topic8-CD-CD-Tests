def calculate_salary(base_salary, cargo_coefficient, cargo_volume, bonuses, deductions):

    salary = base_salary + (cargo_coefficient * cargo_volume) + bonuses - deductions

    if salary < base_salary:
        salary = base_salary

    return round(salary, 2)

route_time = 4

base_salary = 10000
cargo_coefficient = 0.01
cargo_volume = 700000
bonuses = 500
deductions = 200

month_salary = calculate_salary(base_salary, cargo_coefficient, cargo_volume, bonuses, deductions) / route_time

print(f"Salary is: {month_salary} $")
