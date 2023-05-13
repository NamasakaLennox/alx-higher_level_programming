#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: address of the first element in the list
 *
 * Return: returns 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *last = *head, *first = *head;
	int len = 0, count_up = 0, i;

	/* if list is empty */
	if (*head == NULL)
		return (1);
	/* get length of list and last element of the list */
	while (last)
	{
		len++;
		if (last->next == NULL)
			break;
		last = last->next;
	}

	len = len - 1; /* indexing starts from zero */
	while (count_up < len)
	{
		if (first->n != last->n) /* compare first and last values */
			return (0);
		count_up++;
		len--;
		first = first->next;
		last = first;
		for (i = count_up; i < len; i++) /* change value of last elem */
			last = last->next;
	}
	return (1);
}
