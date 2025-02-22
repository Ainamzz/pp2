#для разделения строки на основе заглавных букв
import re
text = input("Enter a string: ")
split = re.findall(r'[A-Z][a-z]*', text)
print(split)