### DOUBLY LINKEDLIST Implementation
```
#class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None
# 
# 
# def insert_begin(head,val):
#     newNode = Node(val)
#     if head is None:
#         return newNode
# 
#     newNode.next = head
#     head.prev = newNode
#     return newNode
# 
# def insert_end(head,val):
#     newNode = Node(val)
#     if head is None:
#         return newNode
#     curr = head
#     while curr.next is not None:
#         curr = curr.next
#     curr.next = newNode
#     newNode.prev = curr
#     return head
# 
# 
# def delete_head(head):
#     if head is None or head.next is None:
#         return None
#     head = head.next
#     head.prev = None
#     return head
# 
# def printDLL(head):
#     curr = head
#     while curr != None:
#         print(curr.data, end=' ')
#         curr = curr.next
# 
# 
# def reverse(head):
#     if head is None:
#         return None
#     if head.next is None:
#         return head
# 
#     curr = head
#     pre = None
# 
#     while curr != None:
#         pre = curr
#         curr.next, curr.prev = curr.prev, curr.next #swap
#         curr = curr.prev
#     return pre
# 
# 
# head = None
# # head = insert_begin(head,10)
# # head = insert_begin(head,20) #  20 -> 10
# # printDLL(head)
# 
# # head = insert_end(head,12)
# # head = insert_end(head,14)
# # head = insert_end(head,116)
# #
# # head = delete_head(head)
# # printDLL(head)
# 
# 
# # head = reverse(head)
# # printDLL(head)
# 
# # head = Node(10)
# # temp1 = Node(20)
# # temp2 = Node(30)
# # head.next = temp1
# # temp1.prev = head
# # temp1.next = temp2
# # temp2.prev = temp1
```


### CIRCULAR LINKEDLIST Implementation
```
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printCLL(head):
    if head is None:
        return
    print(head.data, end=' ')
    curr = head.next
    while curr is not head:
        print(curr.data,end=' ')
        curr = curr.next


def insertCLL(head,val): #insert at beginning
    newNode = Node(val) #method2 : O(1)
    if head is None:
        return newNode
    else:
        newNode.next = head.next
        head.next = newNode
        head.data,newNode.data = newNode.data,head.data #swap i.e, data at head is changed
        return head

    # if head is None:
    #     return newNode
    #
    # curr = head   #method1 : O(n)
    # while curr.next != head:
    #     curr = curr.next
    #
    # curr.next = newNode
    # newNode.next = head
    # return newNode


def insertENDCLL(head,val):
    newNode = Node(val) #O(1)
    if head is None:
        return newNode
    else:
        newNode.next = head.next
        head.next = newNode
        newNode.data,head.data = head.data,newNode.data #swap
        return newNode

    # newNode = Node(val) #O(n)
    # if head is None:
    #     return newNode
    # curr = head
    # while curr.next != head: #here if we write curr only instead of curr.next it will stay at head only.
    #     curr = curr.next
    # curr.next = newNode
    # newNode.next = head
    # return head



def delete_head(head): #delete head node i.e first node
    if head is None or head.next:
        return None
    else:
        head.data = head.next.data
        head.next = head.next.next
        return head
    # if head is None or head.next:
    #     return None
    # else:
    #     cur = head  # O(n)
    #     while cur.next != head:
    #         cur = cur.next
    #     cur.next = head.next
    #     return cur.next

def del_kth(head,k):
    if head is None:
        return head
    elif k == 1:
        return delete_head(head)
    else:
        curr = head
        for i in range(k-2):
            curr = curr.next
        curr.next = curr.next.next
        return head


#driver code
head = Node(5)
head.next = Node(10)
head.next.next = Node(15) #till this singly linked list
head.next.next.next = head #make circular
# printCLL(head) # 5 10 15 circular linked list is printed
# h = insertCLL(head,20)
# h = insertENDCLL(head,3)
h = delete_head(head)
printCLL(h)
```
