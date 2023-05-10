#include "lists.h"

/**
 * check_cycle - checks if the linked list has a loop
 * @list: the head of the linked list
 *
 * Return: returns 0 if no loop, 1 if a loop is present
 */
int check_cycle(listint_t *list)
{
	listint_t *check, *last = list;

	while (last)
	{
		if (last == last->next)
			return (1);

		for (check = list; check != last; check = check->next)
			if (check == last->next)
				return (1);
		last = last->next;
	}
	return (0);
}
