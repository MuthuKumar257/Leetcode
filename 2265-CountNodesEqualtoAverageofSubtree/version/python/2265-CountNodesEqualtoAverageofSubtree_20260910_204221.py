# Last updated: 9/10/2026, 8:42:21 PM
1class Solution:
2    def __init__(self):
3        self.matchingSubtreeCount = 0  # Initialize the count of subtrees with matching averages.
4
5    # A Depth-First Search (DFS) function that returns a tuple of two values:
6    # - The sum of values within the current subtree.
7    # - The number of nodes within the current subtree.
8    def calculateSubtreeValues(self, currentNode):
9        if currentNode is None:
10            return 0, 0  # Base case: Return 0 for both sum and number of nodes if the node is None.
11
12        # Recursively calculate values for the left and right subtrees.
13        leftSubtree  = self.calculateSubtreeValues(currentNode.left)
14        rightSubtree = self.calculateSubtreeValues(currentNode.right)
15
16        # Calculate the sum of values and the number of nodes in the current subtree.
17        sumOfValues  = leftSubtree [0] + rightSubtree[0] + currentNode.val
18        numberOfNodes  = leftSubtree [1] + rightSubtree[1] + 1
19
20        # Check if the current node's value matches the average of its subtree.
21        if sumOfValues  // numberOfNodes  == currentNode.val:
22            self.matchingSubtreeCount += 1
23
24        return sumOfValues , numberOfNodes   # Return the calculated values for the current subtree.
25
26
27    def averageOfSubtree(self, root):
28        self.calculateSubtreeValues(root)  # Start the DFS from the root node.
29        return self.matchingSubtreeCount 