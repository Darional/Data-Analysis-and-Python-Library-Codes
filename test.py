
arr = [5,1,2,3,4,4,4,4,4,4,6,7,6,77,1]
num = 0
# indices = [i for i, x in enumerate(arr) if x == num]
# enumare => para un arreglo crea un nuevo arreglo de la forma (indice, valor)
# enumerate(arr)
"""
indices = []
for i,x in enumerate(arr):
    if x == num:
        indices.append(i)
print([x for x in enumerate(arr)])
e = enumerate(arr)
print(next(e))
print(e)

        """
#[0,5] -> 5 - 0 - 1
#[0,2,2,3,4,1,2,5,3,4,32,1]
a = {1: 4,
     2: 9,
     3: 2,
     99: 99 }
print(min(a, key=a.get))