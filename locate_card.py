#solution in plain english
#1-create a variable position with the value 0
#2-check whether the number at index position in card equals query
#3- if it does, position is the answer and can be returned from the function
#4-if not, increment the value of position by 1, and repeat steps 2 to 4 till we reach the last position
#5- if the number was not found, return -1

def locate_card(cards, query):
    position =0
    while position <len(cards):
        if cards[position] == query:
            return position
        else:
            position +=1
    return -1
print(locate_card([4,3,2,1],4))