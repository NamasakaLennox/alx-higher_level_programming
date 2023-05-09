#include "lists.h"

/**
 * insert_node - inserts a node in a sorted list
 * @head: address of the first node
 * @number: the element to add
 *
 * Return: the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *previous, *next;

	if (!head)
		return (NULL);
	previous = *head;
	next = (*head)->next;
	new = malloc(sizeof(listint_t)); /* memory allocation */
	if (!new)
		return (NULL);
	new->n = number;
	if (*head == NULL) /* if empty list */
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if (number < (*head)->n) /* if number is less than head */
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	/* add node elsewhere */
	while (previous->next)
	{
		previous = previous->next;
		next = next->next;
		if (next)
			if (next->n > number)
				break;
	}
	previous->next = new;
	new->next = next;
	return (new);
}
