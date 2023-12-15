# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return node
        clones = {node.val: Node(node.val, [])}
        queue = [node] if node else []
        while queue:
            curr_node = queue.pop(0)
            new_clone = clones[curr_node.val]

            for neighbor in curr_node.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                new_clone.neighbors.append(clones[neighbor.val])

        return clones[node.val]

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
one.neighbors = [two, four]
two.neighbors = [one, three]
three.neighbors = [two, four]
four.neighbors = [one, three]

new_one = Solution().cloneGraph(one)
new_two = new_one.neighbors[0]
new_four = new_one.neighbors[1]
new_three = new_two.neighbors[1]

print(list(map(lambda x: x.val, new_one.neighbors)))
print(list(map(lambda x: x.val, new_two.neighbors)))
print(list(map(lambda x: x.val, new_three.neighbors)))
print(list(map(lambda x: x.val, new_four.neighbors)))