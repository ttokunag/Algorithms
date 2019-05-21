# returns True if the path exists
def path_exists_dfs(grid):

    visited = []
    stack = [(0,0)]

    while stack:

        node = stack.pop()
        if node not in visited:
            if node[0]-1 >= 0 and grid[node[0]-1][node[1]] == 1:
                stack.append((node[0]-1, node[1]))
            if node[0]+1 < len(grid) and grid[node[0]+1][node[1]] == 1:
                stack.append((node[0]+1, node[1]))
            if node[1]-1 >= 0 and grid[node[0]][node[1]-1] == 1:
                stack.append((node[0], node[1]-1))
            if node[1]+1 < len(grid[0]) and grid[node[0]][node[1]+1] == 1:
                stack.append((node[0], node[1]+1))
            # destination coordinate
            if (len(grid)-1, len(grid[0])-1) in stack:
                return True
        
        visited.append(node)
    
    return False
