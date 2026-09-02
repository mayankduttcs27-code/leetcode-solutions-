class Solution:
    def flatten(self, head):
        if not head:
            return head

        curr = head

        while curr:
            if curr.child:
                next_node = curr.next

                child = curr.child
                curr.next = child
                child.prev = curr
                curr.child = None

                tail = child
                while tail.next:
                    tail = tail.next

                if next_node:
                    tail.next = next_node
                    next_node.prev = tail

            curr = curr.next

        return head