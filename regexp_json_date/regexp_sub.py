# Sub substitute patter for a given one

text = """My name is carlos and i live in Spain
My name is Guyana and live in France
My name is Laia and i, live in Sant Marti
"""

import re

print(re.sub("name", "names", text))