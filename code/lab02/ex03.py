def format_record(rec: tuple[str, str, float]) -> str:

    if not isinstance(rec[0], str) or not rec[0].strip():
        return ValueError
    if not isinstance(rec[1], str) or not rec[1].strip():
        return ValueError
    if not isinstance(rec[2], (float, int)):
        return TypeError
    
    fio = ' '.join(rec[0].strip().split())
    parts = fio.split()

    surname = parts[0]
    initials = ''.join(part[0].upper() + '.' for part in parts[1:]).strip()

    gpa = f"{rec[2]:.2f}"

    result = f"{surname} {initials}, гр. {rec[1].strip()}, GPA {gpa}"
    
    return result

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))