#!/usr/bin/python3
"""
the Solution lockboxes problem.
"""


def canUnlockAll(boxes):
    """
    Determined whether the series of boxes locked can open
    based on the keys attained.
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for l in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = l in boxes[idx] and l != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
