
def bubble_sort(nums):
    # Create a copy of the list, to avoid changing it 
    nums = list(nums)

    # 4. Repeat the process n-1 times 
    for _ in range(len(nums)-1):
        
        # 1. Iterate over the array (except last element)
        for i in range(len(nums) - 1):
            
            # 2. Compare the number with
            if nums[i] > nums[i+1]:

                # 3. Swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    # Return the sorted list
    return nums

def merge(nums1, nums2):
    # List to store the results
    merged = []
    # Indices for iteration
    i, j = 0, 0

    # Loop over the two lists
    while i < len(nums1) and j < len(nums2):
        
        # Include the smaller element in the result and move to next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    # GEt the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    return merged + nums1_tail + nums2_tail
    
    
def merge_sort(nums):
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums
    # Get the midpoint 
    mid = len(nums) // 2

    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]

    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    # Combine the results of the two halves 
    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums


def partition(nums, start=0, end=None):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1
    
    # Initialize right and left pointers
    l, r = start, end-1
    # Iterate while they're apart
    while r > l:
        # print(' ', nums, l, r)
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1
        # Decrement right right pointer if number is greater than pivot 
        elif nums[r] > nums[end]:
            r -= 1

        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    # print(' ', nums, l, r)
    # Place the pivot between the two parts 
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end

def quicksort(nums, start=0, end=None):
    # print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end :
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums


## Custom Comparison function
# Question 1: You're working on a new feature on Jovian called
# "Top Notebooks of the Week". Write a function to sort a list of notebooks in 
# decreasing order of likes.
# Keep in mind that up to millions of notebooks can be created every week, so your
# function needs to be as efficient as possible

# First, we need to sort objects, not just numbers. Also, we want to sort them in the
# descending order of likes. To achieve this, all we need is a custom comparison
# function to compare two notebooks.

class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes

    def __repr__(self):
        return 'Notebook<"{}/{}", {} likes>'.format(self.username, self.title, self.likes)
    
def compare_likes (nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'
    # Note that we say nb1 is lesser than nb2 if it has higher likes, we want
    # to sort the notebooks in decreasing order of likes