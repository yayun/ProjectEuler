#include<stdio.h>
int main()
{
    int sum=0;
    int i,j;
    for (i=2;i<2000000;i++)
    {
        for(j=2;j<i;j++)
        {
            if(i%j==0)
                break;
            if(j==i-1)
                sum=sum+i;
        }
    }
    printf("%d \n",sum+2);
//Remember to add 2!

}
