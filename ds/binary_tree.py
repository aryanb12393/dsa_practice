class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)

firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode

def level_order(node):

    if node is None:
        return
    
    queue = [node]
    result = []

    while queue:
        
        level_size = len(queue)
        level = []

        for _ in range(level_size):

            node = queue.pop(0)

            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        result.append(level)
    
    print(result)


level_order(firstNode)