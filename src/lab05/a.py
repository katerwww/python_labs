import csv, json, sys, os
from pathlib import Path
def is_valid_json_file(file_path: str) -> bool:
    try:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return False
        
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file) #pагружает JSON данные из файла.
            return isinstance(json_data, list) and len(json_data) > 0 and all(isinstance(item, dict) for item in json_data) # является ли списком, список не пустой, все элементы списка являются словарями
    except:
        return False

def is_valid_csv_file(file_path: str) -> bool:
    try:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return False
            
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)  
            header = next(reader, None) #читает CSV файл и получает первую строку
            return header is not None and len(header) > 0
    except:
        return False

def json_to_csv(json_path: str, csv_path: str) -> None:
    if not is_valid_json_file(json_path): # JSON файл не соотвествует критериям, выводит ошибку и завершит программу
        print("ValueError: Input file is not a valid JSON or is empty")
        sys.exit(1) 
    json_path=Path(json_path)
    csv_path=Path(csv_path)
    if json_path.suffix.lower() != ".json": #проверка расширения файлов, lower-метод преобразования в нижний регистр
        raise ValueError(f"Неверный формат входного файла: ожидается .json")
    if csv_path.suffix.lower() != ".csv":  #проверка расширения файлов
        raise ValueError(f"Неверный формат выходного файла: ожидается .csv")
    

    with open(json_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file) 

    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=json_data[0].keys()) #создает CSV файл с заголовками из ключей первого элемента JSON, названия колонок = ключи первого элемента
        writer.writeheader()  
        writer.writerows(json_data) 

def csv_to_json(csv_path: str, json_path: str) -> None:
    if not is_valid_csv_file(csv_path):
        print("ValueError: Input file is not a valid CSV or is empty")
        sys.exit(1)
    json_path=Path(json_path)
    csv_path=Path(csv_path)
    if json_path.suffix.lower() != ".json":
        raise ValueError(f"Неверный формат выходного файла: ожидается .json")
    if csv_path.suffix.lower() != ".csv":
        raise ValueError(f"Неверный формат входного файла: ожидается .csv")

    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  #читает CSV как список словарей
        data = list(reader) 
    
    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4) 
csv_to_json(r"C:\Users\lezgi\Desktop\python_labs\data\samples\people.csv",r"C:\Users\lezgi\Desktop\python_labs\data\out\people_from_json.json")

json_to_csv( r"C:\Users\lezgi\Desktop\python_labs\data\samples\people.json",  r"C:\Users\lezgi\Desktop\python_labs\data\out\people_from_csv.csv" )