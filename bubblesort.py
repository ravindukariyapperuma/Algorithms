A=[]
for s in range(8):
    A.append(int(input("Enter a number : ")))
print(A)

ln = len(A)
def bubbleSort(A):
    for i in range(ln):
        for j in range((ln-1),i,-1):
            if(A[j] < A[j-1]): #array aka anith paththata sort karanna oni nm < meka > mehema vanas karanna oni
                #A[j],A[j-1] = A[j-1],A[j]
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
                
print("Sorted array")
bubbleSort(A)
print(A)

