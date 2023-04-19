from collections import defaultdict
from typing import List, Tuple

class GroupSummer:
    """
    Things should be a list of tuples (group, amount)

    [
        ('A', 1), ('B', 3), ('C', 4)
    ]

    this class can be used to return the totals for each group 
    """

    def __init__(self, things: List[Tuple[str, int]]):
        
        self._groups = set(g for g, t in things)
        self._sums = dict()

        for g in self._groups:
            
            self._sums[g] = 0
            
            for group, amount in things:
                if g == group:
                    self._sums[group] += amount 

    def groupsum(self, group) -> int:
        return self._sums[group]




class BetterGroupSummer:
    """
    Things should be a list of tuples (group, amount)

    [
        ('A', 1), ('B', 3), ('C', 4)
    ]

    this class can be used to return the totals for each group 
    """

    def __init__(self, things: List[Tuple[str, int]]):
        
        self._sums = defaultdict(int)
        for group, amount in things:
            self._sums[group] += amount

    def groupsum(self, group: str):
        return self._sums[group]

