# example of nums [4,5,1,2,3]


def count_rotations_linear(nums):
    position = 0 #what is the initial value of the position
    while position < len(nums): #when should the loop end
        if position >0 and nums[position-1]> nums[position]: #succes criteria :check whether the number at the current position is smaller than the number before it 
            return position
        
        #move to the next position
        position +=1
    return 0 #what if none of the positions passed the check
    

#stating binary solution in plain english
#given the middle element of the list compare it to the element before in i.e [3,4,5,6,7,1,2]
#if it smaller than the element before it , then the middle element index is the answer
#if not we compare it to the last element, if it is greater than the last element 
# then the answer lies in the right half of the list
# if not then the answer lie in the left half of the list

def count_rotations_binary(nums):
    lo, hi = 0, len(nums)-1
    if len(nums)==1:
        return 0
    elif len(nums)== 2:
        if nums[1] < nums[0]:
            return 1
        else:
            return 0
        
    else:

        while lo <= hi and hi>=2:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid -1] and (mid -1 >0):
                return mid
            elif nums[mid] > nums[hi]:
                lo = mid +1
                
            elif nums[mid] < nums[hi]:
                hi = mid-1
                
        return 0
print(count_rotations_binary([2,3,4,]))


