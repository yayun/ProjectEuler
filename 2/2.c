//Find the sum of all the even-valued terms in the Fibonacci sequence which do not exceed four million.

///Here we use Exhaustive method :a cycle from 1 to 4000000 first:find the fibonacci second:find whose value is even then sum it
#include<stdio.h>
int main()
{
    int i=1,j=1,k=0;
    int  sum=0;
    while(k<=4000000)
    {
        if(k%2==0)
            sum=sum+k;
        i=j;
        j=k;
        k=i+j;
    }
    printf("%d\n",sum);
    return 0;
}   
