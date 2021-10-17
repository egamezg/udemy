# regular expressions, search, findall, split, subj

text = "hello my name is Ernesto"

import re

print(re.search("name", text))

result = re.search("^hello.*Ernesto$", text)

if result:
    print("find string")
else:
    print("not found string")