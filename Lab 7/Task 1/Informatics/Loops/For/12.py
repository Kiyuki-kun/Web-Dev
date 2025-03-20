binary_number = input()  
decimal_number = 0  

for i in range(len(binary_number)):  
    bit = int(binary_number[-(i + 1)])  
    decimal_number += bit * (2 ** i)  

print(decimal_number)
