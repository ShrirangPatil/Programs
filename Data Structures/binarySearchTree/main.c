#include <stdio.h>
#include <stdlib.h>
#define MAX 10
struct node
{
    struct node *left;
    int data;
    struct node *right;
};
int maxi = 0;
int num = 0;
void inOrder(struct node* root)
{
    if(root != NULL)
    {
        inOrder(root->left);
        printf("%d ",root->data);
        inOrder(root->right);
    }
}
void preOrder(struct node* root)
{
    if(root != NULL)
    {
        printf("%d ",root->data);
        inOrder(root->left);
        inOrder(root->right);
    }
}
void postOrder(struct node* root)
{
    if(root != NULL)
    {
        inOrder(root->left);
        inOrder(root->right);
        printf("%d ",root->data);
    }
}
void LOT(struct node* root)
{
    struct node *queue[MAX];
    int front = 0, rear = -1, temp;
    queue[++rear] = root;
    while(front <= rear)
    {
        printf("%d\t",queue[front]->data);
        temp = front++;
        if(queue[temp]->left != NULL)
        {
            //printf("%d\n",queue[temp]->data);
            queue[++rear] = queue[temp]->left;
        }
        if(queue[temp]->right != NULL)
        {
            //printf("%d\n",queue[temp]->data);
            queue[++rear] = queue[temp]->right;
        }
    }
}
struct node* constructBST(struct node* root,int ele)
{
    struct node *newnode;
    //printf("%d\n",ele);
    //printf("%u\n",root);
    if(root == NULL)
    {
        newnode = (struct node*)malloc(sizeof(struct node));
        newnode->data = ele;
        //printf("%d",root->data);
        newnode->left = NULL;
        newnode->right = NULL;
        return newnode;
    }
    if(root->data > ele)
        root->left = constructBST(root->left,ele);
    else
        root->right = constructBST(root->right,ele);
    return root;
}

void heightOfSubTree(struct node *root)
{
    if(root != NULL)
    {
        num++;
        heightOfSubTree(root->left);
        num--;
        if(num > maxi)
            maxi = num;
        num++;
        heightOfSubTree(root->right);
        num--;
        if(num > maxi)
            maxi = num;
    }
}
int main()
{
    struct node *root = NULL;
    int ele,choice;
    while(1)
    {
        scanf("%d",&choice);
        switch(choice)
        {
        case 1:
            scanf("%d",&ele);
            root = constructBST(root,ele);
            break;
        case 2:
            //scanf("%d",&ele);
            //head = removeNode(head,ele);
            inOrder(root);
            break;
        case 3:
            //display(head);
            preOrder(root);
            break;
        case 4:
            postOrder(root);
            break;
        case 5:
            LOT(root);
            break;
        case 6:
            heightOfSubTree(root);
            printf("%d\n",maxi);
            break;
        default:
            exit(0);
        }
    }
    return 0;
}
