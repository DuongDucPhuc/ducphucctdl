class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def nth_to_last(head, n):
    if head is None or n <= 0:
        return None

    # Initialize two pointers
    pointer1 = head
    pointer2 = head

    # Move pointer2 n nodes ahead
    for _ in range(n):
        if pointer2 is None:
            return None  # List is shorter than n elements
        pointer2 = pointer2.next

    # Move both pointers until pointer2 reaches the end
    while pointer2 is not None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1.value

# Example usage:
# Create a linked list: 1 -> 3 -> 5 -> 7 -> 9
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(5)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(9)

n = 2
result = nth_to_last(head, n)

if result is not None:
    print(f"The {n}th-to-last element is: {result}")
else:
    print(f"The list is shorter than {n} elements.")
