#include "lists.h"
/**
 * is_palindrome - function that check for palindrom
 * @head:list
 *
 *Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
const listint_t *u;
int len, i, j;
int ary[10000];
if (*head == NULL)
return (1);
u = *head;
len = 0;
while (u != NULL)
{
u = u->next;
len++;
}
if (len == 1)
return (1);
u = *head;
i = 0;
while (u != NULL)
{
ary[i] = u->n;
i++;
u = u->next;
}
j = 0;
i--;
len--;
while (i >= (len / 2))
{
if (ary[i] != ary[j])
return (0);
i--;
j++;
}
return (1);
}
