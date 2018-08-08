#include <stdio.h>
#include <stdlib.h>

struct node
{
    struct node *prev;
    int data;
    struct node *next;
};
struct node* addNode(struct node* head,int ele)
{
    struct node *newnode;
    newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = ele;
    if(head == NULL)
    {
        head = newnode;
        newnode->prev = NULL;
        newnode->next = NULL;
        return head;
    }
    newnode->next = head;
    newnode->prev = NULL;
    head->prev = newnode;
    head = newnode;
    return head;
}
struct node* removeNode(struct node *head,int ele)
{
    struct node *temp, *rmNode;
    temp = head;
    if(temp->data == ele)
    {
        head = temp->next;
        temp->next = NULL;
        head->prev = NULL;
        return head;
    }
    while(temp != NULL && temp->next != NULL && temp->next->data != ele)
    {
        temp = temp->next;
        //printf("%d\t",temp->data);
    }
    if(temp != NULL && temp->next != NULL)
    {
        rmNode = temp->next;
        //printf("\n%d\n",rmNode->data);
        temp->next = temp->next->next;
        if(rmNode->next != NULL)
            rmNode->next->prev = temp;
        rmNode->prev = NULL;
        rmNode->next = NULL;
    }
    return head;
}
void display(struct node* head)
{
    while(head != NULL)
    {
        printf("%d\t",head->data);
        //printf("%f\t",head->next);
        head = head->next;
    }
}
int main()
{
    struct node *head = NULL;
    int ele,choice;
    while(1)
    {
        scanf("%d",&choice);
        switch(choice)
        {
        case 1:
            scanf("%d",&ele);
            head = addNode(head,ele);
            break;
        case 2:
            scanf("%d",&ele);
            head = removeNode(head,ele);
            break;
        case 3:
            display(head);
            break;
        default:
            exit(0);
        }
    }
    return 0;
}

