
# Return the id of the closest value of the given number
def search_the_closest_id(A: list, number):
    A = list(enumerate(A))  # The new list has the items (id, value)
    minimum = 10**10
    minimum_value_id = 0
    
    # 2 Ways to sort the list (Second little faster)
    sorted_list_enumerated = sorted(A, key=lambda x: x[1]) 
    # sorted_list_enumerated = sorted((value, id) for id, value in enumerate(A))

    for id, value in sorted_list_enumerated:
        difference = abs(value - number)
        if difference < minimum and difference != 0:
            minimum_value_id = id
            minimum = difference
    return minimum_value_id

def optimizedReplace(A, B):
    C = {}
    result = []
    sorted_list_enumerated = sorted((value, id) for id, value in enumerate(B))
    
    for i in range(len(sorted_list_enumerated)):
        now_value, now_id = sorted_list_enumerated[i - 1]
        ahead_value, ahead_id = sorted_list_enumerated[i]
        if len(B)>1:
            behind_value, behind_id = sorted_list_enumerated[i - 2]
            behind_difference = abs(behind_value - now_value)
        else:
            behind_difference = 10**10

        
        ahead_difference = abs(ahead_value - now_value)
        if behind_difference < ahead_difference:
            C[now_id] = behind_id
        else:
            C[now_id] = ahead_id
    for i in range(len(B)):
        result.append(A[C[i]])
    return result
A = [1]
B = [1]

print(optimizedReplace(A, B))