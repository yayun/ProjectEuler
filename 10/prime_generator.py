import math
def main():
    sum=2
    count = 3
    while count<2000000:
        isprime = True
        for x in range(2, int(math.sqrt(count) + 1)):
#why we use sqrt in this
            if count % x == 0: 
                isprime = False
                break
        if isprime:
            print count
            sum=sum+coun
#it is much better to local this judgment sentences here (can reduce cycle time greatly)
        count += 1
    print sum
main()
