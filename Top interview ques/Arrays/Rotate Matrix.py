#You are given a N x N 2D matrix A representing an image. Rotate the image by 90 degrees (clockwise).

def rotate(A):
    for i in range(len(A)):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    for i in range(len(A)):
        A[i].reverse()
    
    return A