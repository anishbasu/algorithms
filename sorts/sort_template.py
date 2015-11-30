import sys

numbers = []
for arg in sys.argv:
    try:
        numbers.append(float(arg))
    except ValueError:
        pass

#INSERT SORTING CODE HERE
