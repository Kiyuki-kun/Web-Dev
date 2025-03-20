x = input()
reversed_number = ""

for digit in reversed(x):
    reversed_number += digit

print(int(reversed_number))
