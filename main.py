def calculate_order():
    print("--- Система расчета заказов Ателье ---")
    
    types = {"платье": 1500, "брюки": 1200, "пальто": 3000}
    
    item = input("Введите тип изделия (платье/брюки/пальто): ").lower()
    if item not in types:
        print("Ошибка: Тип изделия не найден.")
        return

    try:
        complexity = float(input("Коэффициент сложности (от 1.0 до 2.0): "))
        meters = float(input("Расход ткани (в метрах): "))
        price_per_meter = float(input("Цена ткани за метр: "))
        
        work_cost = types[item] * complexity
        material_cost = meters * price_per_meter
        total = work_cost + material_cost
        
        print(f"\nИтог: Работа {work_cost} + Ткань {material_cost} = {total} руб.")
    except ValueError:
        print("Ошибка: Вводите только числа.")

calculate_order()
