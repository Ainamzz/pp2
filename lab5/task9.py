#вставляет пробелы перед словами,начинающимися с заглавной буквы
import re
text = input("Enter a string: ")
res = re.sub(r'(?<!^)([A-Z])', r' \1', text)
print(res)