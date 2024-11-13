import cv2
import pytesseract
import os


"""Выведет в консоль распознвный текст"""
def execute_v2(path_to_immage: str) -> None:
    # Путь для подключения tesseract
    pytesseract.pytesseract.tesseract_cmd = 'E:\\Programs\\tesseract\\tesseract.exe'
    # Подключение фото
    img = cv2.imread(path_to_immage)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    config = r' --oem 1 --psm 3'
    result = pytesseract.image_to_string(img, config=config)
    print(result)

"""Выделит на изображении распознвный текст"""
def execute_v1(path_to_immage: str) -> None:
    # Путь для подключения tesseract
    pytesseract.pytesseract.tesseract_cmd = 'E:\\Programs\\tesseract\\tesseract.exe'
    # Подключение фото
    img = cv2.imread(path_to_immage)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Будет выведен весь текст с картинки
    config = r'--oem 3 --psm 6'
    #config = r'-l rus --oem 1 --psm 3'
    # print(pytesseract.image_to_string(img, config=config))
    data = pytesseract.image_to_data(img, config=config)
    # Перебираем данные про текстовые надписи
    for i, el in enumerate(data.splitlines()):
        if i == 0:
            continue

        el = el.split()
        try:
            # Создаем подписи на картинке
            x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
            cv2.putText(img, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
        except IndexError:
            print("Операция была пропущена")

    # Отображаем фото
    cv2.imshow('Result', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    path = './temp/000c21928ecf59ddcc3c1ca08a1e7f06c7d9249b.jpg'
    if os.path.isfile(path):
        print("Файл существует")
        #execute_v1(path)
        execute_v2(path)
    else:
        print("Файл не существует")


