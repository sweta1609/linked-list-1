class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    # Write your code here.
    pass
    if head is None or head.next is None:
        return -1
    
    count = 0
    curr = head
    while curr != None:
        if curr.data == n:
            return count
        curr = curr.next
        count += 1
    return -1



