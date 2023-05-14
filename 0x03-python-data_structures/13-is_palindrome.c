#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: address of the first element in the list
 *
 * Return: returns 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_if_palindrome(head, *head));
}

/**
 * check_if_palindrome - checks if a function is a palindrome recursively
 * @head: the address of the list
 * @last: last node in the list, initially set to head node
 *
 * Return: returns 1 if palindrome, 0 otherwise
 */
int check_if_palindrome(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check_if_palindrome(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
