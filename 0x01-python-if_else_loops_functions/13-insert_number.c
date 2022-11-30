#include "lists.h"

/**
 * insert_node - insert a new node to a sorted linked list
 * @head: linked list
 * @number: node data
 *
 * Return: address of the new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	current = *head;
	new->n = number;

	/* make new node 1st node if list is empty*/
	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (current != NULL)
		{

			if (current->next->n >= number)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			current = current->next;
		}
	}
	new->next = NULL;
	current->next = new;
	return (new);
}
