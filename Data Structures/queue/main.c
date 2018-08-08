#include <stdio.h>
#include <stdlib.h>
int MAX= 10;
int main()
{
    int queue[MAX];
    int front = 0, rear = -1,i;
    int choice, ele;
    while(1)
    {
        scanf("%d",&choice);
        switch(choice)
        {
        case 1:
            scanf("%d",&ele);
            if(rear < MAX)
            {
                queue[++rear] = ele;
            }
            else{
                printf("Overflow");
            }
            break;
        case 2:
            if(front <= rear)
            {
                front++;
            }
            else
            {
                printf("Underflow");
            }
            break;
        case 3:
            for(i=front;i<=rear;i++)
                printf("%d\t",queue[i]);
            break;
        default:
            exit(0);
        }
    }
    return 0;
}
