#include<stdio.h>
int main()
{
    int i,j;
    for(i=3;i<99999;i++)
    {
        for(j=2;j<11;j++)
        {
            if (i%j==0)
            {
                if (j==10)
                {
                    printf("%d\n",i);
                    return 0;
                }
                else
                    break;

            }
        }
    }
    return 0;
}
