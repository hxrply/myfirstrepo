def is_prime(z):
    if z < 2:
        return False
    else:
        for i in range(2,z):
            if z % i == 0:
                #print("No divisible by",i)
                return False
        return True

y = int(input("Please enter a start index: "))
x = int(input("Please enter an end index: "))

total_int=0
total_prime=0

for z in range(y,x+1,1):
    total_int += 1
    if is_prime(z):
        total_prime += 1
        print("",z,"*",sep='')
    else:
        print(z)
    

print("Total number of integars printed:", total_int)
print("Total number of primes printed:", total_prime)
