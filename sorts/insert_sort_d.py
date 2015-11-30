import sys

numbers = []
for arg in sys.argv:
    try:
        numbers.append(float(arg))
    except ValueError:
        pass

#INSERT SORTING CODE HERE
for j in xrange(1,len(numbers)):#For j in range 1 to length of numbers
    key = numbers[j]#key is the current number
    i = j - 1#Let i be a pointer lesser than j by 1
    while i >= 0 and numbers[i] < key:#Move i to the head of the list until key is lesser than the current number.
        numbers[i+1] = numbers[i]#Push the number back one slot because it's lesser than the key
        i = i - 1#decrement i by 1
    numbers[i + 1] = key#put key at i

for number in numbers:
    print number
