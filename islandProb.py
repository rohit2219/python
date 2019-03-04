#https://leetcode.com/problems/number-of-islands/submissions/
def dfs(matrix,row,col):
    visited=set()
    stack=[]
    graphMatr={}
    for i in range(row,len(matrix)):
        for j in range(col,len(matrix[0])):
            graphMatr[(i,j)]=set()
            if j+1 < len(matrix[0]) and matrix[i][j+1] == 1:
                graphMatr[(i,j)].add((i,j+1))
            if i+1 < len(matrix) and matrix[i+1][j] == 1:
                graphMatr[(i, j)].add((i+1, j))
            if j+1 < len(matrix[0]) and i+1 < len(matrix) and matrix[i+1][j + 1] == 1:
                graphMatr[(i, j)].add((i + 1, j+1))
    print('graphMatr',graphMatr)
    stack.append((row,col))
    while len(stack) > 0:
        vertex=stack.pop()
        visited.add(vertex)
        # go thru each neighbour who was not visited
        for point in graphMatr[vertex] - set(visited):
            visited.add(point)
            stack.append(point)
            if matrix[point[0]][point[1]] == 1:
                print('changing',point,'0')
                matrix[point[0]][point[1]] = 0
    return
def islandCnt(matrix):
    stack  =[]
    islandCnt=0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                islandCnt+=1
                dfs(matrix,row,col)
                matrix[row][col]=0
                print('after dfs', matrix)
    return islandCnt

inpMat=[
[1,1,1,1,0],
[1,1,0,1,0],
[1,1,0,0,0],
[0,0,0,0,0]]
#print(islandCnt(inpMat))