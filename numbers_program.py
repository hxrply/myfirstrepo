def is_prime(z):
    if z < 2:
        return False
    else:
        for i in range(2,z):
            if z % i == 0:
                #print("No divisible by",i)
                return False
        return True

start = int(input("Please enter a start index: "))
end = int(input("Please enter an end index: "))

total_prime=0

if (start % 2) == 0:
    start = start + 1

for z in range(start,end+1,2):
    if is_prime(z):
        total_prime += 1
        print("",z,"*",sep='')
    

print("Total number of integars printed:", end - start + 1)
print("Total number of primes printed:", total_prime)
