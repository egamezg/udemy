# Convert data of dict to json struct

products1 = {"name":"chair","color":"swhite","price":80}

import json

json_struct = json.dumps(products1)

print(type(json_struct))

# Now convert the json struct to its original value

product2 = json.loads(json_struct)

print(type(product2))