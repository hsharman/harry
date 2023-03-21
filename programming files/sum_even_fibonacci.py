# declare variables a and b
a, b = 0, 1
sum_even = 0
while b < 4000000:
    # if b is even 
    if b % 2 == 0:
        sum_even += b
    a, b = b, a+b

#print the even sum
print(sum_even)

# answer should be 4613732
