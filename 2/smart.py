#coding:utf-8
"""
Question: Find the sum of all the even-valued terms in the Fibonacci sequence which do not exceed four million.
We will find a  recursive relation if we read the fibanacci sequence :1,1,2,3,5,8,13,21,34,55,89,144,233,377,610.....
       a,b,c a,b,c  a,b,  c  a ,b ,c   a  , b ,c
c---the even fibonacci number 
so we can write program like this:
"""
def sum_third_fibonacci():
    a=b=1
    sum=0
    c=2
    while(c<=4000000):
        sum=sum+c
        a=b+c
        b=a+c
        c=a+b
    print sum
#bypass the judgment of even
sum_third_fibonacci()

"""
the even in the fibonacci sequence obey this discipline:4*E(n-1)+E(n-2).For fibonacci it means F(n)=4*F(n-3)+F(n-6) :we can prove it!
so we can do it like this:
"""

def smart():
    i=2
    j=8
    k=sum=0
# here we can't write k<=4000000 see question clearly, This program is not reasonal because we must statistic the value in fibonacci sequences
    while(k<4000000):
        k=4*j+i
        i=j
        j=k
        sum=sum+k
    print sum+10
smart()        



