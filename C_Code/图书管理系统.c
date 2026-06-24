#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define NAME_LEN 200
#define AUTHOR_LEN 100
#define PUBLISHER_LEN 100//用宏来代替字符串即定义了一个常量
typedef struct Book {
    int id;
    char name[NAME_LEN];
    char author[AUTHOR_LEN];//确保用户在输入时也不会超过这个长度
    char publisher[PUBLISHER_LEN]; //即限制输入函数里占位符的长度 eg: scanf("%99s", book.author);
    double price;
    int stock;
} Book;
typedef struct BookNode {
    Book data;
    struct BookNode *next;//C语言中特有的自引用
} BookNode;
BookNode* createBookNode(Book data){
    BookNode* newNode = (BookNode*)malloc(sizeof(BookNode));
    if (newNode == NULL){
        printf("内存分配失败！\n");
    }
    return NULL;
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}
void addNode(BookNode **head, Book data){
    BookNode* newNode = createBookNode(data);
    if (*head == NULL){
        *head = newNode;
        return;
    }
    else{
        BookNode * p = *head;
        while (p->next != NULL){
            p = p->next;
        }
        p->next = newNode;
    }
}
void printList(BookNode *head){
    if (head == NULL){
        printf("当前没有图书数据！\n");
        return;
    }
    BookNode *p = head;
    while (p != NULL){
        printf("ID: %d\n", p->data.id);
        printf("书名: %s\n", p->data.name);
        printf("作者: %s\n", p->data.author);
        printf("出版社: %s\n", p->data.publisher);
        printf("价格: %.2f\n", p->data.price);
        printf("库存: %d\n", p->data.stock);
        p = p->next;
    }
}
BookNode *findBookbyid(BookNode *head,int id){
    BookNode *p = head;
    while (p != NULL){
        if (p -> data.id == id){
            return p;
        }
        p = p -> next;
    }
    return NULL;
}



