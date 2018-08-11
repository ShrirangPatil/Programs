#include<stdio.h>
#define SIZE 17
/*
Name:
Simple CRC Implementation
Descriptions:
Genrator polynomial : 1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1
Data(say) : 1 1 1 1 
Appending zeros to data : 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0(Provide this as input with length of data to be 4)
CRC(cyclic redundancy check) : 0 1 1 1 1 0 0 1 1 1 1 1 1 1 1 1 1(for above data)
Data after appending CRC : 1 1 1 1 0 1 1 1 1 0 0 1 1 1 1 1 1 1 1 1 1(The data to be sent)

Note:
All the values are stored in reverse fasion ie MSB will be at the LAST position and LSB will be at the FIRST position
*/
int main()
{
	//		     6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 ; 1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1
	int genPoly[SIZE] = {1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1};
	int n,i,j;
	int rem[SIZE], temp[SIZE];
	printf("Enter the size of message \t");
	scanf("%d",&n);
	int message[n+SIZE];
	printf("Enter the message\n");
	
	for(i=SIZE+n-1;i>=0;i--)
		scanf("%d",&message[i]);

	//for(i=SIZE-1;i>=0;i--)
		//message[i] = 0;
	
	for(i=n+SIZE-1;i>=0;i--)
		printf("%d",message[i]);
	
	printf("\n");

	for(i=SIZE-1;i>=0;i--)
		printf("%d",genPoly[i]);
	
	for(i=SIZE+n-1;i>=n;i--)
		temp[i-n] = message[i];
	int x = n-1,y,z;
	//for(j=0;j<=n;j++)
	while(x>=0-1)
	{
		for(i=SIZE-1;i>=0;i--)
			rem[i] = temp[i]^genPoly[i];
		z = SIZE-1;
		while(rem[z] == 0)
			z-=1;
		//for(i=SIZE-1;i>0;i--)
			//temp[i] = rem[i-1];
		y = SIZE-1;
		while(z>=0)
		{
			temp[y] = rem[z];
			y-=1;
			z-=1;
		}
		while(y>=0)
		{
			temp[y] = message[x];
			x-=1;
			y-=1;
		}
		//temp[0] = message[n-j];
		printf("\nResult\n");

		printf("Rem\t");
		for(i=SIZE-1;i>=0;i--)
			printf("%d",rem[i]);
		
		printf("\nGenPoly\t");
		if(x == -1)
		{
			for(i=SIZE-1;i>=0;i--)
				printf("%d",genPoly[i]);

			printf("\ntemp\t");
			for(i=SIZE-1;i>=0;i--)
				printf("%d",temp[i]);
		}

	}
}
