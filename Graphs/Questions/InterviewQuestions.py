# 1. Given a directed graph and two nodes (S and E), design an algorithm to find 
# out whether there is a route from S to E.

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        visited = [startNode]
        queue = [startNode]
        path = False
        while queue:
            dequeuedVertex = queue.pop(0)
            for adjacentVertex in self.gdict[dequeuedVertex]:
                if adjacentVertex not in visited:
                    if adjacentVertex == endNode:
                        path = True
                        break
                    else:
                        visited.append(adjacentVertex)
                        queue.append(adjacentVertex)
        return path
    
customDict = { 
              "a": ["c", "d", "b"],
              "b": ["j"],
              "c": ["g"],
              "d": [],
              "e": ["f", "a"],
              "f": ["i"],
              "g": ["d", "h"],
              "h": [],
              "i": [],
              "j": [],
              }

g = Graph(customDict)
print(g.checkRoute("a", "b"))
print(g.checkRoute("a", "e"))
print(g.checkRoute("e", "h"))

# 2. Given a sorted (increasing order) array with unique integer elements, write an algorithm to create
# a binary search tree with minimal height.

class BinarySearchTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)
    
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def minimalTree(sortedArray):
    if len(sortedArray) == 0:
        return None
    if len(sortedArray) == 1:
        return BinarySearchTree(sortedArray[0])
    mid = int(len(sortedArray)/2)
    left = minimalTree(sortedArray[:mid])
    right = minimalTree(sortedArray[mid+1:])
    return BinarySearchTree(sortedArray[mid], left, right)



sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bst = minimalTree(sortedArray)
bst.display()

print("*** QUESTION 3 *** \n")
# 3. Given a binary search tree, design an algorithm which creates a linked list of all the nodes
# at each depth (i.e, if you have a tree with depth D, you'll have D linked lists)

class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)
    def __str__(self):
        return "({val})".format(val = self.val) + str(self.next)

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def depth(tree):
    if tree == None:
        return 0
    if tree.left == None  and tree.right == None:
        return 1
    else:
        depthLeft = 1 + depth(tree.left)
        depthRight = 1 + depth(tree.right)
        if depthLeft > depthRight:
            return depthLeft
        else:
            return depthRight

def treeToLinkedList(tree, custDict = {}, d = None):
    if d == None:
        d = depth(tree)
    if custDict.get(d) == None:
        custDict[d] = LinkedList(tree.val)
    else:
        custDict[d].add(tree.val)
        if d == 1:
            return custDict
    if tree.left != None:
        custDict = treeToLinkedList(tree.left, custDict, d-1)
    if tree.right != None:
        custDict = treeToLinkedList(tree.right, custDict, d-1)
    return custDict

mainTree = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)
mainTree.left = two
mainTree.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

custDict = treeToLinkedList(mainTree)
for depthLevel, linkedList in custDict.items():
    print("{0} {1}".format(depthLevel, linkedList))


print("\n *** QUESTION 4 ***")

# 4. Implement a function to check if a binary tree is balanced. For the purpose of this question,
# a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than 1.
# For tree problems, always check if we can solve the problem recursively, makes life easy.

def isBalancedHelper(root):
    if root is None:
        return 0
    leftHeight = isBalancedHelper(root.left)
    if leftHeight == -1:
        return -1
    rightHeight = isBalancedHelper(root.right)
    if rightHeight == -1:
        return -1
    if abs(leftHeight - rightHeight) > 1:
        return -1
    return max(leftHeight, rightHeight) + 1 # heigh of tree

def isBalanced(root):
    return isBalancedHelper(root) > -1

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
node1 = Node("N1")
node2 = Node("N2")
node3 = Node("N3")
node4 = Node("N4")
node5 = Node("N5")
node6 = Node("N6")

node1.left = node2
node1.right = node2
node2.left = node4
node2.right = node5
node3.right = node6

print(isBalanced(node1))

print("\n *** QUESTION 5 ***")

