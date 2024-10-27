def is_prime(z):
    return True


y = 1 #int(input("Please enter a start index: "))
x = 10 #int(input("Please enter an end index: "))
for z in range(y,x+1,1):
    if is_prime(z) == True:
        print("",z,"*",sep='')
    else:
        print(z)

    
print("Total number of integars printed:", x-y+1)
