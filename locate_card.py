#solution in plain english
#1-create a variable position with the value 0
#2-check whether the number at index position in card equals query
#3- if it does, position is the answer and can be returned from the function
#4-if not, increment the value of position by 1, and repeat steps 2 to 4 till we reach the last position
#5- if the number was not found, return -1

#linear search solution 

# from jovian.pythondsa import evaluate_test_case
# test = {
#     'input':{'cards':[13, 11, 10, 7, 4, 3, 1, 0],
#              'query': 7},
#              'output':3
# }

# def locate_card(cards, query):
#     position =0
#     while position <len(cards):
#         if cards[position] == query:
#             return position
#         else:
#             position +=1
#     return -1
# evaluate_test_case(locate_card, test)

def test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1 >=0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    elif mid_number > query:
        return 'right'


#Binary search solution

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo+hi)// 2
        result = test_location(cards, query, mid)
        

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1
        elif result == 'right':
            lo = mid +1
        
    return -1
print(locate_card([8, 7, 4, 3, 2, 1, 0], 1))