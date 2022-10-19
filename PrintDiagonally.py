#User function Template for python3

def downwardDigonal(N, A): 
    # code here 
    ans = []
    
    for i in range(N):
        row = 0
        col = i
        while col >= 0:
            ans.append(A[row][col])
            row += 1
            col -= 1
            
    for i in range(1, N):
        col = N - 1
        row = i
        while row < N:
            ans.append(A[row][col])
            row += 1
            col -= 1
        
    return ans
