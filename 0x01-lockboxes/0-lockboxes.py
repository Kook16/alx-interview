#!/usr/bin/python3
'''lockboxes func'''


def canUnlockAll(boxes):
    # Number of boxes
    n = len(boxes)
    
    # A set to keep track of visited boxes
    visited = set()
    
    # A queue to keep track of keys to check
    queue = [0]
    
    # Perform BFS
    while queue:
        current = queue.pop(0)
        
        if current not in visited:
            visited.add(current)
            for key in boxes[current]:
                if key < n and key not in visited:
                    queue.append(key)
    
    # Check if all boxes are visited
    return len(visited) == n
