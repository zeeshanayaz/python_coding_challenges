# Check Prime Number - If a number provided is prime or not

def is_prime(num):
    flag = False

    if num == 0 or num == 1:
        return f'{num} is not a prime number'
    else:
        for i in range(2,num):
            if num % i == 0:
                flag = True
                break
        
        if flag:
            return f'{num} is not a prime number'
        else:
            return f'{num} is a prime number'

print("Prime Number")
print(is_prime(5))