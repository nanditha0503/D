# numbers.py

# Check if a number is prime
# bkugauwg   
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n*0.5)+1):
        if n % i == 0:
            return False
    return True

# Generate Fibonacci series up to n terms
def fibonacci(n):
    pass

def new_fun():
    pass
