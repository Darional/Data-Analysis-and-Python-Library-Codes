def solution(s, letters):
    result = set(s) & set(letters)

    return sorted(result)

a, b = ("hello", ['h', 'a', 'e', 'i', 'o', 'u'])
print(solution(a, b))

print(list(set(["Hola", "Mundo"])))