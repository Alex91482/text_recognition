import os
import time
import uuid
import easyocr
import multiprocessing as mp

from multiprocessing import Pool


class Easyocr_Thred:

    model_path = ''

    def __init__(self, path_to_model: str):
        self.model_path = path_to_model

    def execute(self, images_file_paths: list) -> list:
        """
        Точка входа
        :param images_file_paths: список полных путей к изображениям
        :return: список со массивами такста считанного с изображений
        """
        my_list = self.__read_text_from_image(images_file_paths=images_file_paths, model_path=self.model_path)
        return my_list

    def __read_text(self, full_path: str, reader: easyocr.Reader) -> list:
        """
        Полечение текстовых данных
        :param full_path: путь к изображению с которого нужно прочесть текст
        :param reader: ссылка на инициализированный ридер
        :return: список такста считанного с изображения
        """
        result = reader.readtext(image=full_path)
        arr = []
        for detection in result:
            arr.append(detection[1])
        return arr

    def __read_text_from_image(self, images_file_paths: list, model_path: str) -> list:
        """
        Загрузка ридера и сохранение текстовых данных в список
        :param images_file_paths: список полных путей к изображениям
        :param model_path: путь к моделям для их офлайн загрузки
        :return: список со массивами такста считанного с изображений
        """
        path_full = images_file_paths
        arr_all = []
        reader = easyocr.Reader(lang_list=['ru', 'en'], download_enabled=False, model_storage_directory=model_path)
        for file_name in path_full:
            result = self.__read_text(full_path=file_name, reader=reader)
            arr_all.append(result)
        return arr_all


def init_execute_multi(images_path: list) -> None:
    """
    Инициализация для многопоточной реализации
    :param images_path: список полных путей к изображениям
    """
    temp_path = './temp/result/'
    model_path = 'E:/Programs/easyocr_model/model/'

    easyocr_thread = Easyocr_Thred(path_to_model=model_path)
    my_list = easyocr_thread.execute(images_file_paths=images_path)

    file_name = str(uuid.uuid4()) + ".txt"
    my_file = open(temp_path + file_name, "w+")
    for n in range(0, len(my_list)):
        my_file.writelines(my_list[n])
        my_file.write("\n")
    my_file.close()

    print("exit code 0")


def main() -> None:
    """ Однопоточная реализация """
    model_path = 'E:/Programs/easyocr_model/model/'
    path_image = './temp/data/'
    temp_path = './temp/result/'

    files = os.listdir(path_image)
    path_full = list(map(lambda x: path_image + x, files))

    easyocr_thread = Easyocr_Thred(path_to_model=model_path)
    my_list = easyocr_thread.execute(images_file_paths=path_full)

    file_name = str(uuid.uuid4()) + ".txt"
    my_file = open(temp_path + file_name, "w+")
    for n in range(0, len(my_list)):
        my_file.writelines(my_list[n])
        my_file.write("\n")
    my_file.close()

    print("exit code 0")


def main_multi() -> None:
    """ Многопоточная реализация """
    path_image = './temp/data/'
    thread_size = 10
    chunk_size = 10

    files = os.listdir(path_image)
    path_full = list(map(lambda x: path_image + x, files))
    chunks = [path_full[i:i + chunk_size] for i in range(0, len(path_full), chunk_size)]

    if __name__ == '__main__':
        with Pool(thread_size) as p:
            p.map(init_execute_multi, chunks)


if __name__ == '__main__':
    start_time = time.time()
    #main()
    main_multi()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('Elapsed time: ', elapsed_time)
