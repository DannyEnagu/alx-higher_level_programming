#include"lists.h"

listint_t *copy_list(listint_t **head);
listint_t *reverse_list(listint_t **list);

/**
* is_palindrome - checks if a singly linked list is a palindrome
*	(i.e reading values from left to right is same as reading
*	from right to left)
*
* @head: head of the list which contains the entire linked list
*
* Return: 0 if list is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *current, *temp, *mid_t, *reverse;
	int size = 0, mid_p = 0, i;

	if (head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;
	temp = *head;
	while (current != NULL)
	{
		size++;
		current = current->next;
	}

	current = *head;
	/* find the middle (position or node) of the list */
	mid_p = size / 2;
	for (i = 0; i < mid_p; i++)
		temp = temp->next;

	/* reverse the secode half of the linked list from the middle position */
	reverse = reverse_list(&temp);
	mid_t = reverse;
	/* Compare nodes of first half and second half of list */
	while (reverse)
	{
		if (current->n != reverse->n)
			return (0);

		current = current->next;
		reverse = reverse->next;
	}
	/* reconstruct the list */
	reverse_list(&mid_t);

	return (1);
}

/**
* reverse_list - reverses a single linked list
*
* @list: list to reverse
*
* Return: A reversed linked list, NULL if fails
*/

listint_t *reverse_list(listint_t **list)
{
	listint_t *previous, *current, *next;

	previous = NULL;
	current = *list;
	next = NULL;
	while (current)
	{
	/* save the link to the next node before moving on */
		next = current->next;
	/* current next now points to the previous node */
		current->next = previous;
	/* previous now holds the reversed list */
		previous = current;
	/* continue loop*/
		current = next;
	}
	*list = previous;

	return (*list);
}

/**
* copy_list - Create a copy of the original list
*
* @head: contains list to copy
*
* Return: A copy of the original list on success,
*	NULL if fails
*/

listint_t *copy_list(listint_t **head)
{
	listint_t *current, *new_list;

	if (head == NULL)
		return (NULL);

	current = *head; /* used for iterating list*/
	new_list = NULL; /* head of the new list*/

	while (current != NULL)
	{
	/* copy / past each node data to the end of new_list */
		add_nodeint_end(&new_list, current->n);
		current = current->next;
	}

	return (new_list);
}
