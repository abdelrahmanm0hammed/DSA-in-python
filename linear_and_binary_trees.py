#Binary Search trees, Traversals and Balancing in python
#Question one 
#As a senoior backend engineer at jovian, you are tasked with developing a fast in-memory data structure to 
#manage profile information(username, name and email) for 100 million users.It should allow the following 
#operations to be performed efficiently:
#1-Insert the profile information for a new user
#2-Find the information of a user,given their username
#3-Update the profile information of a user, given their username
#4-List all users of the platform, sorted by username
class User:
    def __init__(self,username, name, email):
        self.username = username
        self.name = name
        self.email = email