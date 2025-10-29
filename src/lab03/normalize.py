def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = text.casefold() 
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    text = " ".join(text.split()) 
    text = text.strip() 
    return text

print(normalize("ПрИвЕт\nМИр\t")) 
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))

