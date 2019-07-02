# Find the sum of all primes below two million

def is_prime(number):
    global highnum
    global primemults
    highsqd = highnum ** 2
    if (highsqd < number):
        highnum = highnum + 1
#    print("highnum =", highnum, number, highsqd)
    if (highsqd == number):
        return False
#    for i in range(2,highnum):
    for i in primemults :
#        print("i =", i)
        j = i * i
        if (j > number) :
#           print("breaking")
            break
        if number % i == 0:
            #Not prime
            return False
            break
#    else:
#    print("prime = ", number)
    primemults.append(number)
    return True
sum=0
counter=0
highnum=1
primemults = []
for number in range(2, 2000000):
 #   if(number % 2 != 0):
    if is_prime(number):
        sum += number

#    counter += 1
#    if counter == 10000:
#        print(number)
#        counter = 0

print("sum = ",sum)
