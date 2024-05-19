import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import time
import csv
import schedule

data_city = ''
headers = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    )
def count_home(min_price, max_price):
    url = f"https://novosibirsk.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p=1&region=4897"
    response = requests.get(url, headers=headers.generate())
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find("div", class_="_93444fe79c--serp--bTAO_ _93444fe79c--serp--light--moDYM")
    count_home = data.find("h5", class_="_93444fe79c--color_black_100--kPHhJ _93444fe79c--lineHeight_20px--tUURJ _93444fe79c--fontWeight_bold--ePDnv _93444fe79c--fontSize_14px--TCfeJ _93444fe79c--display_block--pDAEx _93444fe79c--text--g9xAG _93444fe79c--text_letterSpacing__normal--xbqP6").text
    num = int(''.join(filter(lambda i: i.isdigit(), count_home)))
    num /= 25
    if num == 0:
        return 0
    elif num == int(num):
        return int(num)
    return int(num) + 1

def get_url():
    for i in range(15):
        num_site_page = 1
        min_price = 1
        max_price = 1_000_000
        list_city = [
            f"https://chelyabinsk.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=5048&sort=creation_date_desc",
            f"https://ekb.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=4743&sort=creation_date_desc",
            f"https://kazan.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=4777&sort=creation_date_desc",
            f"https://krasnodar.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=4820&sort=creation_date_desc",
            f"https://krasnoyarsk.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=4827&sort=creation_date_desc",
            f"https://www.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=1&sort=creation_date_desc",
            f"https://nn.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=4885&sort=creation_date_desc",
            f"https://novosibirsk.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=4897&sort=creation_date_desc",
            f"https://omsk.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=4914&sort=creation_date_desc",
            f"https://perm.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=4927&sort=creation_date_desc",
            f"https://samara.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=4966&sort=creation_date_desc",
            f"https://spb.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=2&sort=creation_date_desc",
            f"https://ufa.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=176245&sort=creation_date_desc",
            f"https://volgograd.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=4704&sort=creation_date_desc",
            f"https://voronezh.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice={max_price}&minprice={min_price}&offer_type=flat&p={num_site_page}&region=4713&sort=creation_date_desc"
        ]
        list_data_add = [
            "data_Chelyabinsk.csv",
            "data_EKB.csv",
            "data_Kazan.csv",
            "data_Krasnodar.csv",
            "data_Krasnoyyarsk.csv",
            "data_Moscow.csv",
            "data_NN.csv",
            "data_Novosibirsk.csv",
            "data_Omsk.csv",
            "data_Perm.csv",
            "data_Samara.csv",
            "data_SPB.csv",
            "data_Ufa.csv",
            "data_Volgograd.csv",
            "data_Voronezh.csv"
        ]
        global data_city
        data_city = list_data_add[i]
        url = list_city[i]
        for j in range(1):
            try:
                min_price += 1_000_000
                max_price += 1_000_000
                count_page = count_home(min_price, max_price)

                for num_site_page in range(1): #, count_page + 1
                    response = requests.get(url, headers=headers.generate())
                    soup = BeautifulSoup(response.text, "lxml")
                    data = soup.find("div", class_="_93444fe79c--serp--bTAO_ _93444fe79c--serp--light--moDYM").find("div", class_="_93444fe79c--wrapper--W0WqH")
                    card_url = data.find_all("article", class_="_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc")
                    time_add = data.find_all("span", class_="_93444fe79c--color_gray60_100--MlpSF _93444fe79c--lineHeight_20px--tUURJ _93444fe79c--fontWeight_normal--P9Ylg _93444fe79c--fontSize_14px--TCfeJ _93444fe79c--display_inline--bMJq9 _93444fe79c--text--g9xAG _93444fe79c--text_letterSpacing__normal--xbqP6")
                    k = 0
                    i = 0
                    while k < len(time_add):
                        list_forbidden_worlds = ["неделю", "недели", "месяца", "месяц", "полгода", "год"]
                        for word in list_forbidden_worlds:
                            if word in time_add[k].text:
                                break
                        else:
                            link = card_url[i].find("a", class_="_93444fe79c--media--9P6wN").get("href")
                            yield link
                        i += 1
                        k += 2
                        time.sleep(0.3)
            except Exception as ex:
                print("false1")
                continue


def array():
    for get_link in get_url():
        time.sleep(1)
        try:
            response_object = requests.get(get_link, headers=headers.generate())
            soup = BeautifulSoup(response_object.text, "lxml")
            data_object = soup.find("div", class_="a10a3f92e9--page--OYngf")

            name = data_object.find("div", class_="a10a3f92e9--container--pWxZo").find("h1", class_="a10a3f92e9--title--vlZwT").text
            index_for_name = name.find(',')
            name = name[:index_for_name]


            price = data_object.find("div", class_="a10a3f92e9--amount--ON6i1").find("span").text
            price = int(''.join(filter(lambda i: i.isdigit(), price)))

            price_for_metr = data_object.find("div", class_="a10a3f92e9--item--iWTsg").text
            price_for_metr = int(price_for_metr[12: -4].replace(" ", ""))

            floor_from_block = data_object.find_all("div", class_="a10a3f92e9--item--Jp5Qv")
            floor = 'Null'
            for i in floor_from_block:
                if i.text[:4] == "Этаж":
                    floor = i.text[4:]
            index_for_floor = floor.find(' ')
            floor_object = int(floor[:index_for_floor])
            index_for_floors = floor.rfind(' ')
            total_floors = int(floor[index_for_floors + 1:])

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
            year_house = 'Null'  # Год постройки
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
                    year_house = int(data_block[i+1].text.strip())

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

            count = 1
            print(f"add {count} object")

            with open(data_city, 'a', encoding="utf8", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(
                (
                    name, price, price_for_metr, floor_object, total_floors, type_of_home, square_home, live_square,
                    kitchen_square, height_ceiling, bathroom, balcony, repair, year_house, garbage_chute, type_home,
                    type_of_overlap, entrances, heating, accident_rate, gas_supply, finishing, number_of_elevators,
                    address, get_link
                )
                )
        except Exception as ex:
            print("false2")
            continue




def main():
    schedule.every(7).days.at("21:00").do(array)

    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()