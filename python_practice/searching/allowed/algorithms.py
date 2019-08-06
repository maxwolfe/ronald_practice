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
            node_type=TreeNode,
    ):
        '''
        Initialize a searching algorithm with a starting node

        :param start: the starting node for the search algorithm
        '''

        if not isinstance(
                start,
                node_type,
        ):
            raise TypeError(
                    'Starting point must be a valid Node object',
            )

        self.start = start

    def __iter__(
            self,
    ):
        self.ordering = deque(
                [
                    self.start,
                ],
        )

        return self

    def __next__(
            self,
    ):
        raise NotImplementedError(
                'The search strategy must be implemented per-class',
        )
