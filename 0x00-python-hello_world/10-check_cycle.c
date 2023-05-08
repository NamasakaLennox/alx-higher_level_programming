#include "lists.h"

/**
 * check_cycle - checks if the linked list has a loop
 * @list: the head of the linked list
 *
 * Return: returns 0 if no loop, 1 if a loop is present
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, *next = list->next;

	while (current)
	{
		while (next)
		{
			if (current == next)
				return (1);
			next = next->next;
		}
		current = current->next;

		if (current)
			next = current->next;
	}

	return (0);
}
