def binary_gap(n):
    binary_number = bin(n)[2:]
    b = 0
    max_b = 0
    
    for k in binary_number:
        if int(k) == 0:
            b+=1
        elif int(k) == 1:
            max_b = max(b,max_b)
            b = 0
    
    return max_b
    

print(binary_gap(4241))
print(binary_gap(33921))