from FunctionSalary import calculate_salary

def test_correct_salary():
    # Исходные данные
    base_salary = 5000
    cargo_coefficient = 0.01
    cargo_volume = 700000
    bonuses = 500
    deductions = 200

    # Вызов функции
    month_salary = calculate_salary(base_salary, cargo_coefficient, cargo_volume, bonuses, deductions)
    # Ожидаемый результат
    expected_salary = (base_salary + (cargo_coefficient * cargo_volume) + bonuses - deductions)

    # Проверка результата
    assert month_salary == expected_salary, f"Test failed: Expected {expected_salary}, but got {month_salary}"
    print("Correct test passed!")

# Запуск правильного теста
test_correct_salary()