def solution(list1, list2):
    list2 = set(list2)
    result = [i in list2 for i in list1]
    
    return result
 
    
input1 = ["mars", "jupiter", "venus", "earth"]
input2 = ["earth", "mars", "neptune"]
print(solution(input1, input2))