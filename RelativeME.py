# Imports the input
with open("input.txt") as i:
    inputs = i.readlines()
# Find maxium value
maximum = 0
for input in inputs:
    number = int(input)
    if (number > maximum) is True:
        maximum = number
# Find minimum value
for input in inputs:
	minimum = int(input)
	break
for input in inputs:
	number = int(input)
	if not (minimum - number) < 0:
		minimum = number
maximumError = (maximum - minimum) / 2
# Define the numbers of inputs
inputValue = 0
for input in inputs:
    inputValue = inputValue + 1
# Calculate the avarege value
eSum = 0
for line in inputs:
    eSum = eSum + int(line)
mid = eSum / inputValue

relativeError = maximumError / mid
print(relativeError)