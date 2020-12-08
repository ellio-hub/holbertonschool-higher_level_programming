#include "lists.h"

/**
 * check_cycle - function to check cycles in singly linked lists
 * @head: pointer to a pointer to head of list
 * @number: int
 * Return: bit
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *x = NULL, *last = NULL, *new = NULL;
x = *head;
last = *head;
new = malloc(sizeof(listint_t));
if (!new)
return (NULL);
new->n = number;
if (!x)
{
new->next = NULL;
*head = new;
return (*head);
}
else if ((*head)->n > number)
{
new->next = (*head);
(*head) = new;
return (*head);
}
while (x)
{
if (x->n > number)
{
new->next = x;
last->next = new;
break;
}
last = x;
x = x->next;
}
if (!x)
{
new->next = NULL;
last->next = new;
}
return (*head);
}
