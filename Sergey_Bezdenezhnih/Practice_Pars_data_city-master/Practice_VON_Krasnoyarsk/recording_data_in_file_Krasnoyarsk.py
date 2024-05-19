from f_scrap_home_Krasnoyarsk import array
import csv


def data_writing(parametr):
    with open ("data_home_Krasnoyarsk.csv", 'w', encoding="utf8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ("name", "price", "price_for_metr", "floor_object", "total_floors", "type_of_home", "square_home", "live_square", "kitchen_square", "height_ceiling", "bathroom", "balcony", "repair", "yer_home", "garbage_chute", "type_home", "type_of_overlap", "entrances", "heating", "accident_rate", "gas_supply", "finishing", "number_of_elevators", "address", "link")
        )
        count = 0
    for a in parametr:
        count += 1
        print(f"data block {count}")
        name = a[0]
        price = a[1]
        price_for_metr = a[2]
        floor = a[3]
        index_for_floor = floor.find(' ')
        floor_object = int(floor[:index_for_floor])
        index_for_floors = floor.rfind(' ')
        total_floors = int(floor[index_for_floors + 1:])
        type_of_home = a[4]  # Тип жилья
        square_home = a[5]  # Общая площадь
        live_square = a[6]  # Жилая площадь
        kitchen_square = a[7]  # Площадь кухни
        height_ceiling = a[8]  # Высота потолков
        bathroom = a[9]  # Санузел
        balcony = a[10]  # Балкон/лоджия
        repair = a[11]  # Ремонт
        yer_home = a[12]  # Год постройки
        garbage_chute = a[13]  # Мусоропровод
        type_home = a[14]  # Тип дома
        type_of_overlap = a[15]  # Тип перекрытий
        entrances = a[16]  # Подъезды
        heating = a[17]  # Отопление
        accident_rate = a[18]  # Аварийность
        gas_supply = a[19]  # Газоснабжение
        finishing = a[20]  # Отделка
        number_of_elevators = a[21]  # Количество лифтов
        address = a[22]
        link = a[23]
        with open("data_home_Krasnoyarsk.csv", 'a', encoding="utf8", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                (name, price, price_for_metr, floor_object, total_floors, type_of_home, square_home, live_square, kitchen_square, height_ceiling, bathroom, balcony, repair, yer_home, garbage_chute, type_home, type_of_overlap, entrances, heating, accident_rate, gas_supply, finishing, number_of_elevators, address, link)
            )


data_writing(array())