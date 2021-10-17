# findall finds all concurrences insede the string

string = "This is another string in where we need to add another thing to search."

import re

result = re.findall("another",string)

print(type(result))
print(len(result))

