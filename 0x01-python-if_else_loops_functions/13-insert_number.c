#include "lists.h"

/**
 * check_cycle - function to check cycles in singly linked lists
 * @head: pointer to a pointer to head of list
 * @number: int
 * Return: bit
 */

listint_t *insert_node(listint_t **head, int number)
{
if (head == NULL)
return (NULL);
listint_t *new;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
listint_t *current = *head;
while (current->next)
{
current = current->next;
if (current->n <= number && current->next->n >= number)
{
new->n = number;
new->next = current->next;
current->next = new;
return (new);
}
}
return (NULL);
}
