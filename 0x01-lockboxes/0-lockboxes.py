#!/usr/bin/env python3
'''lockboxes func'''


def canUnlockAll(boxes):
    '''func to unlock boxes'''
    n = len(boxes)
    unlocked = [False] * n  # Track unlocked boxes
    unlocked[0] = True  # The first box is always unlocked
    queue = [0]  # Start with the first box

    while queue:
        box_index = queue.pop(0)
        for key in boxes[box_index]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)
