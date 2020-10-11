from binarytree import Node
root = Node(3)
root.left = Node(6)
root.right = Node(8)

# Getting binary tree
print('Binary tree:', root)

#Getting list of nodes
print('List of nodes:', list(root))

#Getting inorder of nodes
print('Inorder of nodes:', root.inorder)

#checking tree properties
print('Size of tree:', root.size)
print('Height of tree:', root.height)

#Get all properties at once
print('Properties of tree: \n', root.properties)
