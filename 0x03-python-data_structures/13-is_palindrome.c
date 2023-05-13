#include "lists.h"

/**
 * reverse - reverses a list
 * @head: the address of the first element in list
 */
void reverse(listint_t **head)
{
	listint_t *previous = NULL, *current = *head, *temp;

	while (current)
	{
		temp = current->next;
		current->next = previous;
		previous = current;
		current = temp;
	}

	*head = previous;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: address of the first element in the list
 *
 * Return: returns 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *last = *head, *first = *head;

	/* if list is empty */
	if (*head == NULL)
		return (1);
	while (last) /* get last element in the list */
	{
		if (last->next == NULL)
			break;
		last = last->next;
	}

	if (last != first) /* reverse list if more than 1 element */
		reverse(&last);

	while (last > first)
	{
		if (first->n != last->n) /* compare first and last values */
			return (0);
		first = first->next;
		last = last->next;
	}
	return (1);
}
