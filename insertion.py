A=[]
for s in range(10):
    A.append(int(input("Enter a number : ")))
print(A)

def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while(i>=0 and A[i]>key):
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
        
print("Sorted array")
insertionSort(A)
print(A)
