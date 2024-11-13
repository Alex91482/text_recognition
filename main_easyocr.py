import easyocr
import os

model_path = 'E:/Programs/easyocr_model/model/'


def execute_v1(path_image: str) -> None:
    """
    Выведет в консоль распознаный текст
    :param path_image: путь до изображения
    :return: ни чего не возвращает
    """
    reader = easyocr.Reader(lang_list=['ru', 'en'], download_enabled=False, model_storage_directory=model_path)
    result = reader.readtext(image=path_image)

    for detection in result:
        print(detection[1])


if __name__ == '__main__':
    path = './temp/000c21928ecf59ddcc3c1ca08a1e7f06c7d9249b.jpg'

    if os.path.isfile(path):
        print("Файл существует")
        execute_v1(path_image=path)
    else:
        print("Файл не существует")