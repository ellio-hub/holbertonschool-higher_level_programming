#include "lists.h"

/**
 * check_cycle - function to check cycles in singly linked lists
 * @list: pointer to head of list
 * Return: bit
 */

int check_cycle(listint_t *list)
{
listint_t *i = list, *j = list;
while (i && j && j->next)
{
i = i->next;
j = j->next->next;
if (i == j)
return (1);
}
return (0);
}
