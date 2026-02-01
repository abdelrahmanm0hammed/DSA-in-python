
#1- State the problem clearly
#Given an list of numbers [nums] sorted in an increasing fashion, and an integer[target]
#write a function to search for target in nums, if target exist then return its index otherwise return -1

#2- input and output cases
#test cases 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

#the target occurs in the first index i.e nums= [1, 2, 3, 4], target = [1] output:0
#the target occurs in the last index i.e nums= [1, 2, 3, 4], target = [4] output:3
#the target occurs in the middle i.e nums = [1,2,3,4,5], target = [3], output:2
#the target doesnt occur in the list i.e nums= [1, 2, 3], target = [4], output:-1
#the list contain only one number which is the target i.e nums= [4], target=4, output:0
#the list is empty i.e nums=[] target=1, output:-1
#the list contain repeating numbers i.e nums= [1,2,2,2,3,4], target=[3], output:4
#the target occurs in many indecies i.e nums= [1,2,3,3,4,5], target=[5], output:2

#3 state the solution in plain English
#find the number in the middle of the list
#if its equal the target then return the middle index
#if not, if it is greater than the target then search in the first half of the list
# if it is smaller than the target then search in the second half of the list 
#if its does not exist return -1


def test_location(nums, target, mid):
    mid_number = nums[mid]
    if mid_number == target:
        if mid-1 >=0 and nums[mid-1] == target:
            return 'left'
        else:
            return 'found'
    elif mid_number > target:
        return 'left'
    elif mid_number <target:
        return 'right'
    
def search(nums, target):
    lo, hi = 0, len(nums)-1
    while lo <=hi:
        mid = (lo + hi)//2
        result = test_location(nums, target, mid)
        if result == "found":
            return mid
        elif result == 'left':
            hi = mid -1
        elif result == 'right':
            lo = mid + 1        
    return -1
    




