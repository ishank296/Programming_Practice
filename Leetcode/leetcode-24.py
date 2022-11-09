# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# step 1 - add dummmy node - dummy -> 1 ->2 ->3 ->4
# step 2 - cur node - 1st node, prev node - dummy node
# step 3 - perv node.next = cur node.next

