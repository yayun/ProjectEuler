#include<stdio.h>
#include<math.h>
int main()
{
    int i,j,m=0,max=0,n=0,multi;
    int a[6];
    for (i=101;i<1000;i++)
        for (j=101;j<1000;j++)
        {
            multi=i*j;
            int k=10;
            for(;multi>1;m++)
            {
                a[m]=multi%10;
                k=(int)pow(10,m+1);
                multi=(int)(multi/k);
                printf("%d",k);
            }
            multi=i*j;
            for(;(a[n]==a[m])&&(m>=n);m--,n++)
            {
                if (multi>max)
                {
                    max=multi;
                }
            }
             
        }
    printf("%d\n",max);
}
