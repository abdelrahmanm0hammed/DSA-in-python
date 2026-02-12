#Binary Search trees, Traversals and Balancing in python
#Question one 
#As a senoior backend engineer at jovian, you are tasked with developing a fast in-memory data structure to 
#manage profile information(username, name and email) for 100 million users.It should allow the following 
#operations to be performed efficiently:
#1-Insert the profile information for a new user
#2-Find the information of a user,given their username
#3-Update the profile information of a user, given their username
#4-List all users of the platform, sorted by username
# You can assume that usernames are unique


#Here's a systematic strategy we'll apply for solving problems:

# 1-State the problem clearly.Identify the input & output formats.
# 2-Come up with some examples input & outputs.Try to cover all edge cases
# 3-Come up with a correct solution for the problem.State it in plain English
# 4-Implement the solution and test it using examples inputs.Fix bugs,if any
# 5-Analyze the algorithm's complexity and identify inefficiencies, if any.
# 6-Apply the right technique to overcome the inefficiency.Repeat steps 3 to 6.

# 1.State the problem clearly, Identify the input & output formats

# Problem
# We need to create a data structure which can store 100 million records and perform insertion, search, update 
# and list operations efficiently.

# input
# the key inputs to our data structure are user profiles, which contain the username, name and email of a user


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    def __str__(self):
        return f"username: {self.username}, name: {self.name} ,email: {self.email}"
    

# class UserDatabase:
#     def insert(self, user):
#         pass

#     def find(self,username):
#         pass

#     def update(self, user):
#         pass 

#     def list_all(self):
#         pass

#VVVI
#It's a good practice to list out the signatures of different class functions before we 
# actually implement the class


# 2- Come up with some example input & outputs.input

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das','biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha','siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel','vishal@example.com')

#Exercise : List some scenarios for testing the class methods insert, find, update and list_all
# 1-Insert:
#     A.Inserting into an empty database of users
#     B.Trying to insert a user with a username that already exist
#     C.Inserting a user with a username that does not exist

# 3- Come up with a correct solution. State it in plain English

# the various functions can be implemented as follows

# 1-insert:Loop through the list and add the new user at a position that keeps the list sorted
# 2-Find:Loop through the list and find the user object with the username matching the query
# 3-Update:Loop through the list, find the user object matching the query and update the details.
# 4-List :Return the list of user objects


# 4-Implement the solution and test it using example inputs.

class UserDatabase:
    def __init__(self):
        self.users = []
    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users
    
database = UserDatabase()
database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)

user = database.find('siddhant')
# print(user)
database.update(User(username='siddhant',name='Siddhant U',email='siddhantu@example.com'))
user = database.find('siddhant')
# print(user)
# print(database.list_all())

# 5-Analyze the algorithms complexity and identify inefficiencies
#the operations insert, find, update involves iterating over a list of users, in the worst case
#,they may take up to N iterations to return a result, where N is the total number of users
#list_all however, simply returns the existing internal list of users
# thus, the time complexity of the various operations are:
# 1.insert:O(N)
# 2.Find:O(N)
# 3.Update:O(N)
# 4.List:O(1)
# import time
# start_time = time.time()
# for i in range(100000000):
#     j = i*i
# end_time = time.time()
# print(f"time taken: {end_time - start_time:.4f} seconds")

#Here's a simple class representing a node within a binary tree

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    def __str__(self):
        return f"{self.key}"
# node0 = TreeNode(1)
# node1 = TreeNode(3)
# node2 = TreeNode(2)
# node3 = TreeNode(5)
# node4 = TreeNode(3)
# node5 = TreeNode(4)
# node6 = TreeNode(7)
# node7 = TreeNode(6)
# node8 = TreeNode(8)

# #connections
# node2.left = node1
# node1.left = node0
# node2.right = node3
# node3.left = node4
# node4.right = node5
# node3.right = node6 
# node6.left = node7
# node6.right = node8
# print(node2.left.left, node2.right.right.right)

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1]) 
        # print(node)       
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
        
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
        # print(node)
    
    return node
tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

tree2 = parse_tuple(tree_tuple)
print(tree2)

#Inorder Traversal

def traversal_in_order(node):
   
    if node is None:
        return [] 
    return (traversal_in_order(node.left) + [node.key] + 
        traversal_in_order(node.right))

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))
def tree_size(node):
    if node is None:
        return 0
    return 1 +(tree_size(node.left)+tree_size(node.right))

def remove_none(nums):
    return [x for x in nums if x is not None]

#Binary search tree checker function

def is_bst(node):
    if node is None:
        return True, None, None
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and
                   (min_l is None or node.key > min_l) and
                   (min_r is None or node.key < min_r)
                   )
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    return is_bst_node, min_key, max_key

#to represent the value of node 
class BSTNode():
    def __init__(self, key, value= None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node 

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)