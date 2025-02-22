#из snake_case в camelCase 
import re
def snake_to_camel(snake):
    return re.sub(r'_([a-z])', lambda match:match.group(1).upper(), snake)
text = input("Enter a snake case string: ")
camel = snake_to_camel(text)
print("Camel case string:", camel)