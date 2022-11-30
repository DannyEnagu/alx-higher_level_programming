#include "lists.h"

/**
 * check_cycle - checks a single linked list for cycle
 * @head: list input
 *
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */

int check_cycle(listint_t *head)
{
	listint_t *fast;
	listint_t *slow;

	/* if head is NULL, no cycle */
	if (head == NULL)
		return (0);

	fast = head->next;
	slow = head;

	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
