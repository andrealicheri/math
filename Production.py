# Imports the input
with open("input.txt") as i:
    inputs = i.readlines()

# Does the production
production = 1
for input in inputs:
	number = int(input)
	production = production * number

print(production)