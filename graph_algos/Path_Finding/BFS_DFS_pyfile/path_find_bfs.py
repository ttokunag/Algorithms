# returns True if the path exists
def path_find_bfs(grid):

    visited = []
    queue = [(0,0)]

    while queue:
        
        node = queue.pop(0)
        if node not in visited:
            if node[0]-1 >= 0 and grid[node[0]-1][node[1]] == 1:
                queue.append((node[0]-1, node[1]))
            if node[0]+1 < len(grid) and grid[node[0]+1][node[1]] == 1:
                queue.append((node[0]+1, node[1]))
            if node[1]-1 >= 0 and grid[node[0]][node[1]-1] == 1:
                queue.append((node[0], node[1]-1))
            if node[1]+1 < len(grid[0]) and grid[node[0]][node[1]+1] == 1:
                queue.append((node[0], node[1]+1))
            # destination coordinate
            if (len(grid)-1, len(grid[0])-1) in queue:
                return True
       
       visited.append(node)
    
    return False
