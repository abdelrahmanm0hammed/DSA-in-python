# example of nums [4,5,1,2,3]


def count_rotations_linear(nums):
    position = 0 #what is the initial value of the position
    while position < len(nums): #when should the loop end
        if position >0 and nums[position-1]> nums[position]: #succes criteria :check whether the number at the current position is smaller than the number before it 
            return position
        
        #move to the next position
        position +=1
    return 0 #what if none of the positions passed the check
    

