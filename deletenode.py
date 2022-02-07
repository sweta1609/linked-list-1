from sys import stdin

# Following is the Node class already written for the Linked List.
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def length(head):
    temp = head
    count = 0

    while temp:
        count += 1
        temp = temp.next
    return count

def deleteNode(head, pos) :
    # Write your code here.
    pass
    if pos < 0 or pos > length(head):
        return head
    
    if head is None: 
        return head
    if pos == 0:
        return head.next
    
    current = head
    prev = None
    count = 0

    while count < pos:
        prev = current
        current = current.next
        count += 1

    if prev.next == None:
        return head
    if prev is not None:
        nextNode = current.next
        prev.next = nextNode
    else:
        head = head.next
        return head
    
    return head
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head



# To print the linked list.
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


# Main.
t = int(stdin.readline().strip())

while t > 0 :
    
    head = takeInput()
    pos = int(stdin.readline().rstrip())
    
    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1
