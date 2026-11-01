class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        previous_tail = None
        new_head = None

        while curr:
            # Step 1: Check if k nodes exist
            temp = curr
            count = 0

            while temp and count < k:
                temp = temp.next
                count += 1

            if count < k:
                break

            # Step 2: Save the original first node
            group_tail = curr

            # Step 3: Reverse exactly k nodes
            prev = None
            count = 0

            while curr and count < k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                count += 1

            # Step 4: Remember the new head
            if new_head is None:
                new_head = prev

            # Step 5: Connect the previous group
            if previous_tail:
                previous_tail.next = prev

            # Step 6: Connect the remaining nodes
            group_tail.next = curr

            # Step 7: Remember the tail for next time
            previous_tail = group_tail

        return new_head if new_head is not None else head

       
 
        
        



        

        
        
        
