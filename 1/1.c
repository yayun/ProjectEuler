#include<stdio.h>
int main(int argc,char *argv[])
{
    int sum=0,i=0;
    int N;
    printf("Quesion:If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.\nPlease input the number you want to caculate");
    scanf("%d",&N);
    for(i;i<N;i++)
    {
        if ((i%3==0)||(i%5==0))
        {
            sum=sum+i;
        }
    }
    printf("%d \n",sum);
    return 0;
}
