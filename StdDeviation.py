import math
# Imports the input
with open("input.txt") as i:
    inputs = i.readlines()
# Define the numbers of inputs
inputValue = 0
for input in inputs:
    inputValue = inputValue + 1
# Calculate the avarege value
eSum = 0
for line in inputs:
    eSum = eSum + int(line)
mid = eSum / inputValue
# Calculate the standard deviation
stdDeviation = 0
for number in inputs:
    initial = int(line) - mid
    initSquare = initial * initial
    stdDeviation = stdDeviation + initSquare
stdDeviation = stdDeviation / mid
stdDeviation = math.sqrt(stdDeviation)
print(stdDeviation)