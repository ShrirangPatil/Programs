#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX 6
#define LEN 5//MAX-1

void heapConstruct(int heap[])
{
    int i,k,heap1,j,v;
    //for(i=1;i<MAX;i++)
      //  printf("%d\n",heap[i]);
    for(i=floor(LEN/2);i>0;i--)
    {
        k = i;
        //printf("k = %d\n",k);
        v = heap[k];
        heap1 = 0;//initial the heap = false
        while(!heap1 && 2*k <= LEN)
        {
            j = 2*k;
            if(j<LEN)//if there are 2 children
            {
                if(heap[j] < heap[j+1])//get the max of two children// for minHeap changes( > )
                    j = j+1;
            }
            if(v >= heap[j])//compare the max child with parent// for minHeap changes ( <= )
                    heap1= 1;//make the heap = true
            else
            {
                heap[k] = heap[j];//assign value of max child to parent
                k = j;
            }
            heap[k] = v;//assign the value of parent to child
        }
    }
}
int main()
{
    int i;
    int heap[MAX];
    for(i=1;i<MAX;i++)
        scanf("%d",&heap[i]);
    heapConstruct(heap);
    for(i=1;i<MAX;i++)
        printf("%d\t",heap[i]);
    return 0;
}
