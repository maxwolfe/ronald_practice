'''
Custom output methods
'''

from allowed.algorithms import (
        Searcher,
)
from allowed.nodes import (
        BinaryTreeNode,
        TreeNode,
)


sample = BinaryTreeNode(
        5,
        [
            BinaryTreeNode(
                6,
                [
                    BinaryTreeNode(
                        7,
                    ),
                ],
            ),
            BinaryTreeNode(
                8,
                [
                    BinaryTreeNode(
                        9,
                        [
                            BinaryTreeNode(
                                10,
                                [
                                    BinaryTreeNode(
                                        11,
                                        [
                                            BinaryTreeNode(
                                                12,
                                                [
                                                    BinaryTreeNode(
                                                        13,
                                                    ),
                                                    BinaryTreeNode(
                                                        14,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    BinaryTreeNode(
                                        15,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    BinaryTreeNode(
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

        if not isinstance(
                strategy(
                    start,
                ),
                Searcher,
        ):
            raise TypeError(
                    'Searching algorithm not a valid algorithm',
            )

        self.strategy = strategy

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
