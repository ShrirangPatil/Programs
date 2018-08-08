#include <stdio.h>
#include <stdlib.h>
#define MAX 5
int main()
{
    int queue[MAX];
    int front = 0, rear = -1,i;
    int choice, ele,x;
    int counter = 0;
    while(1)
    {
        scanf("%d",&choice);
        switch(choice)
        {
        case 1:
            scanf("%d",&ele);
            if(counter < MAX)
            {
                queue[++rear%MAX] = ele;
                counter++;
            }
            else{
                printf("Overflow");
            }
            break;
        case 2:
            if(counter > 0)
            {
                front++;
                front = front%MAX;
                counter--;
            }
            else
            {
                printf("Underflow");
            }
            break;
        case 3:
            x = 0;
            for(i=front;x<counter;x++){
                printf("%d\t",queue[i]);
                i = (i+1)%MAX;
            }
            break;
        default:
            exit(0);
        }
    }
    return 0;
}
