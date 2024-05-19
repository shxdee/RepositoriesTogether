import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import time

headers = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    )
def count_home(min_price, max_price):
    url = f"https://voronezh.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p=1&region=4713"
    response = requests.get(url, headers=headers.generate())
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find("div", class_="_93444fe79c--serp--bTAO_ _93444fe79c--serp--light--moDYM")
    count_home = data.find("h5", class_="_93444fe79c--color_black_100--kPHhJ _93444fe79c--lineHeight_20px--tUURJ _93444fe79c--fontWeight_bold--ePDnv _93444fe79c--fontSize_14px--TCfeJ _93444fe79c--display_block--pDAEx _93444fe79c--text--g9xAG _93444fe79c--text_letterSpacing__normal--xbqP6").text
    num = int(''.join(filter(lambda i: i.isdigit(), count_home)))
    num /= 25
    if num == 0:
        return 0
    return int(num) + 1


def get_url():
    min_price = 700_001
    max_price = 1_000_000
    for i in range(300):
        try:
            min_price += 300_000
            max_price += 300_000
            count_page = count_home(min_price, max_price)

            for num_site_page in range(1, count_page + 1):
                url = f"https://voronezh.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=4713"
                response = requests.get(url, headers=headers.generate())
                soup = BeautifulSoup(response.text, "lxml")
                data = soup.find("div", class_="_93444fe79c--serp--bTAO_ _93444fe79c--serp--light--moDYM").find("div", class_="_93444fe79c--wrapper--W0WqH")
                card_url = data.find_all("article", class_="_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc")

                for i in card_url:
                    link = i.find("a", class_="_93444fe79c--media--9P6wN").get("href")
                    yield link
        except Exception as ex:
            continue


def array():
    for get_link in get_url():
        time.sleep(2)
        try:
            response_object = requests.get(get_link, headers=headers.generate())
            soup = BeautifulSoup(response_object.text, "lxml")
            data_object = soup.find("div", class_="a10a3f92e9--page--OYngf")

            name = data_object.find("div", class_="a10a3f92e9--container--pWxZo").find("h1", class_="a10a3f92e9--title--vlZwT").text
            index_for_name = name.find(',')
            name = name[:index_for_name]


            price = data_object.find("div", class_="a10a3f92e9--amount--ON6i1").find("span").text
            print(price)
            price = int(''.join(filter(lambda i: i.isdigit(), price)))

            price_for_metr = data_object.find("div", class_="a10a3f92e9--item--iWTsg").text
            price_for_metr = int(price_for_metr[12: -4].replace(" ", ""))

            floor_from_block = data_object.find_all("div", class_="a10a3f92e9--item--Jp5Qv")
            floor = 'Null'
            for i in floor_from_block:
                if i.text[:4] == "Этаж":
                    floor = i.text[4:]

            data_block = data_object.find("div", class_="a10a3f92e9--container--rGqFe").find_all("span")

            # о квартире и дом
            type_of_home = 'Null' # Тип жилья
            square_home = 'Null' # Общая площадь
            live_square = 'Null' # Жилая площадь
            kitchen_square = 'Null' # Площадь кухни
            height_ceiling = 'Null' # Высота потолков
            bathroom = 'Null' # Санузел
            balcony = 'Null' # Балкон/лоджия
            repair = 'Null' # Ремонт
            yer_home = 'Null'  # Год постройки
            garbage_chute = 'Null'  # Мусоропровод
            type_home = 'Null'  # Тип дома
            type_of_overlap = 'Null'  # Тип перекрытий
            entrances = 'Null'  # Подъезды
            heating = 'Null'  # Отопление
            accident_rate = 'Null'  # Аварийность
            gas_supply = 'Null'  # Газоснабжение
            finishing = 'Null' # Отделка
            number_of_elevators = 'Null' # Количество лифтов

            for i in range(len(data_block)):
                if data_block[i].text == "Тип жилья":
                    type_of_home = data_block[i+1].text

            for i in range(len(data_block)):
                if data_block[i].text == "Общая площадь":
                    square_home = float(data_block[i+1].text.replace(",", ".").strip())

            for i in range(len(data_block)):
                if data_block[i].text == "Жилая площадь":
                    live_square = float(data_block[i+1].text.replace(",", ".").strip())

            for i in range(len(data_block)):
                if data_block[i].text == "Площадь кухни":
                    kitchen_square = float(data_block[i+1].text.replace(",", ".").strip())

            for i in range(len(data_block)):
                if data_block[i].text == "Высота потолков":
                    height_ceiling = data_block[i+1].text
                    height_ceiling = height_ceiling[:-2]
                    height_ceiling = float(height_ceiling.replace(",", ".").strip())

            for i in range(len(data_block)):
                if data_block[i].text == "Санузел":
                    bathroom = data_block[i+1].text
                    bathroom = int(bathroom[:1])

            for i in range(len(data_block)):
                if data_block[i].text == "Балкон/лоджия":
                    balcony = data_block[i+1].text
                    balcony = int(balcony[:1])

            for i in range(len(data_block)):
                if data_block[i].text == "Ремонт":
                    repair = data_block[i+1].text

            for i in range(len(data_block)):
                if data_block[i].text == "Год постройки":
                    yer_home = int(data_block[i+1].text.strip())

            for i in range(len(data_block)):
                if data_block[i].text == "Мусоропровод":
                    garbage_chute = data_block[i+1].text

            for i in range(len(data_block)):
                if data_block[i].text == "Тип дома":
                    type_home = data_block[i+1].text

            for i in range(len(data_block)):
                if data_block[i].text == "Тип перекрытий":
                    type_of_overlap = data_block[i+1].text

            for i in range(len(data_block)):
                if data_block[i].text == "Подъезды":
                    entrances = int(data_block[i+1].text.strip())

            for i in range(len(data_block)):
                if data_block[i].text == "Отопление":
                    heating = data_block[i+1].text

            for i in range(len(data_block)):
                if data_block[i].text == "Аварийность":
                    accident_rate = data_block[i+1].text

            for i in range(len(data_block)):
                if data_block[i].text == "Газоснабжение":
                    gas_supply = data_block[i+1].text

            for i in range(len(data_block)):
                if data_block[i].text == "Отделка":
                    finishing = data_block[i+1].text

            for i in range(len(data_block)):
                if data_block[i].text == "Количество лифтов":
                    number_of_elevators = data_block[i+1].text
                    number_of_elevators = int(number_of_elevators[:1].strip())

            address = data_object.find("div", class_="a10a3f92e9--header-information--w7fS9").find("span").get("content")

            yield name, price, price_for_metr, floor, type_of_home, square_home, live_square, kitchen_square, height_ceiling, bathroom, balcony, repair, yer_home, garbage_chute, type_home, type_of_overlap, entrances, heating, accident_rate, gas_supply, finishing, number_of_elevators, address, get_link

        except Exception as ex:
            print("false")
            continue