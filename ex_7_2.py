from typing import Optional

# Imported from EPI Judge code.
from list_node import ListNode


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    head = ListNode(next=L)
    sub_head = head

    for _ in range(1, start):
        sub_head = sub_head.next

    sub_tail = sub_head.next
    for _ in range(start, finish):
        temp = sub_tail.next
        sub_tail.next = temp.next
        temp.next = sub_head.next
        sub_head.next = temp

    return head.next
