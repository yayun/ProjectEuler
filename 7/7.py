#Exhaustive
import sys
k=1
for i in range(2,993333):
    for j in range(2,i):
        if i%j==0:
            break
        if j==i-1:
            k=k+1
            print i
            print k
            if k==10001:
                print i
                print "hello"
                sys.exit(0)
