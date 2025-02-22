#заменяет все пробелы, запятые и точки на двоеточие
import re
text = input("Enter a string: ")
res = re.sub(r"[ ,.]", ":", text)
print(res)
