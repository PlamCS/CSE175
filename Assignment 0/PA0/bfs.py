#
# bfs.py
#
# This file provides a function implementing breadth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS AND ACKNOWLEDGMENTS
#
# YOUR NAME - THE DATE
# Psalm Bautista - 9/15/23


from route import Node
from route import Frontier


def BFS(problem, repeat_check=False):
    """Perform breadth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    parent = Node(problem.start)
    if problem.is_goal(parent):
        return parent
    visited = [parent]
    queue = Frontier(parent)
    while not queue.is_empty():
        branch = queue.pop()
        if problem.is_goal(branch.loc):
            return branch
        for node in branch.expand(problem):
            if repeat_check:
                if node not in visited:
                    visited.append(node)
                    queue.add(node)
            else:
                queue.add(node)
    return None
