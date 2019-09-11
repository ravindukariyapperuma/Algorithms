#LAB-7 Q1
A = []
for v in range(8):
    A.append(input('enter number: '))
print(A)

def SelectionSort(A):
    n=len(A)
    for j in range(n):
        smallest = j
        for i in range(j+1,n):
            if A[i]<A[smallest]:
                smallest = i
        temp = A[j]
        A[j]=A[smallest]
        A[smallest] = temp
            
SelectionSort(A)
print("Sorted Array: ")
print(A)
            
