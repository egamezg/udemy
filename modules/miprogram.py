# This is the program that calls the module
import module1
import camelcase
# We can import an entire module, or only specific funcionts as "from"
from module1 import despedirse

# We can rename the functions on the import as follows
from module1 import despedirse as adios


module1.saludar("Ernesto")

# Call the function directly from the import "from" does not need to put module
# if you imported with from
despedirse("Laia")

# We use the renamed imported function
adios("Rafael")