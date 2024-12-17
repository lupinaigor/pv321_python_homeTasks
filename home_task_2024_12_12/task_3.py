# Завдання 3
# Щороку ваша компанія надає різним державним установам
# фінансову звітність. Залежно від установи, формати звітності
# різні. Використовуючи механізм декораторів вирішіть питання
# звітності для установ.


import json
import xml.etree.ElementTree as ET

# Базова функція формування звіту
def financial_report(data):
    report = "\n".join([f"{key}: {value}" for key, value in data.items()])
    return report

# Декоратор для формату JSON
def json_format_decorator(func):
    def wrapper(data):
        report = func(data)
        json_report = json.dumps(data, indent=4, ensure_ascii=False)
        return f"JSON Report:\n{json_report}"
    return wrapper

# Декоратор для формату XML
def xml_format_decorator(func):
    def wrapper(data):
        report = func(data)
        root = ET.Element("FinancialReport")
        for key, value in data.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        xml_report = ET.tostring(root, encoding="unicode")
        return f"XML Report:\n{xml_report}"
    return wrapper

# Дані звіту
data = {
    "Year": 2024,
    "Revenue": 2500000,  # Дохід
    "Expenses": 1800000,  # Витрати
    "Profit": 700000,  # Прибуток
    "EmployeeCount": 120,  # Кількість співробітників
    "MarketShare": "15%",  # Частка ринку
    "GrowthRate": "12%",  # Темпи зростання
    "NewClients": 35,  # Нові клієнти за рік
    "LostClients": 5,  # Втрачені клієнти за рік
    "AverageDealSize": 55000,  # Середній розмір угоди
    "ReturnOnInvestment": "18%"  # Рентабельність інвестицій
}

# Формування звітів для різних установ
@json_format_decorator
def json_report(data):
    return financial_report(data)

@xml_format_decorator
def xml_report(data):
    return financial_report(data)

# Виклик звітів
print(json_report(data))
print(xml_report(data))

