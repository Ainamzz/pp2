#ищет последовательности строчных букв,соединённых одним подчёркиванием
import re
def sequence(txt):
    a = r'\b[a-z]+_[a-z]+\b'
    match = re.findall(a, txt)
    return match
txt = input("Enter a sentence: ")
matches = sequence(txt)
if matches:
    print(f"Found matches: {matches}")
else:
    print("Does not match")