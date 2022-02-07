from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

#Following is the Node class already written for the Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):

    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev
    return head


def isPalindrome(head):
    if head is  None or head.next is None:
        return True
    
    fast = head
    slow = head

    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    
    secondHalf = slow.next
    slow.next = None
    secondHalf = reverse(secondHalf)

    firstSublist = secondHalf
    secondSublist = head

    while firstSublist is not None:
        if firstSublist.data != secondSublist.data:
            return False
        firstSublist = firstSublist.next
        secondSublist = secondSublist.next
    
    firstSublist  = head
    secondSublist  = reverse(secondHalf)

    while firstSublist.next is not None:
        firstSublist = firstSublist.next
    
    firstSublist.next = secondSublist

    return True




#Taking Input Using Fast I/O


def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list
def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()

    if isPalindrome(head):
        print('true')
    else:
        print('false')

    t -= 1
