import os
import csv
import sys
from pathlib import Path
from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    if not os.path.exists(csv_path):
        print("FileNotFoundError")
        sys.exit(1)  # завершает программу с ошибкой 1
    xlsx_path = Path(xlsx_path)
    csv_path = Path(csv_path)
    if (
        xlsx_path.suffix.lower() != ".xlsx"
    ):  # получает расширение файла,преобразует в нижний регистр
        raise ValueError(f"Неверный формат выходного файла: ожидается .xlsx")
    if csv_path.suffix.lower() != ".csv":
        raise ValueError(f"Неверный формат входного файла: ожидается .csv")

    if os.path.getsize(csv_path) == 0:  # получает размер файла в байтах
        print("ValueError")
        sys.exit(1)
    wb = Workbook()  # c
    ws = wb.active  # получает активный лист
    ws.title = "Sheet1"  # устанавливает название листа "Sheet1"

    with open(csv_path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)  # создает объект для чтения CSV построчно
        for row in reader:
            ws.append(row)
    for column_cells in ws.columns:
        max_length = 0
        column_letter = column_cells[0].column_letter  # получает букву колонки
        for cell in column_cells:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        ws.column_dimensions[column_letter].width = max(
            max_length + 2, 8
        )  # обращается к настройкам ширины конкретной колонки, устанавливает ширину колонки, максимальная длина + 2 символа для отступа, 8- выбирает большее значение между расчитанной шириной и минимальной шириной 8
    wb.save(xlsx_path)


csv_to_xlsx(
    r"C:\Users\lezgi\Desktop\python_labs\data\samples\cities.csv",
    r"C:\Users\lezgi\Desktop\python_labs\data\out\people.xlsx",
)
