"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    phones = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    total_sum = 0
    total_count = 0
    for phone in phones:
        sum_phone = 0
        count_phone = 0
        for price in phone['items_sold']:
            sum_phone += price
            count_phone += 1
            total_sum += price
            total_count += 1
        print(f"Cуммарное количество продаж для {phone['product']} {sum_phone}")
        average_quantity_phone = sum_phone / count_phone
        print(f"Среднее количество продаж для {phone['product']} {round(average_quantity_phone, 2)}")

    average_quantity_phones = total_sum / total_count
    print(f"Суммарное количество продаж всех товаров {total_sum}")
    print(f"Вывести среднее количество продаж всех товаров {round(average_quantity_phones, 2)}")


if __name__ == "__main__":
    main()
