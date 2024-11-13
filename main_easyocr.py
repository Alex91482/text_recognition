import easyocr
import os


def execute_v1(path_image: str) -> None:
    reader = easyocr.Reader(['ru', 'en'])
    result = reader.readtext(path_image)

    for detection in result:
        print(detection[1])


if __name__ == '__main__':
    path = './temp/000c21928ecf59ddcc3c1ca08a1e7f06c7d9249b.jpg'
    if os.path.isfile(path):
        print("Файл существует")
        execute_v1(path)
    else:
        print("Файл не существует")