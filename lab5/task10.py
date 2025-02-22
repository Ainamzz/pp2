#преобразования строки из camel case в snake case
import re
text = input("Enter a camel case string: ")
snake = re.sub(r'([A-Z])', r'_\1', text).lower()
print(snake)
if snake.startswith('_'):
    snake = snake[1:]
print(snake)