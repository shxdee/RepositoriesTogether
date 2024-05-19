from pars_data import array
from removing_duplicates import rem_dubl
from ref_address import rename_address
from geo_coders import run_geo
from ref_coordinates import ref_coor
from destance_to_centr import update_datasets_with_distances
import os


def save_checkpoint(step):
    with open("checkpoint.txt", "w") as file:
        file.write(step)


def load_checkpoint():
    if os.path.exists("checkpoint.txt"):
        with open("checkpoint.txt", "r") as file:
            return file.read()
    return ""


def main():
    checkpoint = load_checkpoint()

    if not checkpoint or checkpoint == "array":
        print("начался сбор данных")
        array()
        save_checkpoint("rem_dubl")

    if not checkpoint or checkpoint == "rem_dubl":
        print("началась чистка от дубликатов")
        rem_dubl()
        save_checkpoint("rename_address")

    if not checkpoint or checkpoint == "rename_address":
        print("началось редактирование адресов")
        rename_address()
        save_checkpoint("run_geo")

    if not checkpoint or checkpoint == "run_geo":
        print("началось геокодирование данных")
        run_geo()
        save_checkpoint("ref_coor")

    if not checkpoint or checkpoint == "ref_coor":
        print("началась обработка координат в 2 столбца")
        ref_coor()
        save_checkpoint("update_datasets_with_distances")

    if not checkpoint or checkpoint == "update_datasets_with_distances":
        print("начался расчет от центра до дома ")
        update_datasets_with_distances()
        save_checkpoint("completed")

    if checkpoint == "completed":
        print("конец работы")
        # при завершении удаляем файл с чекпоинтами
        os.remove("checkpoint.txt")


if __name__ == "__main__":
    main()


    