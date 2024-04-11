#
# heuristic.py
#
# This script defines a utility class that can be used as an implementation
# of a frontier state (location) evaluation function for use in route-finding
# heuristic search algorithms. When a HeuristicSearch object is created,
# initialization code can be executed to prepare for the use of the heuristic
# during search. In particular, a RouteProblem object is typically provided 
# when the HeuristicFunction is created, providing information potentially
# useful for initialization. The actual heuristic cost function, simply
# called "h_cost", takes a state (location) as an argument.
#
# YOUR COMMENTS INCLUDING CITATIONS
#
# YOUR NAME - THE DATE
# Psalm Bautista 10/18/2023


import route


class HeuristicFunction:
    """A heuristic function object contains the information needed to
    evaluate a state (location) in terms of its proximity to an optimal
    goal state."""

    def __init__(self, problem=None):
        self.problem = problem
        # PLACE ANY INITIALIZATION CODE HERE

        self.goal = problem.goal
        self.map = problem.map

        self.gasConsumption = []
        for location in self.map.loc_dict:
            for connection in self.map.connection_dict[location]:
                distance = self.map.euclidean_distance(location, connection)
                gas = distance/self.map.get(location, connection)
                if gas not in self.gasConsumption:
                    self.gasConsumption.append(gas)
        self.efficientGas = max(self.gasConsumption)

    def h_cost(self, loc=None):
        """An admissible heuristic function, estimating the cost from
        the specified location to the goal state of the problem."""
        # a heuristic value of zero is admissible but not informative
        value = 0.0
        if loc is None:
            return value
        else:
            # PLACE YOUR CODE FOR CALCULATING value OF loc HERE
            distance = self.map.euclidean_distance(loc, self.goal)
            value = distance/self.efficientGas
            return value
