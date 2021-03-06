# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (
# характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})


r = 0
products = []
names = []
prices = []
amounts = []
units = []
answer = ''
while answer != "N":
    name = input("название ")
    price = int(input("цена "))
    amount = int(input("количество "))
    unit = input("единица измерения ").lower()
    my_tuple = (r+1, {"название": name, "цена": price, "количество": amount, "eд": unit})
    products.append(my_tuple)
    r += 1
    names.append(name)
    prices.append(price)
    amounts.append(amount)
    if unit not in units:
        units.append(unit)
    answer = input("хотите ввести следующий товар (Y/N) ").upper()
print(products)

# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {“название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7], “ед”: [“шт.”]}

my_products = {
    "название": names,
    "цена": prices,
    "количество": amounts,
    "ед": units
}
print(my_products)