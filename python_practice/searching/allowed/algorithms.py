'''
Base Classes for Types of Algorithms
'''

from collections import (
        deque,
)

from allowed.nodes import (
    TreeNode,
)


class Searcher:
    '''
    A template for implementing searching algorithms
    '''

    def __init__(
            self,
            start,
    ):
        '''
        Initialize a searching algorithm with a starting node

        :param start: the starting node for the search algorithm
        '''

        if not isinstance(
                start,
                TreeNode,
        ):
            raise TypeError(
                    'Starting point must be a valid Node object',
            )

        self.start = start

    def __iter__(
            self,
    ):
        self.ordering = deque()
        self.ordering.append(
                self.start,
        )

        return self

    def __next__(
            self,
    ):
        raise NotImplementedError(
                'The search strategy must be implemented per-class',
        )
