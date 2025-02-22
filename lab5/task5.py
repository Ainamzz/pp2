#проверяет наличие 'a', за которой следует любая последовательность символов и заканчивается на 'b'
import re
a = r"a.*b"
text = input("Enter a word: ")
if re.fullmatch(a, text):
    print("Matches")
else:
    print("Does not match!")