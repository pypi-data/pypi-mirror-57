//
// Created by Eric Graves on 7/24/15.
//

#include "queue.h"
#include "stdio.h"

struct queue* queue_factory() {

    struct queue* q = malloc(sizeof(struct queue));

    q->first = q->last = NULL;
    q->size = 0;

    return(q);
}

void enqueue(struct queue *q, struct work w) {
    struct node* n = malloc(sizeof(struct node));

    n->work = w;
    n->next = NULL;

    if (q->first == NULL) {
        q->first = q->last = n;
    } else {
        q->last->next = n;
        q->last = n;
    }
    q->size++;
}

struct work dequeue(struct queue *q) {
    struct work out = {0};
    if (q->first == NULL) {
    
    } else {
        struct node* tmp = q->first;

        // check if there is anything next in the queue
        if (tmp->next == NULL) {
            q->first = q->last = NULL;
        } else {
            q->first = tmp->next;
        }
        q->size--;
        out = tmp->work;
        free(tmp);
    }
    return(out);
}

void release_queue(struct queue* q) {
    struct node* temp = q->first;
    while(temp != NULL) {
        q->first = temp->next;
        free(temp);
        temp = q->first;
    }
    free(q);
}

int queue_size(struct queue *q) {
    return (q->size);
}

void queue_print(struct queue* q) {
    struct node* temp = q->first;
    while(temp != NULL) {        
        temp = temp->next;
    }    
}

int is_empty(struct queue *q) {
    return q->first == NULL ? 1 : 0;
}
