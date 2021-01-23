# This solution uses a hash table and requires O(N) space. One can use fast
# and slow pointers easily detect a cycle with O(1) space. However, that 
# solution requires extra complexity to find the node where the cycle begins.
def has_cycle(head):
    hash_table = {}
    
    node = head
    while node is not None:
        if node in hash_table:
            return node
        hash_table[node] = None
        node = node.next
    
    return None

