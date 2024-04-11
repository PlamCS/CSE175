#
# greedy.py
#
# This file provides a function implementing greedy best-first search for
# a route finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier. Also, this function uses heuristic function objects defined
# in the "heuristic.py" file.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
# Psalm Bautista 10/18/2023


from route import Node
from route import Frontier


def greedy_search(problem, h, repeat_check=False):
    """Perform greedy best-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    node = Node(problem.start, h_fun=h)
    if problem.is_goal(node.loc):
        return node

    frontier = Frontier(node, "h")
    reachedNodes = [node]

    while not frontier.is_empty():
        node = frontier.pop()
        if problem.is_goal(node.loc):
            return node
        for child in node.expand(problem):
            if repeat_check:
                if child not in reachedNodes:
                    frontier.add(child)
                    reachedNodes.append(child)
            else:
                frontier.add(child)
    return None