# 5. Implement a function to check if a binary tree is a Binary Search Tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def helper(node, minValue = float('-inf'), maxValue = float('inf')):
    if not node:
        return True
    val = node.value
    if val <= minValue or val >= maxValue:
        return False
    if not helper(node.left, minValue, val):
        return False
    if not helper(node.right, val, maxValue):
        return False
    return True

def isValidBST(root):
    return helper(root)

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

print(isValidBST(root1))

root2 = TreeNode(4)
root2.left = TreeNode(1)
root2.right = TreeNode(3)

print(isValidBST(root2))

print("\n *** QUESTION 6 ***")
# 5. Write an algorithm to find the next node (i.e. in-order successor) of given node in a binary
# search tree. You may assume that each node has a link to its parent.

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
    
def minValue(node):
    current = node
    while current is not None:
        if current.left is None:
            break
        current = current.left
    return current

def inOrderSuccessor(root, currentNode):
    if currentNode.right is not None:
        return minValue(currentNode.right)
    
    parent = currentNode.parent
    while parent is not None:
        if currentNode != parent.right:
            break
        currentNode = parent
        parent = parent.parent
    return parent

def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        return node
    
root = None
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 9)

temp = root.left.right # 3

successor = inOrderSuccessor(root, temp)

if successor is not None:
    print("Inorder successor of %d is %d" %(temp.data, successor.data))
else:
    print("Inorder successor does not exist")
    
print("\n *** QUESTION 7 ***")
# You are given a list of projects and a list of dependencies(which is a list of pairs of projects, 
# where the second project is dependent on the first project). All of a project's dependencies must be built before the project is.
# Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

# projects a, b, c, d, e, f
# dependencies: (a, b), (f, b), (b, d), (f, a), (d, c)

def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
customGraph = createGraph(projects, dependencies)
print(customGraph)

def getProjectsWithDependencies(graph):
    projectsWithDependencies = set()
    for project in graph:
        projectsWithDependencies = projectsWithDependencies.union(set(graph[project]))
    return projectsWithDependencies

projectsWithDependencies = getProjectsWithDependencies(customGraph)
print(projectsWithDependencies)

def getProjectsWithoutDependencies(projectWD, graph):
    projectsWODependencies = set()
    for project in graph:
        if not project in projectWD:
            projectsWODependencies.add(project)
    return projectsWODependencies

print(getProjectsWithoutDependencies(projectsWithDependencies, customGraph))

def findBuildOrder(projects, dependencies):
    buildOrder = []
    projectGraph = createGraph(projects, dependencies)
    while projectGraph:
        projectsWithDependencies = getProjectsWithDependencies(projectGraph)
        projectsWODependencies = getProjectsWithoutDependencies(projectsWithDependencies, projectGraph)
        if len(projectsWODependencies) == 0 and projectGraph:
            raise ValueError("There is a cycle in the build order")
        for independenProjects in projectsWODependencies:
            buildOrder.append(independenProjects)
            del projectGraph[independenProjects]
    return buildOrder

print(findBuildOrder(projects, dependencies))

print("\n *** QUESTION 10 ***")
# 10. Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
# Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.

def findNodeInTree(target, rootNode):
    if not rootNode:
        return False
    if target == rootNode:
        return True
    else:
        return (findNodeInTree(target, rootNode.left) or findNodeInTree(target, rootNode.right))

def findFirstCommonAncestor(n1, n2, root):
    n1OnLeft = findNodeInTree(n1, root.left)
    n2OnLeft = findNodeInTree(n2, root.left)
    
    if n1OnLeft ^ n2OnLeft: # exclusive OR
        return root
    else:
        if n1OnLeft:
            return findFirstCommonAncestor(n1, n2, root.left)
        else:
            return findFirstCommonAncestor(n1, n2, root.right)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

node54 = Node(54)
node88 = Node(88, node54)
node35 = Node(35)
node22 = Node(22, node35, node88)
node33 = Node(33)
node90 = Node(90, None, node33)
node95 = Node(95)
node99 = Node(99, node90, node95)
node44 = Node(44, node22, node99)
node77 = Node(77)
rootNode = Node(55, node44, node77)

commonAncestor = findFirstCommonAncestor(node88, node33, rootNode)
print(commonAncestor.value)
