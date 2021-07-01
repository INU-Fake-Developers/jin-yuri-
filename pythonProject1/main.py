def bubbleSort(a, N):
    j = 0
    while j < N - 1:
        i = 0
        while i < N - 1:
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
            i += 1
        j += 1
        print(a)
    return a

N = int(input('N= '))
import random
A = []
for i in range(N):
    A.append(random.randint(1, N*10))
print('정렬 전:', A)
print('정렬 후:', bubbleSort(A, N))



