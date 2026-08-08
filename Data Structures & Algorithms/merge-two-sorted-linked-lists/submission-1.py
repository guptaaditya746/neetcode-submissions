# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        temp1 = list1
        temp2 = list2
        tail = dummyNode

        # Loop while BOTH lists still have nodes to compare
        while temp1 is not None and temp2 is not None:
            if temp1.val > temp2.val:
                tail.next = temp2      # 1. Link the smaller node to our merged list
                tail = tail.next       # 2. Advance our tail to stand on that new node
                temp2 = temp2.next     # 3. Advance temp2 to the next node in its list
            else:
                tail.next = temp1 
                tail = tail.next
                temp1 = temp1.next
        
        # --- OUTSIDE THE WHILE LOOP ---
        # At this point, one list is empty, and the other might still have nodes.
        # We attach the entire remaining chain in one single step.
        if temp1 is not None:
            tail.next = temp1
            
        if temp2 is not None:
            tail.next = temp2

        # Return the start of our actual merged list (skipping the dummy node)
        return dummyNode.next