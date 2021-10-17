# Split divides string from a given pattern

text = """My name is carlos and i live in Spain
My name is Guyana and live in France
My name is Laia and i, live in Sant Marti
"""

import re

result = re.split(" ", text)

print(result)
print(len(result))