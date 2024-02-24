def BubbleSort(A):
    for j in range(len(A) - 1):


        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i] 
