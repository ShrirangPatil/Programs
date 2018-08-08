#include <stdio.h>
#include <stdlib.h>
int MAX = 10;
int main()
{
    int stack[MAX];
    int top = -1,choice,ele,i;
    while(1)
    {
        scanf("%d",&choice);
        switch(choice)
        {
        case 1:
            scanf("%d",&ele);
            if(top < MAX)
            {
                stack[++top] = ele;
            }
            else{
                printf("Overflow");
            }
            break;
        case 2:
            if(top > -1)
            {
                top--;
            }
            else{
                printf("Underflow");
            }
            break;
        case 3:
            for(i=0;i<=top;i++)
                printf("%d\t",stack[i]);
            break;
        default:
            exit(0);
        }
    }
    return 0;
}
