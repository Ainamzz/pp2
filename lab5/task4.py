#проверяет наличие одной заглавной буквы,за которой следуют строчные буквы
import re
def find(text):
    a = r'\b[A-Z][a-z]+\b'
    res = re.findall(a, text)
    return res
b = input("Enter a sentence: ")
sequences = find(b)
if sequences:
    print("Found sequences:", sequences)
else:
    print("Does not match")
