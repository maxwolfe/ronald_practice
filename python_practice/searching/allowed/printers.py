'''
Custom output methods
'''

import random

from allowed.algorithms import (
        Searcher,
)
from allowed.nodes import (
        TreeNode,
)


sample = TreeNode(
        5,
        [
            TreeNode(
                6,
                [
                    TreeNode(
                        7,
                    ),
                ],
            ),
            TreeNode(
                8,
                [
                    TreeNode(
                        9,
                        [
                            TreeNode(
                                10,
                                [
                                    TreeNode(
                                        11,
                                        [
                                            TreeNode(
                                                12,
                                                [
                                                    TreeNode(
                                                        13,
                                                    ),
                                                    TreeNode(
                                                        14,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    TreeNode(
                                        15,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    TreeNode(
                        16,
                    ),
                ],
            ),
        ],
)


class SearchSimulator:
    '''
    Simulates search algorithms
    '''

    def __init__(
            self,
            strategy,
            start=None,
    ):
        '''
        Initialize a searching simulator

        :param strategy: the searching algorithm to use
        :param start: the optional starting point for that search
        '''

        if start and not isinstance(
                start,
                TreeNode,
        ):
            raise TypeError(
                    'Starting point is not a valid node',
            )
        else:
            start = sample

        self.start = start

    def order(
            self,
    ):
        order = ''

        for item in self.strategy(
                self.start,
        ):
            order += '-> {item}\n'.format(
                    item=item,
            )

        return order
