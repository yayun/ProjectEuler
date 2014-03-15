#coding:utf-8
"""
The sum of all the multiples of 3 or 5 below 1000.
We can use Exhaustive method.
But if we want to sum below one billion
Here is a smart way:
    first-- calculate the sum of the numbles divisible by 3
    second--calculate the sum of the numbles divisible by 5 
    third-- substract the sum of the numbers divisible by 15(because we calculate it twice)
    for n=3:3+6+9+12+......+999=3*(1+2+3+4+...+333)
    for n=5:5+10+15+...+995=5*(1+2+....+199)

We all study a formula in Junior high school：Summing the number of columns：1+2+....+n=1/2*n*(n+1)
    
"""
target=int(raw_input("This program is to calculate The sum of all the multiples of 3 or 5 below a numbler.\n please input the number:"))+1
def SumDivisibleBy(n):
    p=target/n
    return n*p*(1+p)/2    
print SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15)




