#include "lists.h"

/**
 * check_cycle - function to check cycles in singly linked lists
 * @head: pointer to a pointer to head of list
 * @number: int
 * Return: bit
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new, *tmp;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
tmp = *head;
if (*head == NULL)
{
new = add_nodeint_end(head, number);
return (new);
}
if (tmp->n > number)
{
new->next = tmp;
new->n = number;
*head = new;
return (new);
}
while (tmp->next)
{
if (number < tmp->next->n)
{
new->next = tmp->next;
tmp->next = new;
new->n = number;
return (new);
}
tmp = tmp->next;
}
new = add_nodeint_end(head, number);
return (new);
}
