#проверяет наличие b(2-3 штук) после a
import re
txt = input("Enter a word: ")
a = r"ab{2,3}"
if re.fullmatch(a, txt):
    print("Matches")
else:
    print("Does not match!")