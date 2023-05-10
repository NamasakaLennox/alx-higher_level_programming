#include "lists.h"

/**
 * check_cycle - checks if the linked list has a loop
 * @list: the head of the linked list
 *
 * Return: returns 0 if no loop, 1 if a loop is present
 */
int check_cycle(listint_t *list)
{
	listint_t *check_ahead, *check = list;

	while (check && check_ahead && check_ahead->next)
	{
		check = check->next;
		check_ahead = check_ahead->next->next;
		if (check == check_ahead)
			return (1);
	}
	return (0);
}
