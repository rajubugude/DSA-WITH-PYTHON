#### Basic Implementation
```
class Binary_tree_Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


# todo basic tree understanding
bt1 = Binary_tree_Node(1)
bt2 = Binary_tree_Node(2)
bt3 = Binary_tree_Node(3)

print(bt1.data) #1
print(bt2.data) #2
print(bt3.data) #3

bt1.left = bt2 #2
bt1.right = bt3 # 3

print(bt1.left.data) #2
print(bt1.right.data) #3



class Binary_tree_Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def printbt_detailed(root): #todo postorder traversal
    if root == None:
        return None
    print(root.data, end=':')
    if root.left != None:
        print('l', root.left.data, end=',')
    if root.right != None:
        print('r', root.right.data, end=' ')
    print() #newline
    printbt_detailed(root.left)
    printbt_detailed(root.right)


def printbt_preOrder(root):
    if not root:
        return
    print(root.data, end=' ')
    printbt_preOrder(root.left)
    printbt_preOrder(root.right)


def printbt_postOrder(root):
    if root == None:
        return
    printbt_postOrder(root.left)
    printbt_postOrder(root.right)
    print(root.data,end=' ')


def printbt_inOrder(root):
    if root is None:
        return
    printbt_inOrder(root.left)
    print(root.data, end=' ')
    printbt_inOrder(root.right)

bt1 = Binary_tree_Node(1)
bt2 = Binary_tree_Node(2)
bt3 = Binary_tree_Node(3)
bt4 = Binary_tree_Node(4)
bt5 = Binary_tree_Node(5)
#
#
bt1.left = bt2
bt1.right = bt3
bt2.left = bt4
bt2.right = bt5

# printbt(bt1)
printbt_detailed(bt1)


def takeInput(): #first all left then ryt
    rootData = int(input())
    if rootData == -1: #basecase we are considering
        return None

    root = Binary_tree_Node(rootData)

    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root
```    

#### Implementation according to Questions
```
class Binary_tree_Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


from queue import Queue
def singleLineInputLevelwise(intL):
    q = Queue()
    rootData = intL[0]
    root = Binary_tree_Node(rootData)
    q.put(root)
    i = 0
    while not q.empty() and i < len(intL):
        i = i+1
        curr_data = intL[i]
        if curr_data != -1:
            curr = q.queue[0]
            curr.left = Binary_tree_Node(curr_data)
            q.put(curr.left)
        i = i + 1
        curr_data = intL[i]
        if curr_data != -1:
            curr = q.queue[0]
            curr.right = Binary_tree_Node(curr_data)
            q.put(curr.right)
        q.get()
    return root
    
    
def printlevelwiselinebyline(root): #todo bestway print linebyline levelwise
    q = Queue()
    q.put(root)
    while not q.empty():
        width = q.qsize()
        while width:
            cur = q.get()
            print(cur.data,end=' ')
            if cur.left != None:
                q.put(cur.left)
            if cur.right != None:
                q.put(cur.right)
            width = width - 1

        print()    
```
